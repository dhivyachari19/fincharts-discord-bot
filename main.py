from discord.ext import commands
import os
import discord
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def compound(ctx, ticker: str):
  start = dt.datetime.today() - dt.timedelta(365)
  end = dt.datetime.today()
  cl_price = pd.DataFrame()
  cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]
  cl_price.dropna(axis=0,how='any',inplace=True)
  daily_return = cl_price.pct_change()
  (1+daily_return).cumprod().plot(title = f"Compounded Return on {ticker}")
  plt.savefig("compound.png")
  await ctx.send(file = discord.File("compound.png"))

@bot.command()
async def candlestick(ctx, ticker: str):
  ohlcv_data = yf.download(ticker, period="1mo", interval="1d")
  ohlcv_data.dropna(how="any",inplace=True)
  up = ohlcv_data[ohlcv_data["Adj Close"] >= ohlcv_data["Open"]]
  down = ohlcv_data[ohlcv_data["Adj Close"] < ohlcv_data["Open"]]
  body_width = 0.5
  shadow_width = 0.05
  up_color = 'green'
  down_color = 'red'
  #plotting rises in price
  plt.bar(up.index, height= up["Adj Close"]-up["Open"], width= body_width, bottom= up["Open"], color= up_color)
  plt.bar(up.index, height = up["High"] - up["Adj Close"], width = shadow_width, bottom = up["Adj Close"], color = up_color)
  plt.bar(up.index, height = up["Low"] - up["Open"], width = shadow_width, bottom = up["Open"], color = up_color)
  #plotting falls in price
  plt.bar(down.index, height = down["Adj Close"] - down["Open"], width = body_width, bottom = down["Open"], color = down_color)
  plt.bar(down.index, height = down["High"] - down["Open"], width = shadow_width, bottom = down["Open"], color = down_color)
  plt.bar(down.index, height = down["Low"] - down["Adj Close"], width = shadow_width, bottom = down["Adj Close"], color = down_color)
  #formatting
  plt.xticks(rotation=50, ha='right')
  plt.title(f"Candlestick Chart of {ticker}")
  plt.style.use('ggplot')
  plt.savefig("candlestick.png")
  await ctx.send(file = discord.File("candlestick.png"))

def MACD(DF, a=12, b=26, c=9):
    df = DF.copy()
    df["ma_fast"] = df["Adj Close"].ewm(span = a, min_periods = a).mean()
    df["ma_slow"] = df["Adj Close"].ewm(span = b, min_periods = b).mean()
    df["macd"] = df["ma_fast"] - df["ma_slow"]
    df["signal"] = df["macd"].ewm(span = c, min_periods = c).mean()
    return df.loc[:,["macd", "signal"]]

@bot.command()
async def macd(ctx, ticker: str):
  ohlcv_data = yf.download(ticker, period="1mo", interval="15m")
  ohlcv_data.dropna(how="any",inplace=True)
  ohlcv_data[["MACD", "Signal"]] = MACD(ohlcv_data)
  ohlcv_data.dropna(how="any",inplace=True)
  macd = ohlcv_data[["MACD", "Signal"]]
  macd.plot(title = f"MACD and Signal Line of {ticker}", legend=True)
  plt.savefig("macd.png")
  await ctx.send(file = discord.File("macd.png"))
  
password = os.environ['password']
bot.run(password)