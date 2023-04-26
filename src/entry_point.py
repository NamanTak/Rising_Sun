import time
from datetime import datetime
import access_token
import repository
import pandas as pd
import numpy as np
import openpyxl
̐̐̐

##I have added this line


STOCK_NAME = "SHRIRAMFIN"
RESOLUTION = "D"

FROM_DAYS = 100
FUNDS = 250000 * 5
rr_ratio = 4

dema_time_period = 3
supertrend_ATR = 12
supertrend_Multiplier = 3
per = 1.03  # sell percentage criteria

# Constants
BUY_SIDE = 1
SELL_SIDE = -1

# Variables
OPEN_VALUES = []
HIGH_VALUES = []
LOW_VALUES = []
CLOSE_VALUES = []
EPOCH_VALUES = []
EMA_VALUES = []
FLAG = 0

# orderId = ""
# quantity = 1
# type = 1
# product_type = "INTRADAY"
# validity = "DAY"
# symbol = "NSE:" + STOCK_NAME + "-EQ"
# limit_price = 0


# Generating Stock Details
stock_meta_data = repository.pass_stock_data(STOCK_NAME, RESOLUTION, FROM_DAYS)

# Getting the entire data of the stock
entire_stock_data = access_token.get_fyers_entry_point().history(stock_meta_data)

# length of entire stock data
length_of_entire_stock_data = len(entire_stock_data['candles'])

for i in range(len((entire_stock_data)["candles"])):
    EPOCH_VALUES.append((entire_stock_data)["candles"][i][0])
    OPEN_VALUES.append((entire_stock_data)["candles"][i][1])
    HIGH_VALUES.append((entire_stock_data)["candles"][i][2])
    LOW_VALUES.append((entire_stock_data)["candles"][i][3])
    CLOSE_VALUES.append((entire_stock_data)["candles"][i][4])


# dataframe ke form me supertrend ko value pass kar raha hai:
dataframe_data = pd.DataFrame(
    {"HIGH": repository.list_to_numpy_array(HIGH_VALUES), "LOW": repository.list_to_numpy_array(LOW_VALUES),
     "CLOSE": repository.list_to_numpy_array(CLOSE_VALUES)})

# # Initialization Section
repository.buy_strategy_final_initializer_forDay(repository.get_supertrend(dataframe_data,supertrend_ATR,supertrend_Multiplier),repository.get_ema(CLOSE_VALUES,5),HIGH_VALUES,LOW_VALUES,CLOSE_VALUES,rr_ratio,FUNDS,EPOCH_VALUES)



print("\n====================APP CLOSED=====================")

# ********************************************************************************************************
