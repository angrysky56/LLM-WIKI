---
title: "tlaplus/Examples: A collection of TLA⁺ specifications of varying complexities."
source: "https://github.com/tlaplus/Examples"
author:
published:
created: 2026-04-17
description: "A collection of TLA⁺ specifications of varying complexities. - tlaplus/Examples"
tags:
  - "clippings"
---
## TLA+ Examples

This is a repository of TLA <sup>+</sup> specifications and models covering applications in a variety of fields. It serves as:

- a comprehensive example library demonstrating how to specify an algorithm in TLA <sup>+</sup>
- a diverse corpus facilitating development & testing of TLA <sup>+</sup> language tools
- a collection of case studies in the application of formal specification in TLA <sup>+</sup>

All TLA <sup>+</sup> specs can be found in the [`specifications`](https://github.com/tlaplus/Examples/blob/master/specifications) directory. To contribute a spec of your own, see [`CONTRIBUTING.md`](https://github.com/tlaplus/Examples/blob/master/CONTRIBUTING.md).

The table below lists all specs and indicates whether a spec is beginner-friendly, includes an additional PlusCal variant `(✔)`, or uses PlusCal exclusively. Additionally, the table specifies which verification tool— [TLC](https://github.com/tlaplus/tlaplus), [Apalache](https://github.com/apalache-mc/apalache), or [TLAPS](https://github.com/tlaplus/tlapm) —can be used to verify each specification.

Space contraints limit the information displayed in the table; detailed spec metadata can be found in the `manifest.json` files in each specification's directory. You can search these files for examples exhibiting a number of features, either using the GitHub repository search or locally with the command `ls specifications/*/manifest.json | xargs grep -l $keyword`, where `$keyword` can be a value like:

- `pluscal`, `proof`, or `action composition` (the `\cdot` operator)
- Specs intended for trace generation (`generate`), `simulate`, or checked symbolically with Apalache (`symbolic`)
- Models failing in interesting ways, like `deadlock failure`, `safety failure`, `liveness failure`, or `assumption failure`

It is also helpful to consult model files using specific TLC features. For this, run `ls specifications/*/*.cfg | xargs grep -l $keyword`, where `$keyword` can be a feature like `SYMMETRY`, `VIEW`, `ALIAS`, `CONSTRAINT`, or `DEADLOCK`.

## Validated Examples Included Here

Here is a list of specs included in this repository which are validated by the CI, with links to the relevant directory and flags for various features:

| Name | Author(s) | Beginner | TLAPS Proof | PlusCal | TLC Model | Apalache |
| --- | --- | --- | --- | --- | --- | --- |
| [Teaching Concurrency](https://github.com/tlaplus/Examples/blob/master/specifications/TeachingConcurrency) | Leslie Lamport | ✔ | ✔ | ✔ | ✔ |  |
| [Loop Invariance](https://github.com/tlaplus/Examples/blob/master/specifications/LoopInvariance) | Leslie Lamport | ✔ | ✔ | ✔ | ✔ |  |
| [Learn TLA⁺ Proofs](https://github.com/tlaplus/Examples/blob/master/specifications/LearnProofs) | Andrew Helwer | ✔ | ✔ | ✔ | ✔ |  |
| [Boyer-Moore Majority Vote](https://github.com/tlaplus/Examples/blob/master/specifications/Majority) | Stephan Merz | ✔ | ✔ |  | ✔ |  |
| [Proof x+x is Even](https://github.com/tlaplus/Examples/blob/master/specifications/sums_even) | Martin Riener | ✔ | ✔ |  | ✔ |  |
| [The N-Queens Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/N-Queens) | Stephan Merz | ✔ |  | ✔ | ✔ |  |
| [The Dining Philosophers Problem](https://github.com/tlaplus/Examples/blob/master/specifications/DiningPhilosophers) | Jeff Hemphill | ✔ |  | ✔ | ✔ |  |
| [The Car Talk Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/CarTalkPuzzle) | Leslie Lamport | ✔ |  |  | ✔ |  |
| [The Die Hard Problem](https://github.com/tlaplus/Examples/blob/master/specifications/DieHard) | Leslie Lamport | ✔ |  |  | ✔ |  |
| [The Prisoners & Switches Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/Prisoners) | Leslie Lamport | ✔ |  |  | ✔ |  |
| [The Prisoners & Switch Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/Prisoners_Single_Switch) | Florian Schanda | ✔ |  |  | ✔ |  |
| [Specs from Specifying Systems](https://github.com/tlaplus/Examples/blob/master/specifications/SpecifyingSystems) | Leslie Lamport | ✔ |  |  | ✔ |  |
| [The Tower of Hanoi Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/tower_of_hanoi) | Markus Kuppe, Alexander Niederbühl | ✔ |  |  | ✔ |  |
| [Missionaries and Cannibals](https://github.com/tlaplus/Examples/blob/master/specifications/MissionariesAndCannibals) | Leslie Lamport | ✔ |  |  | ✔ |  |
| [Stone Scale Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/Stones) | Leslie Lamport | ✔ |  |  | ✔ |  |
| [The Coffee Can Bean Problem](https://github.com/tlaplus/Examples/blob/master/specifications/CoffeeCan) | Andrew Helwer | ✔ |  |  | ✔ |  |
| [EWD687a: Detecting Termination in Distributed Computations](https://github.com/tlaplus/Examples/blob/master/specifications/ewd687a) | Stephan Merz, Leslie Lamport, Markus Kuppe | ✔ |  | (✔) | ✔ |  |
| [The Moving Cat Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/Moving_Cat_Puzzle) | Florian Schanda | ✔ |  |  | ✔ |  |
| [The Boulangerie Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/Bakery-Boulangerie) | Leslie Lamport, Stephan Merz |  | ✔ | ✔ | ✔ |  |
| [Misra Reachability Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/MisraReachability) | Leslie Lamport |  | ✔ | ✔ | ✔ |  |
| [Byzantizing Paxos by Refinement](https://github.com/tlaplus/Examples/blob/master/specifications/byzpaxos) | Leslie Lamport |  | ✔ | ✔ | ✔ |  |
| [Barrier Synchronization](https://github.com/tlaplus/Examples/blob/master/specifications/barriers) | Jarod Differdange |  | ✔ | ✔ | ✔ |  |
| [Peterson Lock Refinement With Auxiliary Variables](https://github.com/tlaplus/Examples/blob/master/specifications/locks_auxiliary_vars) | Jarod Differdange |  | ✔ | ✔ | ✔ |  |
| [EWD840: Termination Detection in a Ring](https://github.com/tlaplus/Examples/blob/master/specifications/ewd840) | Stephan Merz |  | ✔ |  | ✔ |  |
| [EWD998: Termination Detection in a Ring with Asynchronous Message Delivery](https://github.com/tlaplus/Examples/blob/master/specifications/ewd998) | Stephan Merz, Markus Kuppe |  | ✔ | (✔) | ✔ |  |
| [The Paxos Protocol](https://github.com/tlaplus/Examples/blob/master/specifications/Paxos) | Leslie Lamport |  | (✔) |  | ✔ |  |
| [Asynchronous Reliable Broadcast](https://github.com/tlaplus/Examples/blob/master/specifications/bcastByz) | Thanh Hai Tran, Igor Konnov, Josef Widder |  | ✔ |  | ✔ |  |
| [Distributed Mutual Exclusion](https://github.com/tlaplus/Examples/blob/master/specifications/lamport_mutex) | Stephan Merz |  | ✔ |  | ✔ |  |
| [Two-Phase Handshaking](https://github.com/tlaplus/Examples/blob/master/specifications/TwoPhase) | Leslie Lamport, Stephan Merz |  | ✔ |  | ✔ |  |
| [Paxos (How to Win a Turing Award)](https://github.com/tlaplus/Examples/blob/master/specifications/PaxosHowToWinATuringAward) | Leslie Lamport |  | (✔) |  | ✔ |  |
| [Finitizing Monotonic Systems](https://github.com/tlaplus/Examples/blob/master/specifications/FiniteMonotonic) | Andrew Helwer, Stephan Merz, Markus Kuppe |  | ✔ |  | ✔ |  |
| [Dijkstra's Mutual Exclusion Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/dijkstra-mutex) | Leslie Lamport |  |  | ✔ | ✔ |  |
| [The Echo Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/echo) | Stephan Merz |  |  | ✔ | ✔ |  |
| [The TLC Safety Checking Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/TLC) | Markus Kuppe |  |  | ✔ | ✔ |  |
| [Transaction Commit Models](https://github.com/tlaplus/Examples/blob/master/specifications/transaction_commit) | Leslie Lamport, Jim Gray, Murat Demirbas |  |  | ✔ | ✔ |  |
| [The Slush Protocol](https://github.com/tlaplus/Examples/blob/master/specifications/SlushProtocol) | Andrew Helwer |  |  | ✔ | ✔ |  |
| [Minimal Circular Substring](https://github.com/tlaplus/Examples/blob/master/specifications/LeastCircularSubstring) | Andrew Helwer |  |  | ✔ | ✔ |  |
| [Snapshot Key-Value Store](https://github.com/tlaplus/Examples/blob/master/specifications/KeyValueStore) | Andrew Helwer, Murat Demirbas |  |  | ✔ | ✔ |  |
| [Chang-Roberts Algorithm for Leader Election in a Ring](https://github.com/tlaplus/Examples/blob/master/specifications/chang_roberts) | Stephan Merz |  |  | ✔ | ✔ |  |
| [MultiPaxos in SMR-Style](https://github.com/tlaplus/Examples/blob/master/specifications/MultiPaxos-SMR) | Guanzhou Hu |  |  | ✔ | ✔ |  |
| [Einstein's Riddle](https://github.com/tlaplus/Examples/blob/master/specifications/EinsteinRiddle) | Isaac DeFrain, Giuliano Losa |  |  |  |  | ✔ |
| [Resource Allocator](https://github.com/tlaplus/Examples/blob/master/specifications/allocator) | Stephan Merz |  |  |  | ✔ |  |
| [Transitive Closure](https://github.com/tlaplus/Examples/blob/master/specifications/TransitiveClosure) | Stephan Merz |  |  |  | ✔ |  |
| [Atomic Commitment Protocol](https://github.com/tlaplus/Examples/blob/master/specifications/acp) | Stephan Merz |  |  |  | ✔ |  |
| [SWMR Shared Memory Disk Paxos](https://github.com/tlaplus/Examples/blob/master/specifications/diskpaxos) | Leslie Lamport, Giuliano Losa |  |  |  | ✔ |  |
| [Span Tree Exercise](https://github.com/tlaplus/Examples/blob/master/specifications/SpanningTree) | Leslie Lamport |  |  |  | ✔ |  |
| [The Knuth-Yao Method](https://github.com/tlaplus/Examples/blob/master/specifications/KnuthYao) | Ron Pressler, Markus Kuppe |  |  |  | ✔ |  |
| [Huang's Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/Huang) | Markus Kuppe |  |  |  | ✔ |  |
| [EWD 426: Token Stabilization](https://github.com/tlaplus/Examples/blob/master/specifications/ewd426) | Murat Demirbas, Markus Kuppe |  |  |  | ✔ |  |
| [Sliding Block Puzzle](https://github.com/tlaplus/Examples/blob/master/specifications/SlidingPuzzles) | Mariusz Ryndzionek |  |  |  | ✔ |  |
| [Single-Lane Bridge Problem](https://github.com/tlaplus/Examples/blob/master/specifications/SingleLaneBridge) | Younes Akhouayri |  |  |  | ✔ |  |
| [Software-Defined Perimeter](https://github.com/tlaplus/Examples/blob/master/specifications/SDP_Verification) | Luming Dong, Zhi Niu |  |  |  | ✔ |  |
| [Simplified Fast Paxos](https://github.com/tlaplus/Examples/blob/master/specifications/SimplifiedFastPaxos) | Lim Ngian Xin Terry, Gaurav Gandhi |  |  |  | ✔ |  |
| [Checkpoint Coordination](https://github.com/tlaplus/Examples/blob/master/specifications/CheckpointCoordination) | Andrew Helwer |  |  |  | ✔ |  |
| [Multi-Car Elevator System](https://github.com/tlaplus/Examples/blob/master/specifications/MultiCarElevator) | Andrew Helwer |  |  |  | ✔ |  |
| [Nano Blockchain Protocol](https://github.com/tlaplus/Examples/blob/master/specifications/NanoBlockchain) | Andrew Helwer |  |  |  | ✔ |  |
| [The Readers-Writers Problem](https://github.com/tlaplus/Examples/blob/master/specifications/ReadersWriters) | Isaac DeFrain |  |  |  | ✔ |  |
| [Asynchronous Byzantine Consensus](https://github.com/tlaplus/Examples/blob/master/specifications/aba-asyn-byz) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [Folklore Reliable Broadcast](https://github.com/tlaplus/Examples/blob/master/specifications/bcastFolklore) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [The Bosco Byzantine Consensus Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/bosco) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [Consensus in One Communication Step](https://github.com/tlaplus/Examples/blob/master/specifications/c1cs) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [One-Step Consensus with Zero-Degradation](https://github.com/tlaplus/Examples/blob/master/specifications/cf1s-folklore) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [Failure Detector](https://github.com/tlaplus/Examples/blob/master/specifications/detector_chan96) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [Asynchronous Non-Blocking Atomic Commit](https://github.com/tlaplus/Examples/blob/master/specifications/nbacc_ray97) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [Asynchronous Non-Blocking Atomic Commitment with Failure Detectors](https://github.com/tlaplus/Examples/blob/master/specifications/nbacg_guer01) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [Spanning Tree Broadcast Algorithm](https://github.com/tlaplus/Examples/blob/master/specifications/spanning) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  | ✔ |  |
| [The Cigarette Smokers Problem](https://github.com/tlaplus/Examples/blob/master/specifications/CigaretteSmokers) | Mariusz Ryndzionek |  |  |  | ✔ |  |
| [Conway's Game of Life](https://github.com/tlaplus/Examples/blob/master/specifications/GameOfLife) | Mariusz Ryndzionek |  |  |  | ✔ |  |
| [Chameneos, a Concurrency Game](https://github.com/tlaplus/Examples/blob/master/specifications/Chameneos) | Mariusz Ryndzionek |  |  |  | ✔ |  |
| [PCR Testing for Snippets of DNA](https://github.com/tlaplus/Examples/blob/master/specifications/glowingRaccoon) | Martin Harrison |  |  |  | ✔ |  |
| [RFC 3506: Voucher Transaction System](https://github.com/tlaplus/Examples/blob/master/specifications/byihive) | Santhosh Raju, Cherry G. Mathew, Fransisca Andriani |  |  |  | ✔ |  |
| [Yo-Yo Leader Election](https://github.com/tlaplus/Examples/blob/master/specifications/YoYo) | Ludovic Yvoz, Stephan Merz |  |  |  | ✔ |  |
| [TCP as defined in RFC 9293](https://github.com/tlaplus/Examples/blob/master/specifications/tcp) | Markus Kuppe |  |  |  | ✔ |  |
| [B-trees](https://github.com/tlaplus/Examples/blob/master/specifications/btree) | Lorin Hochstein |  |  |  | ✔ |  |
| [TLA⁺ Level Checking](https://github.com/tlaplus/Examples/blob/master/specifications/LevelChecking) | Leslie Lamport |  |  |  |  |  |
| [Condition-Based Consensus](https://github.com/tlaplus/Examples/blob/master/specifications/cbc_max) | Thanh Hai Tran, Igor Konnov, Josef Widder |  |  |  |  |  |
| [Buffered Random Access File](https://github.com/tlaplus/Examples/blob/master/specifications/braf) | Calvin Loncaric |  |  |  | ✔ |  |
| [Disruptor](https://github.com/tlaplus/Examples/blob/master/specifications/Disruptor) | Nicholas Schultz-Møller |  |  |  | ✔ |  |
| [DAG-based Consensus](https://github.com/tlaplus/Examples/blob/master/specifications/dag-consensus) | Giuliano Losa |  |  | ✔ | ✔ |  |

## Other Examples

Here is a list of specs stored in locations outside this repository or not validated by the CI, such as submodules. Since these specs are not covered by CI testing it is possible they contain errors, the reported details are incorrect, or they are no longer available. Ideally these will be moved into this repo over time.

| Spec | Details | Author(s) | Beginner | TLAPS Proof | TLC Model | PlusCal | Apalache |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Blocking Queue](https://github.com/lemmy/BlockingQueue) | BlockingQueue | Markus Kuppe | ✔ | ✔ | ✔ | (✔) |  |
| IEEE 802.16 WiMAX Protocols | 2006, [paper](https://users.cs.northwestern.edu/~ychen/Papers/npsec06.pdf), [specs](http://list.cs.northwestern.edu/802.16/) | Prasad Narayana, Ruiming Chen, Yao Zhao, Yan Chen, Zhi (Judy) Fu, Hai Zhou |  |  |  |  |  |
| On the diversity of asynchronous communication | 2016, [paper](https://dl.acm.org/doi/10.1007/s00165-016-0379-x), [specs](http://hurault.perso.enseeiht.fr/asynchronousCommunication/) | Florent Chevrou, Aurélie Hurault, Philippe Quéinnec |  |  |  |  |  |
| [Caesar](https://github.com/tlaplus/Examples/blob/master/specifications/Caesar) | Multi-leader generalized consensus protocol (Arun et al., 2017) | Giuliano Losa |  |  | ✔ | ✔ |  |
| [CASPaxos](https://github.com/tlaplus/Examples/blob/master/specifications/CASPaxos) | An extension of the single-decree Paxos algorithm to a compare-and-swap type register (Rystsov) | Tobias Schottdorf |  |  | ✔ |  |  |
| [DataPort](https://github.com/tlaplus/Examples/blob/master/specifications/DataPort) | Dataport protocal 505.89PT, only PDF files (Biggs & Noriaki, 2016) | Geoffrey Biggs, Noriaki Ando |  |  |  |  |  |
| [egalitarian-paxos](https://github.com/tlaplus/Examples/blob/master/specifications/egalitarian-paxos) | Leaderless replication protocol based on Paxos (Moraru et al., 2013) | Iulian Moraru |  |  | ✔ |  |  |
| [fastpaxos](https://github.com/tlaplus/Examples/blob/master/specifications/fastpaxos) | An extension of the classic Paxos algorithm, only PDF files (Lamport, 2006) | Leslie Lamport |  |  |  |  |  |
| [fpaxos](https://github.com/tlaplus/Examples/blob/master/specifications/fpaxos) | A variant of Paxos with flexible quorums (Howard et al., 2017) | Heidi Howard |  |  | ✔ |  |  |
| [HLC](https://github.com/tlaplus/Examples/blob/master/specifications/HLC) | Hybrid logical clocks and hybrid vector clocks (Demirbas et al., 2014) | Murat Demirbas |  |  | ✔ | ✔ |  |
| [L1](https://github.com/tlaplus/Examples/blob/master/specifications/L1) | Data center network L1 switch protocol, only PDF files (Thacker) | Tom Rodeheffer |  |  |  |  |  |
| [leaderless](https://github.com/tlaplus/Examples/blob/master/specifications/leaderless) | Leaderless generalized-consensus algorithms (Losa, 2016) | Giuliano Losa |  |  | ✔ | ✔ |  |
| [losa\_ap](https://github.com/tlaplus/Examples/blob/master/specifications/losa_ap) | The assignment problem, a variant of the allocation problem (Delporte-Gallet, 2018) | Giuliano Losa |  |  | ✔ | ✔ |  |
| [losa\_rda](https://github.com/tlaplus/Examples/blob/master/specifications/losa_rda) | Applying peculative linearizability to fault-tolerant message-passing algorithms and shared-memory consensus, only PDF files (Losa, 2014) | Giuliano Losa |  |  |  |  |  |
| [m2paxos](https://github.com/tlaplus/Examples/blob/master/specifications/m2paxos) | Multi-leader consensus protocols (Peluso et al., 2016) | Giuliano Losa |  |  | ✔ |  |  |
| [mongo-repl-tla](https://github.com/tlaplus/Examples/blob/master/specifications/mongo-repl-tla) | A simplified part of Raft in MongoDB (Ongaro, 2014) | Siyuan Zhou |  |  | ✔ |  |  |
| [MultiPaxos](https://github.com/tlaplus/Examples/blob/master/specifications/MultiPaxos) | The abstract specification of Generalized Paxos (Lamport, 2004) | Giuliano Losa |  |  | ✔ |  |  |
| [naiad](https://github.com/tlaplus/Examples/blob/master/specifications/naiad) | Naiad clock protocol, only PDF files (Murray et al., 2013) | Tom Rodeheffer |  |  | ✔ |  |  |
| [nfc04](https://github.com/tlaplus/Examples/blob/master/specifications/nfc04) | Non-functional properties of component-based software systems (Zschaler, 2010) | Steffen Zschaler |  |  | ✔ |  |  |
| [raft](https://github.com/tlaplus/Examples/blob/master/specifications/raft) | Raft consensus algorithm (Ongaro, 2014) | Diego Ongaro |  |  | ✔ |  |  |
| [SnapshotIsolation](https://github.com/tlaplus/Examples/blob/master/specifications/SnapshotIsolation) | Serializable snapshot isolation (Cahill et al., 2010) | Michael J. Cahill, Uwe Röhm, Alan D. Fekete |  |  | ✔ |  |  |
| [SyncConsensus](https://github.com/tlaplus/Examples/blob/master/specifications/SyncConsensus) | Synchronized round consensus algorithm (Demirbas) | Murat Demirbas |  |  | ✔ | ✔ |  |
| [Termination](https://github.com/tlaplus/Examples/blob/master/specifications/Termination) | Channel-counting algorithm (Kumar, 1985) | Giuliano Losa |  | ✔ | ✔ | ✔ | ✔ |
| [Tla-tortoise-hare](https://github.com/tlaplus/Examples/blob/master/specifications/Tla-tortoise-hare) | Robert Floyd's cycle detection algorithm | Lorin Hochstein |  |  | ✔ | ✔ |  |
| [VoldemortKV](https://github.com/tlaplus/Examples/blob/master/specifications/VoldemortKV) | Voldemort distributed key value store | Murat Demirbas |  |  | ✔ | ✔ |  |
| [Tencent-Paxos](https://github.com/tlaplus/Examples/blob/master/specifications/TencentPaxos) | PaxosStore: high-availability storage made practical in WeChat. Proceedings of the VLDB Endowment(Zheng et al., 2017) | Xingchen Yi, Hengfeng Wei |  | ✔ | ✔ |  |  |
| [Paxos](https://github.com/neoschizomer/Paxos) | Paxos |  |  |  | ✔ |  |  |
| [Lock-Free Set](https://github.com/tlaplus/tlaplus/blob/master/tlatools/org.lamport.tlatools/src/tlc2/tool/fp/OpenAddressing.tla) | PlusCal spec of a lock-Free set used by TLC | Markus Kuppe |  |  | ✔ | ✔ |  |
| [ParallelRaft](https://github.com/tlaplus/Examples/blob/master/specifications/ParalleRaft) | A variant of Raft | Xiaosong Gu, Hengfeng Wei, Yu Huang |  |  | ✔ |  |  |
| [CRDT-Bug](https://github.com/Alexander-N/tla-specs/tree/main/crdt-bug) | CRDT algorithm with defect and fixed version | Alexander Niederbühl |  |  | ✔ |  |  |
| [asyncio-lock](https://github.com/Alexander-N/tla-specs/tree/main/asyncio-lock) | Bugs from old versions of Python's asyncio lock | Alexander Niederbühl |  |  | ✔ |  |  |
| [Raft (with cluster changes)](https://github.com/dranov/raft-tla) | Raft with cluster changes, and a version with Apalache type annotations but no cluster changes | George Pîrlea, Darius Foom, Brandon Amos, Huanchen Zhang, Daniel Ricketts |  |  | ✔ |  | ✔ |
| [MET for CRDT-Redis](https://github.com/elem-azar-unis/CRDT-Redis/tree/master/MET/TLA) | Model-check the CRDT designs, then generate test cases to test CRDT implementations | Yuqi Zhang |  |  | ✔ | ✔ |  |
| [Parallel increment](https://github.com/Cjen1/tla_increment) | Parallel threads incrementing a shared variable. Demonstrates invariants, liveness, fairness and symmetry | Chris Jensen |  |  | ✔ |  |  |
| [The Streamlet consensus algorithm](https://github.com/nano-o/streamlet) | Specification and model-checking of both safety and liveness properties of Streamlet with TLC | Giuliano Losa |  |  | ✔ | ✔ |  |
| [Petri Nets](https://github.com/elh/petri-tlaplus) | Instantiable Petri Nets with liveness properties | Eugene Huang |  |  | ✔ |  |  |
| [CRDT](https://github.com/JYwellin/CRDT-TLA) | Specifying and Verifying CRDT Protocols | Ye Ji, Hengfeng Wei |  |  | ✔ |  |  |
| [Azure Cosmos DB](https://github.com/tlaplus/azure-cosmos-tla) | Consistency models provided by Azure Cosmos DB | Dharma Shukla, Ailidani Ailijiang, Murat Demirbas, Markus Kuppe |  |  | ✔ | ✔ |  |
| [Simple Microwave Oven](https://github.com/lucformalmethodscourse/microwave-tla) | Spec of a microwave oven | Konstantin Läufer, George K. Thiruvathukal | ✔ |  |  | ✔ |  |

## Contributing a Spec

See [`CONTRIBUTING.md`](https://github.com/tlaplus/Examples/blob/master/CONTRIBUTING.md) for instructions.

## License

The repository is under the MIT license and you are encouraged to publish your spec under a similarly-permissive license. However, your spec can be included in this repo along with your own license if you wish.