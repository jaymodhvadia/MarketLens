# Economic Indicator Analyzer

## Overview

A Python-based financial data analysis project that collects, analyses and visualises real world financial data.

The project analyses the FTSE 100 and compares its performance with GBP/USD and Bitcoin.

## Features

- Downloads real time and historical financial data
- Analyses FTSE 100 performance
- Calculates average, highest and lowest closing values
- Calculates daily and annualised volatility
- Identifies the best and worst trading days
- Calculates a 30 day moving average
- Identifies short term market trends
- Calculates maximum drawdown
- Calculates a Sharpe ratio
- Compares FTSE 100 with GBP/USD
- Compares FTSE 100 with Bitcoin
- Calculates correlation between financial assets
- Analyses daily percentage returns
- Generates financial data visualisations
- Produces a market dashboard

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance
- CSV data

## Key Findings

During the period analysed:

- FTSE 100 overall change: **17.1%**
- FTSE 100 annualised volatility: **11.33%**
- Maximum drawdown: **-9.32%**
- Sharpe ratio: **1.09**
- FTSE 100 / GBP/USD correlation: **0.25**
- FTSE 100 / Bitcoin price correlation: **-0.88**
- FTSE 100 / Bitcoin daily-return correlation: **0.17**

The difference between the Bitcoin price correlation and daily-return correlation demonstrates why analysing percentage returns can provide a more meaningful measure of the relationship between financial assets.

## Project Structure

```text
Economic_Indicator_Analyzer/
│
├── market_data.py
├── analyse_data.py
├── report.py
├── dashboard.py
├── interest_rates.py
├── bitcoin_data.py
│
├── ftse100_history.csv
├── gbpusd_history.csv
├── bitcoin_history.csv
│
└── ftse100_dashboard.png