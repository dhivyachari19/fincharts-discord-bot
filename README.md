#fincharts-discord-bot

##Introduction

'fincharts-discord-bot' is a Discord chatbot that uses command lines to generate 3 different kinds of financial charts. Charts are produced when the user sends a message containing a specific command into a Discord server that has the chatbot implemented. This message includes a command prefix, immediately followed by the command name, and the stock ticker/symbol which corresponds to the certain security that a user would like to produce information about. This chatbot uses the 'yfinance' library to import data from Yahoo Finance.

##Requirements

A Discord account is required to create a chatbot, add it to a server, and run its commands. Please access the Discord Developer Page (https://discord.com/developers/applications) and follow these steps:

- Name and create your bot.
- Go to bot page on the sidebar and click ‘Add Bot’.
- Scroll down to ‘TOKEN’ and click on copy. This is the bot’s password we use to login into it. Reset the token if you were unable to copy the token.
- Be careful to NEVER share the token, or your bot could be stolen.
- Make sure to tick all three of Privileged Gateway Intents.
- Create a key called “password” and paste your token there. Make sure to never make it public - or else your token might get stolen.

##Charts

The commands for all of the charts use the command prefix '!' and only accept one string input from the user, other than the command itself. '{ticker}' is to be replaced by the capitalized stock symbol for the particular security chosen by the user (ex: 'AAPL', 'CSCO', 'AMZN').

###Candlestick

The candlestick chart indicates the high, low, open, and close prices of the selected stock over a period of one month and recorded at an interval of daily. The command is '!candlestick {ticker}'.

###Compounded Return

This chart visualizes the compounded growth of an investment in the selected security over the course of one year. The command is '!compound {ticker}'.

###MACD and Signal Line

This chart plots the MACD (moving average convergence/divergence) and signal lines of the selected stock. Both MACD and signal lines are technical indicators used to identify changes in trends of a stock's price. When the MACD line rises past the signal line, this indicates a bullish signal (rise in prices); whereas when the MACD line lies below the signal line, the indicator gives a bearish signal (fall in prices). The command for this chart is '!macd {ticker}'.