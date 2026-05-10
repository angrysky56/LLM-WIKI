---
title: "Graph Theory: Heuristic Search Algorithm (A-Star) Applied in Trading"
source: "https://www.mql5.com/en/articles/22184"
author:
  - "[[Hlomohang John Borotho]]"
published: 2026-05-07T15:17:35+00:00Z
created: 2026-05-08
description: "The article applies the A* heuristic to market structure by modeling validated swing highs and lows as graph nodes and weighting edges with ATR‑normalized distance, spread, and noise penalties. The engine searches the most efficient route to infer trade direction and targets, then filters signals by directional ratio, total path cost, and opposing swings. It anchors TP to the final node and SL to prior structure, with on‑chart visualization and configurable inputs."
tags:
  - "clippings"
---
### Introduction

On live markets, price prints dozens of local highs and lows, and it quickly becomes unclear which of these are meaningful structure and which are noise. Traders often sense a "direction" but cannot convert it into repeatable rules: which swings matter, where the path of least resistance runs, what is an achievable target, and which level to use for a structural stop so it isn’t arbitrary. For an algorithmic approach to the challenge is stricter: without a graph model and numeric path scoring, it is impossible to consistently filter setups and make reproducible on‑bar decisions. This article addresses that problem directly—we turn validated swings into graph nodes, construct a weighted map (ATR‑normalized distance, spread, and noise penalties), and use the A\* algorithm to find the optimal route for price. The result is a formal, testable framework for identifying high‑probability entries, structural stops, and logical profit targets.

### System Overview

The Heuristic A\* EA works as a discrete decision-making engine, not a continuous indicator. On each new bar, it scans historical price action to identify key swing highs and lows, which act as nodes in a graph. These nodes are validated to ensure the price has not already moved through them. The EA then connects the nodes with edges, where each edge has a cost based on normalized price distance, spread, and market noise. This converts the price chart into a structured, weighted map that the A\* algorithm can navigate.

![](https://c.mql5.com/2/206/AStar_price_swings.png)

The EA builds a weighted map of unbreached swing points. Each connection has a cost based on distance and market friction.

Once the graph is built, the A\* engine finds the optimal path from the node nearest to the current price to a projected trend-direction target. It evaluates paths using both the actual cost traveled (G) and the estimated remaining cost (H), always expanding the most efficient option. The final path is checked for quality. It must meet directional consistency, stay within acceptable cost limits, and remain free of opposing swing obstacles. If all conditions are met, the EA executes a trade, using the final node as the take-profit and the previous opposing swing as the stop-loss.

![](https://c.mql5.com/2/206/AStar_best_route.png)

Only high-quality paths that meet strict criteria become trades, with stops anchored to prior structure.

Configurable modules and their functions within the system architecture:

| Module | Input Group | Primary Function |
| --- | --- | --- |
| Node Detection | Swing Detection | Identifies local price extremes using a symmetrical lookback window and filters redundant or breached levels. |
| Graph Builder | A\* Engine | Constructs the edge network between nodes, calculating traversal cost based on ATR, spread, and noise penalties. |
| Pathfinder | A\* Engine | Executes the heuristic search to find the most efficient route through the price structure towards a target. |
| Signal Filter | Trade Decision | Validates the path by checking the directional ratio, total normalized cost, and presence of structural blockades. |
| Risk Manager | Risk Management | Calculates position size based on a fixed percentage of account balance and the distance to the structural stop-loss. |
| Visualizer | Visualization | Renders swing nodes, graph edges, and the selected A\* path directly on the chart for transparency. |

### Getting Started

```
//+------------------------------------------------------------------+
//|                                             Heuristic A_Star.mq5 |
//|                             Git, Copyright 2025, MetaQuotes Ltd. |
//|                     https://www.mql5.com/en/users/johnhlomohang/ |
//+------------------------------------------------------------------+
#property copyright "Git, Copyright 2025, MetaQuotes Ltd."
#property link      "https://www.mql5.com/en/users/johnhlomohang/"
#property version   "1.00"

#include <Trade\Trade.mqh>

//+------------------------------------------------------------------+
//| INPUT PARAMETERS                                                 |
//+------------------------------------------------------------------+
//--- Swing Detection ---
input group "=== Swing Detection ==="
input int    InpSwingLookback    = 5;        // Bars left/right for swing detection
input int    InpMaxNodes         = 100;      // Maximum swing nodes to keep
input int    InpMinSwingBars     = 3;        // Minimum bars between swings

//--- A* Engine ---
input group "=== A* Engine ==="
input double InpSpreadPenalty    = 1.5;      // Spread cost multiplier
input double InpNoisePenalty     = 0.5;      // Noise penalty weight
input int    InpATRPeriod        = 14;       // ATR period for normalization

//--- Trade Decision ---
input group "=== Trade Decision ==="
input double InpMinPathScore     = 0.55;     // Minimum directional ratio to trade (0-1)
input double InpMaxPathCost      = 5.0;      // Maximum total path cost (ATR multiples)
input double InpSLBufferATR      = 0.5;      // SL buffer in ATR units

//--- Risk Management ---
input group "=== Risk Management ==="
input double InpRiskPercent      = 1.5;      // Risk per trade (% of balance)
input double InpMaxSpreadPoints  = 40;       // Max allowed spread in points
input int    InpMagicNumber      = 20250413; // EA magic number
input string InpComment          = "AStarEA";

//--- Visualization ---
input group "=== Visualization ==="
input bool   InpDrawNodes        = true;     // Draw swing nodes
input bool   InpDrawEdges        = true;     // Draw graph edges
input bool   InpDrawPath         = true;     // Draw A* best path
input color  InpHighNodeColor    = clrDodgerBlue;
input color  InpLowNodeColor     = clrOrangeRed;
input color  InpEdgeColor        = clrDimGray;
input color  InpPathColor        = clrLime;
input int    InpNodeSize         = 3;
```

To get started, we define the input parameters that control how the A\* Expert Advisor operates. We organize them into groups for clarity and ease of use. The swing detection settings determine how we identify and filter swing highs and lows. The A\* engine settings control how path costs are calculated using spread, noise, and ATR. The trade decision section defines when a path is strong enough to execute a trade. The risk management inputs handle position sizing, spread limits, and trade identification. Finally, the visualization settings allow us to draw nodes, edges, and paths on the chart with customizable colors and sizes.

```
//+------------------------------------------------------------------+
//| DATA STRUCTURES                                                  |
//+------------------------------------------------------------------+
struct SwingNode
  {
   double            price;
   datetime          time;
   bool              isHigh;
   bool              isValid;
   int               barIndex;   // bar index at detection time
  };

struct Edge
  {
   int               from;
   int               to;
   double            cost;
  };

struct AStarNode
  {
   int               index;
   double            g;
   double            h;
   double            f;
   int               parent;
   bool              inOpen;
   bool              inClosed;
  };

//+------------------------------------------------------------------+
//| GLOBAL VARS                                                      |
//+------------------------------------------------------------------+
CTrade trade;

SwingNode  Nodes[];
Edge       Edges[];
AStarNode  AStar[];
int        BestPath[];     // indices into Nodes[]

int        NodeCount  = 0;
int        EdgeCount  = 0;
int        PathLength = 0;

datetime   LastBarTime = 0;
double     CachedATR   = 0;

//--- Visualization object name prefix
string OBJ_PREFIX = "ASTAR_";

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
  {
   trade.SetExpertMagicNumber(InpMagicNumber);
   trade.SetDeviationInPoints(20);
   trade.SetTypeFilling(ORDER_FILLING_FOK);

   ArrayResize(Nodes, InpMaxNodes + 10);
   ArrayResize(Edges, (InpMaxNodes * 3) + 10);
   ArrayResize(AStar, InpMaxNodes + 10);
   ArrayResize(BestPath, InpMaxNodes + 10);

   Print("Heuristic A_Star EA initialized. Magic=", InpMagicNumber);
   return INIT_SUCCEEDED;
  }
```

Here, we define the core data structures that represent our graph and A\* logic. The SwingNode structure stores key market points, including price, time, type (high or low), and validity. The edge structure connects these nodes and assigns a movement cost between them. The AStarNode structure holds the values needed for pathfinding, such as the actual cost (g), estimated cost (h), total cost (f), and parent reference. These structures allow us to model price action as a weighted graph that the A\* algorithm can process.

We then declare global variables to store nodes, edges, and A\* states, along with the resulting best path. We track counts for nodes, edges, and path length to manage memory efficiently. Additional variables store timing and ATR values for calculations. The OnInit() function prepares the EA by setting trade parameters such as magic number and execution type. It also resizes all arrays based on input limits and confirms initialization with a log message.

```
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
  {
   ClearVisualization();
   Print("Heuristic A_Star EA removed.");
  }

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
  {
   //--- Only process on new bar
   if(!IsNewBar())
      return;

   //--- Cache ATR for this bar cycle
   CachedATR = GetATR();
   if(CachedATR <= 0)
      return;

   //--- Check spread
   double spreadPoints = (double)SymbolInfoInteger(_Symbol, SYMBOL_SPREAD);
   if(spreadPoints > InpMaxSpreadPoints)
     {
      Print("Spread too wide: ", spreadPoints, " points. Skipping.");
      return;
     }

   //--- Core pipeline
   UpdateSwings();    // Detect swing nodes
   BuildGraph();      // Construct edge graph
   RunAStar();        // Heuristic + A* search
   EvaluatePath();    // Decision logic + execution
   DrawVisualization(); // Render to chart
  }
```

The OnDeinit() function clears all chart objects to keep the workspace clean and log that the EA has been removed. In the OnTick() function, we ensure that the system only runs once per new bar to improve efficiency. We then cache the ATR value for consistent calculations and check that the current spread is within acceptable limits before proceeding.

If all conditions are met, we execute the full processing pipeline in sequence. We detect and update swing nodes, build the graph structure, and run the A\* algorithm to find the optimal path. We then evaluate the path to decide whether a trade should be executed. Finally, we draw the nodes, edges, and selected path on the chart for visualization and analysis.

```
//+------------------------------------------------------------------+
//| SWING DETECTION (NODE GENERATION)                                |
//+------------------------------------------------------------------+
void UpdateSwings()
  {
   NodeCount = 0;

   int totalBars = MathMin(Bars(_Symbol, _Period) - InpSwingLookback - 1,
                           InpMaxNodes * 4);

   double currentPrice = SymbolInfoDouble(_Symbol, SYMBOL_BID);

   for(int i = InpSwingLookback; i < totalBars && NodeCount < InpMaxNodes; i++)
     {
      bool isSwingHigh = IsSwingHigh(i, InpSwingLookback);
      bool isSwingLow  = IsSwingLow(i, InpSwingLookback);

      if(!isSwingHigh && !isSwingLow)
         continue;

      double nodePrice = isSwingHigh
                         ? iHigh(_Symbol, _Period, i)
                         : iLow(_Symbol, _Period, i);

      datetime nodeTime = iTime(_Symbol, _Period, i);

      //--- CRITICAL: Remove nodes where price has already passed through
      //--- (blown-through levels are invalid)
      if(!IsNodeValid(nodePrice, isSwingHigh, i, currentPrice))
         continue;

      //--- Minimum separation filter — avoid duplicate adjacent swings
      if(NodeCount > 0)
        {
         int prevIdx = NodeCount - 1;
         if(Nodes[prevIdx].isHigh == isSwingHigh &&
            MathAbs(Nodes[prevIdx].price - nodePrice) < CachedATR * 0.3)
            continue;
        }

      Nodes[NodeCount].price    = nodePrice;
      Nodes[NodeCount].time     = nodeTime;
      Nodes[NodeCount].isHigh   = isSwingHigh;
      Nodes[NodeCount].isValid  = true;
      Nodes[NodeCount].barIndex = i;
      NodeCount++;
     }

   //--- Trim to max
   if(NodeCount > InpMaxNodes)
      NodeCount = InpMaxNodes;
  }

//+------------------------------------------------------------------+
//|  Swing High                                                      |
//+------------------------------------------------------------------+
bool IsSwingHigh(int bar, int n)
  {
   double h = iHigh(_Symbol, _Period, bar);
   for(int j = 1; j <= n; j++)
     {
      if(iHigh(_Symbol, _Period, bar - j) >= h)
         return false;
      if(iHigh(_Symbol, _Period, bar + j) >= h)
         return false;
     }
   //--- True if bar[i].high is greater than N bars on each side
   return true;
  }

//+------------------------------------------------------------------+
//|  Swing Low                                                       |
//+------------------------------------------------------------------+
bool IsSwingLow(int bar, int n)
  {
   double l = iLow(_Symbol, _Period, bar);
   for(int j = 1; j <= n; j++)
     {
      if(iLow(_Symbol, _Period, bar - j) <= l)
         return false;
      if(iLow(_Symbol, _Period, bar + j) <= l)
         return false;
     }
//--- True if bar[i].low is lower than N bars on each side
   return true;
  }
```

In this code section, we handle swing detection by scanning historical price data and converting key turning points into graph nodes. At the start of UpdateSwings(), we reset the node count and limit how many bars we analyze to maintain performance. For each bar within the range, we check whether it forms a swing high or swing low using predefined lookback conditions. If a valid swing is found, we extract its price and time. We then apply a critical validation step to ensure price has not already moved through that level, since such nodes are no longer meaningful for future decisions. This keeps our graph clean and focused on relevant structure.

We also apply a spacing filter to avoid clustering similar swing points too close together, using ATR as a dynamic threshold. If a new swing is too close to the previous one and of the same type, we ignore it. Once a node passes all checks, we store its details, including price, time, type, and bar index. The helper functions IsSwingHigh() and IsSwingLow() ensure that a bar is only classified as a swing if it is higher or lower than a set number of bars on both sides. This strict condition helps us capture meaningful market structure rather than noise, resulting in a well-defined set of nodes for the A\* engine.

```
//+------------------------------------------------------------------+
//|  Validate node                                                   |
//+------------------------------------------------------------------+
bool IsNodeValid(double price, bool isHigh, int barIndex, double currentPrice)
  {
   //--- Check bars between barIndex and bar 0 (current)
   for(int b = barIndex - 1; b >= 0; b--)
     {
      if(isHigh)
        {
         //--- If any close above the swing high -> node breached
         if(iClose(_Symbol, _Period, b) > price)
            return false;
        }
      else
        {
         //--- If any close below the swing low -> node breached
         if(iClose(_Symbol, _Period, b) < price)
            return false;
        }
     }
   return true;
  }

//+------------------------------------------------------------------+
//| GRAPH CONSTRUCTION                                               |
//+------------------------------------------------------------------+
void BuildGraph()
  {
   EdgeCount = 0;
   if(NodeCount < 2)
      return;

   double spread   = SymbolInfoDouble(_Symbol, SYMBOL_ASK)
                     - SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double atr      = CachedATR;

   for(int i = 0; i < NodeCount; i++)
     {
      //--- Connect to immediate neighbours (prev + next)
      for(int delta = -1; delta <= 1; delta += 2)
        {
         int j = i + delta;
         if(j < 0 || j >= NodeCount)
            continue;

         double edgeCost = CalculateEdgeCost(i, j, atr, spread);

         //--- Store edge
         if(EdgeCount < ArraySize(Edges) - 1)
           {
            Edges[EdgeCount].from = i;
            Edges[EdgeCount].to   = j;
            Edges[EdgeCount].cost = edgeCost;
            EdgeCount++;
           }
        }

      //--- Optional cross-connections: skip one node
      for(int delta = -2; delta <= 2; delta += 4)
        {
         int j = i + delta;
         if(j < 0 || j >= NodeCount)
            continue;

         double edgeCost = CalculateEdgeCost(i, j, atr, spread) * 1.2; // slight penalty

         if(EdgeCount < ArraySize(Edges) - 1)
           {
            Edges[EdgeCount].from = i;
            Edges[EdgeCount].to   = j;
            Edges[EdgeCount].cost = edgeCost;
            EdgeCount++;
           }
        }
     }
  }
```

In the IsNodeValid() function, the system ensures that each swing node is still relevant before including it in the graph. The function checks all candles between the node’s formation and the current bar. For a swing high, if any closing price moves above that level, the node is considered breached and rejected. For a swing low, the opposite applies, where any close below the level invalidates it. This process removes levels that price has already interacted with, ensuring that only untouched and meaningful structure is preserved for further analysis.

Within the BuildGraph() function, the focus shifts to constructing connections between valid nodes. The process begins by resetting the edge count and confirming that there are enough nodes to form a graph. Each node is then connected to its immediate neighbors, creating a simple and structured path network. Additional cross-connections are introduced by skipping one node, allowing alternative routes to exist. These connections carry a slightly higher cost to keep them less favorable. All edge costs are calculated using ATR and spread, which ensures the graph reflects real market conditions and can be effectively used by the A\* algorithm.

```
//+------------------------------------------------------------------+
//|  Calculate Edge Cost                                             |
//+------------------------------------------------------------------+
double CalculateEdgeCost(int from, int to, double atr, double spread)
  {
   double priceDiff = MathAbs(Nodes[from].price - Nodes[to].price);

   //--- Normalize by ATR
   double normalizedDist = (atr > 0) ? priceDiff / atr : priceDiff;

   //--- Spread cost (in ATR units)
   double spreadCost = (atr > 0) ? spread / atr : 0;

   //--- Noise penalty: penalize same-type adjacent nodes (low→low = noise)
   double noisePenalty = 0;
   if(Nodes[from].isHigh == Nodes[to].isHigh)
      noisePenalty = InpNoisePenalty;

   return normalizedDist + (InpSpreadPenalty * spreadCost) + noisePenalty;
  }

//+------------------------------------------------------------------+
//| HEURISTIC FUNCTION                                               |
//+------------------------------------------------------------------+
double Heuristic(int current, int target)
  {
   double distance = MathAbs(Nodes[current].price - Nodes[target].price);
   return (CachedATR > 0) ? distance / CachedATR : distance;
  }

//+------------------------------------------------------------------+
//| A* ENGINE                                                        |
//+------------------------------------------------------------------+
void RunAStar()
  {
   PathLength = 0;
   if(NodeCount < 2)
      return;

   //--- Determine start: node closest to current price
   int startNode = FindStartNode();
   //--- Determine goal: support/resistance target
   int goalNode  = FindGoalNode(startNode);

   if(startNode < 0 || goalNode < 0 || startNode == goalNode)
      return;

   //--- Initialize A* state
   ArrayResize(AStar, NodeCount);
   for(int i = 0; i < NodeCount; i++)
     {
      AStar[i].index    = i;
      AStar[i].g        = 1e18;
      AStar[i].h        = 0;
      AStar[i].f        = 1e18;
      AStar[i].parent   = -1;
      AStar[i].inOpen   = false;
      AStar[i].inClosed = false;
     }

   AStar[startNode].g      = 0;
   AStar[startNode].h      = Heuristic(startNode, goalNode);
   AStar[startNode].f      = AStar[startNode].h;
   AStar[startNode].inOpen = true;

   bool goalReached = false;

   while(true)
     {
      //--- Pick node in OPEN with lowest f
      int current = -1;
      double bestF = 1e18;
      for(int i = 0; i < NodeCount; i++)
        {
         if(AStar[i].inOpen && AStar[i].f < bestF)
           {
            bestF   = AStar[i].f;
            current = i;
           }
        }

      if(current < 0)
         break; // OPEN is empty

      AStar[current].inOpen   = false;
      AStar[current].inClosed = true;

      if(current == goalNode)
        {
         goalReached = true;
         break;
        }

      //--- Expand neighbours via edges
      for(int e = 0; e < EdgeCount; e++)
        {
         if(Edges[e].from != current)
            continue;

         int neighbor = Edges[e].to;
         if(neighbor < 0 || neighbor >= NodeCount)
            continue;
         if(AStar[neighbor].inClosed)
            continue;

         double tentativeG = AStar[current].g + Edges[e].cost;

         if(tentativeG < AStar[neighbor].g)
           {
            AStar[neighbor].g      = tentativeG;
            AStar[neighbor].h      = Heuristic(neighbor, goalNode);
            AStar[neighbor].f      = AStar[neighbor].g + AStar[neighbor].h;
            AStar[neighbor].parent = current;
            AStar[neighbor].inOpen = true;
           }
        }
     }

   //--- Reconstruct path if goal was reached
   if(goalReached)
     {
      int temp[];
      ArrayResize(temp, NodeCount);
      int len = 0;
      int cur = goalNode;
      while(cur != -1 && len < NodeCount)
        {
         temp[len++] = cur;
         cur = AStar[cur].parent;
        }

      //--- Reverse into BestPath
      ArrayResize(BestPath, len);
      for(int i = 0; i < len; i++)
         BestPath[i] = temp[len - 1 - i];
      PathLength = len;
     }
  }
```

The CalculateEdgeCost() function defines how expensive it is for price to move between two nodes. It starts by measuring the absolute price difference and then normalizes it using ATR to account for market volatility. A spread cost is added to reflect real trading conditions, also scaled by ATR. The function then applies a noise penalty when two connected nodes are of the same type, such as high-to-high or low-to-low, since this often represents choppy or less meaningful movement. The final cost combines all these components, producing a balanced and realistic weight for each edge in the graph.

Then, the Heuristic() function provides the estimated cost from a current node to the target node. It calculates the price distance between the two nodes and normalizes it using the cached ATR value. This keeps the heuristic consistent with the edge cost logic and ensures that distance is evaluated relative to market volatility. By doing this, the A\* algorithm can make more informed decisions about which paths are likely to be efficient, rather than relying on raw price differences alone.

![](https://c.mql5.com/2/206/AStar_Forml.png)

In the RunAStar() function, the system runs the A\* pathfinding process. It selects the start node nearest to the current price and a goal node based on market structure. It then iteratively expands the lowest-cost node and updates parents and costs until it reaches the goal, after which it reconstructs the final path. This path represents the most efficient route for price movement according to the defined cost and heuristic logic.

![](https://c.mql5.com/2/206/Core_Formula.png)

```
//+------------------------------------------------------------------+
//| Find Starting Node                                               |
//+------------------------------------------------------------------+
int FindStartNode()
  {
   //--- Find node closest to current price (start)
   double currentPrice = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   int    best = -1;
   double bestDist = 1e18;

   for(int i = 0; i < NodeCount; i++)
     {
      double d = MathAbs(Nodes[i].price - currentPrice);
      if(d < bestDist)
        {
         bestDist = d;
         best     = i;
        }
     }
   return best;
  }

//+------------------------------------------------------------------+
//|  Find Goal Node                                                  |
//+------------------------------------------------------------------+
int FindGoalNode(int startNode)
  {
   //--- Find goal node: nearest unbreached resistance (for buy context) or support (sell)
   if(startNode < 0)
      return -1;

   double currentPrice = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double atr          = CachedATR;

   //--- Count upward vs downward nodes from start to get initial bias
   int upCount = 0, downCount = 0;
   for(int i = 0; i < NodeCount; i++)
     {
      if(Nodes[i].price > currentPrice)
         upCount++;
      else
         downCount++;
     }

   bool biasUp = (upCount >= downCount);

   //--- Goal = first swing of the opposing type, furthest in direction of bias
   int   bestGoal = -1;
   double bestDist = 0;

   for(int i = 0; i < NodeCount; i++)
     {
      if(i == startNode)
         continue;

      bool isAbove = Nodes[i].price > currentPrice;
      if(isAbove != biasUp)
         continue; // wrong side

      double d = MathAbs(Nodes[i].price - currentPrice);
      if(d > bestDist && d < atr * 8.0) // within 8 ATR range
        {
         bestDist  = d;
         bestGoal  = i;
        }
     }

   return bestGoal;
  }
```

In the FindStartNode() function, we determine where the A\* search should begin by locating the node closest to the current market price. We retrieve the current bid price and compare it against all stored node prices. For each node, we calculate the absolute distance from the current price and keep track of the smallest value. The node with the shortest distance is selected as the starting point, since it best represents the market’s current position within the graph structure.

Then in the FindGoalNode() function, we define where the pathfinding process should aim. We first establish a directional bias by counting how many nodes lie above and below the current price. If more nodes are above, we assume an upward bias; otherwise, a downward bias. We then search for a suitable goal node in that direction, ignoring nodes on the opposite side. Among the valid candidates, we select the one that is furthest from the current price but still within a reasonable range, capped at a multiple of ATR. This ensures the goal is both directionally consistent and realistically reachable within current market conditions.

```
//+------------------------------------------------------------------+
//| PATH EVALUATION & TRADE DECISION                                 |
//+------------------------------------------------------------------+
void EvaluatePath()
  {
   if(PathLength < 2)
      return;

   //--- Compute directional score
   int upMoves   = 0;
   int downMoves = 0;
   double totalCost = 0;

   for(int i = 1; i < PathLength; i++)
     {
      double priceDelta = Nodes[BestPath[i]].price - Nodes[BestPath[i-1]].price;
      if(priceDelta > 0)
         upMoves++;
      else
         downMoves++;
     }

   //--- Accumulate total path cost from A* g-value of goal
   int goalIdx = BestPath[PathLength - 1];
   totalCost   = AStar[goalIdx].g;

   double totalMoves    = upMoves + downMoves;
   double upRatio       = (totalMoves > 0) ? upMoves / totalMoves : 0.5;
   double downRatio     = 1.0 - upRatio;

   //--- Check opposing node on path
   bool hasOpposingNode = CheckOpposingNode();

   //--- Decision 
   int signal = 0; // 0=none, 1=buy, -1=sell

   double currentPrice = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double goalPrice    = Nodes[goalIdx].price;

   bool pathGoesUp   = goalPrice > currentPrice;
   bool pathGoesDown = goalPrice < currentPrice;

   //--- BUY conditions
   if(pathGoesUp  &&
      upRatio   >= InpMinPathScore &&
      totalCost <= InpMaxPathCost  &&
      !hasOpposingNode)
     {
      signal = 1;
     }
   //--- SELL conditions
   else
      if(pathGoesDown  &&
         downRatio   >= InpMinPathScore &&
         totalCost   <= InpMaxPathCost  &&
         !hasOpposingNode)
        {
         signal = -1;
        }

   if(signal == 0)
      return;

   // --- SL / TP Calculation ---
   double atr = CachedATR;
   double slBuffer = atr * InpSLBufferATR;

   double tp = goalPrice; // TP = final node in path
   double sl = 0;

   //--- SL = node before start on path, or fallback to previous swing
   if(PathLength >= 3)
     {
      //--- The node just before start in path context: use node index BestPath[1]
      //--- reversed — actually use the swing opposite to start
      int prevNode = FindOppositeSwingBeforeStart(BestPath[0]);
      if(prevNode >= 0)
         sl = Nodes[prevNode].price;
     }

   //--- Fallback SL
   if(sl == 0)
     {
      sl = (signal == 1)
           ? currentPrice - (atr * 1.5 + slBuffer)
           : currentPrice + (atr * 1.5 + slBuffer);
     }
   else
     {
      //--- Add buffer
      sl = (signal == 1) ? sl - slBuffer : sl + slBuffer;
     }

   ExecuteTrade(signal, sl, tp);
  }

//+------------------------------------------------------------------+
//|  Check Opposing Node                                             |
//+------------------------------------------------------------------+
bool CheckOpposingNode()
  {
   //--- Check if path contains a high-confidence opposing node (counter-trend node)
   if(PathLength < 2)
      return false;

   double currentPrice = SymbolInfoDouble(_Symbol, SYMBOL_BID);
   double goalPrice    = Nodes[BestPath[PathLength-1]].price;
   bool   goingUp      = goalPrice > currentPrice;

   for(int i = 1; i < PathLength - 1; i++)
     {
      int ni = BestPath[i];
      // Opposing = swing high blocking an uptrend, or swing low blocking downtrend
      if(goingUp  && Nodes[ni].isHigh  && Nodes[ni].price < goalPrice &&
         Nodes[ni].price > currentPrice)
         return true;
      if(!goingUp && !Nodes[ni].isHigh && Nodes[ni].price > goalPrice &&
         Nodes[ni].price < currentPrice)
         return true;
     }
   return false;
  }
```

In the EvaluatePath() function, we convert the A\* result into an actual trading decision by analyzing the structure of the computed path. We first ensure the path is valid, then measure its directional strength by counting how many moves go upward versus downward between consecutive nodes. We also retrieve the total cost of the path from the A\* calculation, which reflects how efficient or “expensive” the route is. From this, we compute directional ratios and check whether the path aligns with a clear bias toward buying or selling. We also validate the path further by checking for any opposing structure that could block price movement, ensuring we only act on clean and directional setups.

Once the path passes all conditions, we generate a trade signal and define execution levels. The take-profit is set at the final node in the path, representing the projected market target. The stop-loss is determined by either a structural swing opposite to the entry or, if unavailable, a volatility-based fallback using ATR and a buffer. This ensures the trade is protected even when the structure is unclear. The CheckOpposingNode() function reinforces safety by scanning the path for conflicting swing points that could interrupt price movement. If such a node exists within the path, the trade is rejected to avoid low-quality or obstructed setups.

```
//+------------------------------------------------------------------+
//|  Find Opposite Swing                                             |
//+------------------------------------------------------------------+
int FindOppositeSwingBeforeStart(int startNodeIdx)
  {
  //--- Find the opposite swing type just before the start node
   bool startIsHigh = Nodes[startNodeIdx].isHigh;

   for(int i = startNodeIdx + 1; i < NodeCount; i++)
     {
      if(Nodes[i].isHigh != startIsHigh)
         return i;
     }
   return -1;
  }

//+------------------------------------------------------------------+
//| EXECUTION ENGINE                                                 |
//+------------------------------------------------------------------+
void ExecuteTrade(int signal, double sl, double tp)
  {
   //--- Only one open trade at a time (per magic)
   if(HasOpenPosition())
      return;

   double ask = SymbolInfoDouble(_Symbol, SYMBOL_ASK);
   double bid = SymbolInfoDouble(_Symbol, SYMBOL_BID);

   //--- Validate SL/TP logic
   if(signal == 1)
     {
      if(sl >= ask || tp <= ask)
        {
         Print("BUY: Invalid SL/TP. SL=", sl, " TP=", tp, " Ask=", ask);
         return;
        }
     }
   else
     {
      if(sl <= bid || tp >= bid)
        {
         Print("SELL: Invalid SL/TP. SL=", sl, " TP=", tp, " Bid=", bid);
         return;
        }
     }

   //--- Risk-based lot sizing
   double entryPrice = (signal == 1) ? ask : bid;
   double slDistance = MathAbs(entryPrice - sl);
   double lots       = CalculateLotSize(slDistance);
   if(lots <= 0)
      return;

   //--- Normalize prices
   int    digits = (int)SymbolInfoInteger(_Symbol, SYMBOL_DIGITS);
   sl = NormalizeDouble(sl, digits);
   tp = NormalizeDouble(tp, digits);

   bool result = false;
   if(signal == 1)
     {
      result = trade.Buy(lots, _Symbol, ask, sl, tp, InpComment);
      Print("BUY executed. Lots=", lots, " SL=", sl, " TP=", tp,
            " PathLen=", PathLength);
     }
   else
     {
      result = trade.Sell(lots, _Symbol, bid, sl, tp, InpComment);
      Print("SELL executed. Lots=", lots, " SL=", sl, " TP=", tp,
            " PathLen=", PathLength);
     }

   if(!result)
      Print("Trade failed: ", trade.ResultRetcodeDescription());
  }

//+------------------------------------------------------------------+
//|  Calculate LotSize                                               |
//+------------------------------------------------------------------+
double CalculateLotSize(double slDistance)
  {
   //--- Position sizing: 1–2% risk per trade
   if(slDistance <= 0)
      return 0;

   double balance     = AccountInfoDouble(ACCOUNT_BALANCE);
   double riskAmount  = balance * InpRiskPercent / 100.0;

   double tickSize    = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_SIZE);
   double tickValue   = SymbolInfoDouble(_Symbol, SYMBOL_TRADE_TICK_VALUE);
   double minLot      = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MIN);
   double maxLot      = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_MAX);
   double lotStep     = SymbolInfoDouble(_Symbol, SYMBOL_VOLUME_STEP);

   if(tickSize <= 0 || tickValue <= 0)
      return minLot;

   double slInTicks   = slDistance / tickSize;
   double lotSize     = riskAmount / (slInTicks * tickValue);

   lotSize = MathFloor(lotSize / lotStep) * lotStep;
   lotSize = MathMax(minLot, MathMin(maxLot, lotSize));

   return NormalizeDouble(lotSize, 2);
  }
```

In this code section, we first determine a structurally relevant stop-loss reference using FindOppositeSwingBeforeStart(). This function starts from the selected start node and scans forward through the node list to locate the first swing of the opposite type. If the start node is a swing high, we search for a swing low, and vice versa. This helps us anchor risk around meaningful market structure rather than arbitrary price levels. If no opposite swing is found, the function returns -1, indicating that a fallback risk method must be used later.

We then move into the ExecuteTrade() function, which handles the full trade execution process. Before placing any order, we ensure there is no existing open position for the same EA. We validate that the stop-loss and take-profit levels are logically correct relative to the current market price. Next, we calculate the entry risk distance and pass it into the lot sizing function to determine position size based on account balance and risk percentage. Once validated and normalized, the trade is executed using either a buy or sell order, and the result is logged for confirmation or debugging.

We complete the execution logic with the CalculateLotSize() function, which ensures proper risk-based position sizing. This function converts the stop-loss distance into tick exposure and calculates how much capital is being risked per trade. It then determines the appropriate lot size based on account balance, tick value, and tick size. The result is adjusted to comply with broker constraints such as minimum lot size, maximum lot size, and lot step increments. This ensures every trade respects risk management rules while maintaining consistent exposure across different market conditions.

```
//+------------------------------------------------------------------+
//| New Bar Function                                                 |
//+------------------------------------------------------------------+
bool IsNewBar()
  {
   datetime currentBar = iTime(_Symbol, _Period, 0);
   if(currentBar == LastBarTime)
      return false;
   LastBarTime = currentBar;
   return true;
  }

//+------------------------------------------------------------------+
//|  Clear Objects on the chart                                      |
//+------------------------------------------------------------------+
void ClearVisualization()
  {
   int total = ObjectsTotal(0);
   for(int i = total - 1; i >= 0; i--)
     {
      string name = ObjectName(0, i);
      if(StringFind(name, OBJ_PREFIX) == 0)
         ObjectDelete(0, name);
     }
  }

//+------------------------------------------------------------------+
//|  Get ATR Handle                                                  |
//+------------------------------------------------------------------+
double GetATR()
  {
   int handle = iATR(_Symbol, _Period, InpATRPeriod);
   if(handle == INVALID_HANDLE)
      return 0;

   double buf[1];
   if(CopyBuffer(handle, 0, 0, 1, buf) <= 0)
      return 0;
   IndicatorRelease(handle);
   return buf[0];
  }
```

Here, we handle three utility functions that support the EA’s core A\* engine. The IsNewBar() function ensures that all processing only happens once per new candle by comparing the current bar time with the previously stored value. This prevents redundant calculations and keeps the system efficient. The ClearVisualization() function removes all chart objects created by the EA by scanning through existing objects and deleting those that match the defined prefix, ensuring a clean chart state when the EA is removed or restarted.

We also include GetATR(), which retrieves the Average True Range value for the current symbol and timeframe. This is done by creating an ATR indicator handle, copying the latest buffer value, and then releasing the handle to avoid memory leaks. The ATR value is used throughout the system for normalizing costs, setting buffers, and controlling risk sensitivity. Together, these helper functions ensure the EA runs efficiently, and maintains a clean visual environment.

```
//+------------------------------------------------------------------+
//| VISUALIZATION ENGINE                                             |
//+------------------------------------------------------------------+
void DrawVisualization()
  {
   ClearVisualization();

   if(NodeCount == 0)
      return;

   //--- Draw edges first (behind nodes)
   if(InpDrawEdges)
     {
      for(int e = 0; e < EdgeCount; e++)
        {
         int f = Edges[e].from;
         int t = Edges[e].to;
         if(f < 0 || f >= NodeCount || t < 0 || t >= NodeCount)
            continue;

         string name = OBJ_PREFIX + "EDGE_" + IntegerToString(e);
         ObjectCreate(0, name, OBJ_TREND, 0,
                      Nodes[f].time, Nodes[f].price,
                      Nodes[t].time, Nodes[t].price);
         ObjectSetInteger(0, name, OBJPROP_COLOR,   InpEdgeColor);
         ObjectSetInteger(0, name, OBJPROP_WIDTH,   1);
         ObjectSetInteger(0, name, OBJPROP_STYLE,   STYLE_DOT);
         ObjectSetInteger(0, name, OBJPROP_RAY_RIGHT, false);
         ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
         ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
        }
     }

   //--- Draw best path (thick colored lines)
   if(InpDrawPath && PathLength >= 2)
     {
      for(int p = 0; p < PathLength - 1; p++)
        {
         int a = BestPath[p];
         int b = BestPath[p + 1];
         if(a < 0 || a >= NodeCount || b < 0 || b >= NodeCount)
            continue;

         string name = OBJ_PREFIX + "PATH_" + IntegerToString(p);
         ObjectCreate(0, name, OBJ_TREND, 0,
                      Nodes[a].time, Nodes[a].price,
                      Nodes[b].time, Nodes[b].price);
         ObjectSetInteger(0, name, OBJPROP_COLOR,   InpPathColor);
         ObjectSetInteger(0, name, OBJPROP_WIDTH,   3);
         ObjectSetInteger(0, name, OBJPROP_STYLE,   STYLE_SOLID);
         ObjectSetInteger(0, name, OBJPROP_RAY_RIGHT, false);
         ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
         ObjectSetInteger(0, name, OBJPROP_HIDDEN, true);
        }
     }

   //--- Draw nodes (circles/arrows)
   if(InpDrawNodes)
     {
      for(int i = 0; i < NodeCount; i++)
        {
         string name  = OBJ_PREFIX + "NODE_" + IntegerToString(i);
         color  col   = Nodes[i].isHigh ? InpHighNodeColor : InpLowNodeColor;
         int    arrow = Nodes[i].isHigh ? 217 : 218; // down/up triangle arrows

         ObjectCreate(0, name, OBJ_ARROW, 0, Nodes[i].time, Nodes[i].price);
         ObjectSetInteger(0, name, OBJPROP_ARROWCODE,  arrow);
         ObjectSetInteger(0, name, OBJPROP_COLOR,      col);
         ObjectSetInteger(0, name, OBJPROP_WIDTH,      InpNodeSize);
         ObjectSetInteger(0, name, OBJPROP_SELECTABLE, false);
         ObjectSetInteger(0, name, OBJPROP_HIDDEN,     true);

         //--- Highlight path nodes
         if(InpDrawPath)
           {
            for(int p = 0; p < PathLength; p++)
              {
               if(BestPath[p] == i)
                 {
                  ObjectSetInteger(0, name, OBJPROP_COLOR, InpPathColor);
                  ObjectSetInteger(0, name, OBJPROP_WIDTH, InpNodeSize + 2);
                  break;
                 }
              }
           }
        }
     }

   ChartRedraw();
  }
//+------------------------------------------------------------------+
```

The function implements the visualization engine to graphically represent the A\* system directly on the chart. It begins by clearing all previously drawn objects to ensure the display stays updated and clean. It then checks whether any nodes exist before proceeding. If edge drawing is enabled, we plot all connections between nodes using dotted trend lines, effectively showing the full graph structure that represents market relationships. These edges are drawn first so they appear behind other elements.

We then render the optimal A\* path by connecting consecutive nodes in the best path using thicker, solid lines to highlight the chosen route through the market structure. After that, we draw all swing nodes as arrow markers, with different colors and shapes depending on whether they represent highs or lows. If a node is part of the optimal path, we visually emphasize it by changing its color and increasing its size. This layered visualization allows us to clearly distinguish between raw market structure, the full graph, and the final A\* decision path.

We finish by calling ChartRedraw(), which forces the platform to immediately update the chart so all visual elements appear in real time.

![](https://c.mql5.com/2/206/AStar_Demo.gif)

### Backtest Results

The backtest was conducted on XAUUSD on the H1 timeframe over a two-month window (02 February 2026 to 01 April 2026) with the following settings:

![](https://c.mql5.com/2/206/AStar_INP.png)

The equity curve and backtest results are shown below:

![](https://c.mql5.com/2/206/AStar_CRV.png)

![](https://c.mql5.com/2/206/AStar_BT.png)

### Conclusion

We converted a "noisy" price chart into a formal market map and produced a practical MetaTrader 5 EA framework that replaces subjective judgment with measurable criteria. The pipeline UpdateSwings -> BuildGraph -> RunAStar -> EvaluatePath -> ExecuteTrade is the operational artifact: it (1) extracts validated swing nodes (removing levels already breached), (2) builds weighted edges using ATR‑normalized distance, spread cost, and a noise penalty, (3) finds the most efficient route with A\*, and (4) filters and converts that route into a trade only when formal metrics are satisfied—directional ratio (up/down move share), total path cost (g), and absence of opposing swing obstacles. Executions set TP at the final node, SL at the nearest opposite structure (with ATR buffer), or use a volatility fallback, and size positions by percentage risk.

Practically, you obtain a transparent EA that draws nodes/edges/path on the chart and only takes trades meeting explicit, configurable thresholds (swing lookback, ATR period, spread/noise penalties, min path score, max path cost, risk%). This makes results reproducible and straightforward to backtest: success is verifiable by the presence of visual objects (nodes/edges/path), by trades that obey the stated decision rules, and by the ability to tune parameters to improve P&L under the same formal criteria.

**Attached files** |

[Download ZIP](https://www.mql5.com/en/articles/download/22184.zip "Download all attachments in the single ZIP archive")

[Heuristic\_A\_Star.mq5](https://www.mql5.com/en/articles/download/22184/Heuristic_A_Star.mq5 "Download Heuristic_A_Star.mq5") (29.18 KB)

#### Other articles by this author

- [Automating Market Entropy Indicator: Trading System Based on Information Theory](https://www.mql5.com/en/articles/21742)
- [Formulating Dynamic Multi-Pair EA (Part 8): Time-of-Day Capital Rotation Approach](https://www.mql5.com/en/articles/21976)
- [Swing Extremes and Pullbacks in MQL5 (Part 3): Defining Structural Validity Beyond Simple Highs/Lows](https://www.mql5.com/en/articles/21888)
- [Developing Market Entropy Indicator: Trading System Based on Information Theory](https://www.mql5.com/en/articles/21743)
- [Integrating MQL5 with Data Processing Packages (Part 8): Using Graph Neural Networks for Liquidity Zone Recognition](https://www.mql5.com/en/articles/21676)
- [Graph Theory: Traversal Depth-First Search (DFS) Applied in Trading](https://www.mql5.com/en/articles/21590)

[How to implement AutoARIMA forecasting in MQL5](https://www.mql5.com/en/articles/22224)

This article presents an MQL5 implementation of AutoARIMA that builds ARIMA models without manual tuning. It estimates d via a variance-based heuristic, fits ARMA(p,q) by gradient optimization with Adam, and selects p and q using AICc. The code returns a one-step-ahead price forecast by differencing, model estimation, and integration back to price level, ready to call on a Close series.

[MQL5 Wizard Techniques you should know (Part 88): Using Blooms Filter with a Custom Trailing Class](https://www.mql5.com/en/articles/22389)

Our next focus in these series on ideas that can be rapidly prototyped with the MQL5 Wizard, is a Custom Trailing class that uses the Blooming Filter. Trailing Stop systems are an optional but very resourceful part to any trading system that we want to explore more in these series besides the traditional Entry Signals.

[Building an Object-Oriented FVG Scanner in MQL5](https://www.mql5.com/en/articles/22264)

Create an object-oriented fair value gap (FVG) scanner in MQL5 and display liquidity gaps directly on a MetaTrader 5 chart, this article formalizes the imbalance geometry based on three candlesticks, synchronizes OHLC arrays with CopyRates, manages rectangles without leaks, and monitors mitigation in real time. It also shows how to integrate this class into an Expert Advisor with a strict new bar filter for stable and efficient execution.

[Price Action Analysis Toolkit Development (Part 68): Price-Attached RSI Panel in MQL5](https://www.mql5.com/en/articles/22110)

We present a chart-embedded RSI panel that removes the need for a separate window by attaching momentum directly to live price. The article explains the design and MQL5 code: real-time RSI retrieval, slope-based signal classification, and adaptive positioning. Traders get RSI value, state, and signal strength where decisions are made, improving clarity across timeframes.

<iframe width="800" height="80" frameborder="0" src="https://www.mql5.com/ff/sh/0hvxp984jjj79943z2/index.html?link=https%3A%2F%2Ftrade.metatrader5.com%2F&amp;a=uyigsjnbfcdvysiynusmriwvhincciwd&amp;s=c95531ae2fd8a81b0fac3def2e4cf820a67584bbf4b02f76ec75f808942dbbd2&amp;v=1&amp;w=800&amp;h=80&amp;r=https%3A%2F%2Fwww.mql5.com%2Fen%2Farticles%2F22184&amp;host=https%3A%2F%2Fwww.mql5.com%2Fff%2F&amp;id=wdausxxqrpvhekbwjrjlhqjghyhesrqqau&amp;fz_uniq=5050341010206998204&amp;custom="></iframe>