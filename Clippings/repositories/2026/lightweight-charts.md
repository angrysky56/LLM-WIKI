---
title: "lightweight-charts"
source: "https://pypi.org/project/lightweight-charts/"
author:
published: 2024-09-28
created: 2026-04-21
description: "Python framework for TradingView's Lightweight Charts JavaScript library."
tags:
  - "clippings"
---
## lightweight-charts-python

![cover](https://pypi-camo.freetls.fastly.net/cc14da137450a3497f64aece377d685c539259b4/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6c6f7569736e7730312f6c696768747765696768742d6368617274732d707974686f6e2f6d61696e2f636f7665722e706e67)

lightweight-charts-python aims to provide a simple and pythonic way to access and implement [TradingView's Lightweight Charts](https://www.tradingview.com/lightweight-charts/).

## Installation

```
pip install lightweight-charts
```

---

## Features

1. Streamlined for live data, with methods for updating directly from tick data.
2. Multi-pane charts using [Subcharts](https://lightweight-charts-python.readthedocs.io/en/latest/reference/abstract_chart.html#AbstractChart.create_subchart).
3. The [Toolbox](https://lightweight-charts-python.readthedocs.io/en/latest/reference/toolbox.html), allowing for trendlines, rectangles, rays and horizontal lines to be drawn directly onto charts.
4. [Events](https://lightweight-charts-python.readthedocs.io/en/latest/tutorials/events.html) allowing for timeframe selectors (1min, 5min, 30min etc.), searching, hotkeys, and more.
5. [Tables](https://lightweight-charts-python.readthedocs.io/en/latest/reference/tables.html) for watchlists, order entry, and trade management.
6. Direct integration of market data through [Polygon.io's](https://polygon.io/?utm_source=affiliate&utm_campaign=pythonlwcharts) market data API.

**Supports:** Jupyter Notebooks, PyQt6, PyQt5, PySide6, wxPython, Streamlit, and asyncio.

PartTimeLarry: [Interactive Brokers API and TradingView Charts in Python](https://www.youtube.com/watch?v=TlhDI3PforA)

---

### 1\. Display data from a csv:

```
import pandas as pd
from lightweight_charts import Chart

if __name__ == '__main__':
    
    chart = Chart()
    
    # Columns: time | open | high | low | close | volume 
    df = pd.read_csv('ohlcv.csv')
    chart.set(df)
    
    chart.show(block=True)
```

![setting_data image](https://pypi-camo.freetls.fastly.net/7b80740251bba88eb409557c74ba56227c7aac4c/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6c6f7569736e7730312f6c696768747765696768742d6368617274732d707974686f6e2f6d61696e2f6578616d706c65732f315f73657474696e675f646174612f73657474696e675f646174612e706e67)

---

### 2\. Updating bars in real-time:

```
import pandas as pd
from time import sleep
from lightweight_charts import Chart

if __name__ == '__main__':

    chart = Chart()

    df1 = pd.read_csv('ohlcv.csv')
    df2 = pd.read_csv('next_ohlcv.csv')

    chart.set(df1)

    chart.show()

    last_close = df1.iloc[-1]['close']
    
    for i, series in df2.iterrows():
        chart.update(series)

        if series['close'] > 20 and last_close < 20:
            chart.marker(text='The price crossed $20!')
            
        last_close = series['close']
        sleep(0.1)
```

![live data gif](https://pypi-camo.freetls.fastly.net/867a54e75710791f10cf49b2ca81c2926e12a8d4/68747470733a2f2f6769746875622e636f6d2f6c6f7569736e7730312f6c696768747765696768742d6368617274732d707974686f6e2f626c6f622f6d61696e2f6578616d706c65732f325f6c6976655f646174612f6c6976655f646174612e6769663f7261773d74727565)

---

### 3\. Updating bars from tick data in real-time:

```
import pandas as pd
from time import sleep
from lightweight_charts import Chart

if __name__ == '__main__':
    
    df1 = pd.read_csv('ohlc.csv')
    
    # Columns: time | price 
    df2 = pd.read_csv('ticks.csv')
    
    chart = Chart()
    
    chart.set(df1)
    
    chart.show()
    
    for i, tick in df2.iterrows():
        chart.update_from_tick(tick)
            
        sleep(0.03)
```

![tick data gif](https://pypi-camo.freetls.fastly.net/1969f18a81c1cb35b433f9d19a1b52051d942517/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6c6f7569736e7730312f6c696768747765696768742d6368617274732d707974686f6e2f6d61696e2f6578616d706c65732f335f7469636b5f646174612f7469636b5f646174612e676966)

---

### 4\. Line Indicators:

```
import pandas as pd
from lightweight_charts import Chart

def calculate_sma(df, period: int = 50):
    return pd.DataFrame({
        'time': df['date'],
        f'SMA {period}': df['close'].rolling(window=period).mean()
    }).dropna()

if __name__ == '__main__':
    chart = Chart()
    chart.legend(visible=True)

    df = pd.read_csv('ohlcv.csv')
    chart.set(df)

    line = chart.create_line('SMA 50')
    sma_data = calculate_sma(df, period=50)
    line.set(sma_data)

    chart.show(block=True)
```

![line indicators image](https://pypi-camo.freetls.fastly.net/5332cd8d1d6ade310112f1ffac38d51acc993ba0/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6c6f7569736e7730312f6c696768747765696768742d6368617274732d707974686f6e2f6d61696e2f6578616d706c65732f345f6c696e655f696e64696361746f72732f6c696e655f696e64696361746f72732e706e67)

---

### 5\. Styling:

```
import pandas as pd
from lightweight_charts import Chart

if __name__ == '__main__':
    
    chart = Chart()

    df = pd.read_csv('ohlcv.csv')

    chart.layout(background_color='#090008', text_color='#FFFFFF', font_size=16,
                 font_family='Helvetica')

    chart.candle_style(up_color='#00ff55', down_color='#ed4807',
                       border_up_color='#FFFFFF', border_down_color='#FFFFFF',
                       wick_up_color='#FFFFFF', wick_down_color='#FFFFFF')

    chart.volume_config(up_color='#00ff55', down_color='#ed4807')

    chart.watermark('1D', color='rgba(180, 180, 240, 0.7)')

    chart.crosshair(mode='normal', vert_color='#FFFFFF', vert_style='dotted',
                    horz_color='#FFFFFF', horz_style='dotted')

    chart.legend(visible=True, font_size=14)

    chart.set(df)

    chart.show(block=True)
```

![styling image](https://pypi-camo.freetls.fastly.net/894c5f9209c8659e6fa74951f6e3dda8f1f1b61c/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6c6f7569736e7730312f6c696768747765696768742d6368617274732d707974686f6e2f6d61696e2f6578616d706c65732f355f7374796c696e672f7374796c696e672e706e67)

---

### 6\. Callbacks:

```
import pandas as pd
from lightweight_charts import Chart

def get_bar_data(symbol, timeframe):
    if symbol not in ('AAPL', 'GOOGL', 'TSLA'):
        print(f'No data for "{symbol}"')
        return pd.DataFrame()
    return pd.read_csv(f'bar_data/{symbol}_{timeframe}.csv')

def on_search(chart, searched_string):  # Called when the user searches.
    new_data = get_bar_data(searched_string, chart.topbar['timeframe'].value)
    if new_data.empty:
        return
    chart.topbar['symbol'].set(searched_string)
    chart.set(new_data)

def on_timeframe_selection(chart):  # Called when the user changes the timeframe.
    new_data = get_bar_data(chart.topbar['symbol'].value, chart.topbar['timeframe'].value)
    if new_data.empty:
        return
    chart.set(new_data, True)

def on_horizontal_line_move(chart, line):
    print(f'Horizontal line moved to: {line.price}')

if __name__ == '__main__':
    chart = Chart(toolbox=True)
    chart.legend(True)

    chart.events.search += on_search

    chart.topbar.textbox('symbol', 'TSLA')
    chart.topbar.switcher('timeframe', ('1min', '5min', '30min'), default='5min',
                          func=on_timeframe_selection)

    df = get_bar_data('TSLA', '5min')
    chart.set(df)

    chart.horizontal_line(200, func=on_horizontal_line_move)

    chart.show(block=True)
```

![callbacks gif](https://pypi-camo.freetls.fastly.net/7aa6286179752fc85e9ab8730ba5dffee9d9b137/68747470733a2f2f7261772e67697468756275736572636f6e74656e742e636f6d2f6c6f7569736e7730312f6c696768747765696768742d6368617274732d707974686f6e2f6d61696e2f6578616d706c65732f365f63616c6c6261636b732f63616c6c6261636b732e676966)

---

Inquiries: [shaders\_worker\_0e@icloud.com](mailto:shaders_worker_0e@icloud.com)

---

*This package is an independent creation and has not been endorsed, sponsored, or approved by TradingView. The author of this package does not have any official relationship with TradingView, and the package does not represent the views or opinions of TradingView.*