import pandas as pd
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id = 'bitcoin', vs_currency = 'usd', days = 60)
bitcoin_data['prices']

data = pd.DataFrame(bitcoin_data, columns = ['TimeStamp', 'Price'])
data = pd.DataFrame(bitcoin_data['prices'], columns = [ 'Timestamp', 'Prices'])
values = [bitcoin_data['prices'], bitcoin_data['market_caps']]
values

data['Date'] = pd.to_datetime(data['Timestamp'], unit = 'ms')

candlestick_data = data.groupby(data.Date.dt.date).agg({'Prices': ['min', 'max','first', 'last']})
candlestick_data

open= candlestick_data['Prices']['first']

import plotly
import plotly.graph_objects as go

fig = go.Figure(data = [go.Candlestick(x = candlestick_data.index,
                                       open= candlestick_data['Prices']['first'],
                                       high = candlestick_data['Prices']['max'],
                                       low = candlestick_data['Prices']['min'],
                                       close = candlestick_data['Prices']['last'])])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title = 'Date', yaxis_title = '$ Prices (USD)', title= 'Bitcoin Candlestick Chart Over Past 60 Days')
fig.show()