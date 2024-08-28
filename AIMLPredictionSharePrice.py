from neuralprophet import NeuralProphet
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

stocks_symbol = '005935.KS' #Samsung
start_date = '2015-01-01'
end_date = '2023-01-01'

stock_data = yf.download(stocks_symbol, start = start_date, end=end_date)
stock_data.to_csv('stock_data.csv')

stocks = pd.read_csv('stock_data.csv')
stocks['Date'] = pd.to_datetime(stocks['Date'])
stocks = stocks[['Date', 'Close']]
stocks.columns = ['ds', 'y']

model = NeuralProphet()
model.fit(stocks)

future = model.make_future_dataframe(stocks, periods=300)

forecast = model.predict(future)
actual_prediction = model.predict(stocks)

plt.plot(actual_prediction['ds'],actual_prediction['yhat1'], label='Actual_Pred', c='r')
plt.plot(forecast['ds'],forecast['yhat1'], label='Forcast', c='b')
plt.plot(stocks['ds'],stocks['y'], label='Actual', c='g')
plt.show()

model.plot_components(forecast)