import time
from datetime import datetime
import access_token
import repository
import pandas as pd
import numpy as np
import openpyxl
import math
import pytz
import time
from datetime import datetime
import access_token
import repository
import pandas as pd

STOCK_NAME = "SHRIRAMFIN"
RESOLUTION = "5"
FROM_DAYS = 2
FUNDS = 250000 * 5
rr_ratio = 4
supertrend_ATR = 12
supertrend_Multiplier = 3
# Variables
OPEN_VALUES = []
HIGH_VALUES = []
LOW_VALUES = []
CLOSE_VALUES = []
EPOCH_VALUES = []
EMA_VALUES = []
FLAG = 0

flag = True # Using for Buy or Sell
flag2 = True # Using for market close
flag3 = True # Using for buy in range
humantime = '2023-04-25 17:49:00'
seconds = int(repository.get_epoch_from_humantime(humantime))
timezone = pytz.timezone('Asia/Kolkata')  # replace with your local timezone

# Initialization Section
while True: # intellij terminal active

    if(int(time.time()) == seconds):
        local_time = datetime.fromtimestamp(seconds, timezone).strftime(' %H:%M:%S')
        print(local_time)

        forloop_ka_i = 0
        while True:


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

            # # dataframe ke form me supertrend ko value pass kar raha hai:
            dataframe_data = pd.DataFrame(
                {"HIGH": repository.list_to_numpy_array(HIGH_VALUES), "LOW": repository.list_to_numpy_array(LOW_VALUES),
                 "CLOSE": repository.list_to_numpy_array(CLOSE_VALUES)})


            supertrend = repository.get_supertrend(dataframe_data,supertrend_ATR,supertrend_Multiplier)
            ema = repository.get_ema(CLOSE_VALUES,5)
            high = HIGH_VALUES
            low = LOW_VALUES
            close = CLOSE_VALUES
            rr = 4
            fund = FUNDS
            epoch = EPOCH_VALUES

            m = len(close)
            counter = 0
            # flag = True # Can be purchased
            # flag2 = True # Using for market close
            # flag3 = True # Using for buy in range
            profit = 0
            net_pnl = 0
            trade_counter = 0
            risk_per_trade = 3000
            a = 146
            b = 144
            c = 149

            trade_book = {
                "EPOCH":[],
                "Index": [],
                "Buy": [],
                "Quantity": [],
                "Total buy amount": [],
                "Risk": [],
                "Stoploss": [],
                "Sell": [],
                "Total sell amount": [],
                "PnL": [],
                "Net PnL": [],

            }

            while(forloop_ka_i <= 149):
                if(forloop_ka_i >= 75):


                    if b < forloop_ka_i < c:
                        flag3 = False
                    else:
                        flag3 = True

                    if forloop_ka_i<(m-1) and \
                            supertrend['Supertrend'][forloop_ka_i] == True and \
                            ema[forloop_ka_i] > high[forloop_ka_i] and \
                            close[forloop_ka_i + 1] > high[forloop_ka_i] and \
                            flag == True and flag3 == True:

                        print(f"Under BUY condition, a = {a}, forloop_ka_i = {forloop_ka_i}\n")

                        buy = close[forloop_ka_i + 1]
                        flag = False
                        flag2 = True

                        stoploss = low[forloop_ka_i] if low[forloop_ka_i] < low[forloop_ka_i + 1] else low[forloop_ka_i + 1]
                        target = abs(close[forloop_ka_i + 1] - stoploss) * rr + close[forloop_ka_i + 1]
                        risk = abs(buy - stoploss)

                        quantity = math.trunc(fund/buy)

                        if (quantity * risk) > risk_per_trade:
                            jobana = (quantity * risk)/risk_per_trade
                            quantity = math.trunc(quantity / jobana)

                        if quantity % 2 != 0:
                            quantity = quantity - 1

                        total_buy_amount = buy * quantity

                        trade_book["EPOCH"].append(epoch[forloop_ka_i])
                        trade_book["Index"].append(forloop_ka_i)
                        trade_book["Buy"].append(buy)
                        trade_book["Stoploss"].append(stoploss)
                        trade_book["Risk"].append(risk)
                        trade_book["Quantity"].append(quantity)
                        trade_book["Total buy amount"].append(total_buy_amount)
                        trade_book["Sell"].append("NaN")
                        trade_book["Total sell amount"].append("NaN")
                        trade_book["PnL"].append("NaN")
                        trade_book["Net PnL"].append("NaN")


                    elif flag == False and close[forloop_ka_i] <= stoploss:
                        print(f"Under STOPLOSS condition, a = {a}, forloop_ka_i = {forloop_ka_i}\n")

                        sell = close[forloop_ka_i]
                        # print(f"The sell value of {forloop_ka_i} candle is {sell}")
                        flag = True
                        flag2 = False
                        counter = counter + 1
                        profit = (sell - buy) * quantity
                        net_pnl = net_pnl + profit
                        total_sell_amount = quantity * sell
                        # print(f"No. of share sold: {quantity} and total amount to sell (stoploss): {total_sell_amount}")
                        # print(f"Profit of {forloop_ka_i} trade(stoploss): {profit}")
                        trade_counter = trade_counter + 1

                        trade_book["EPOCH"].append(epoch[forloop_ka_i])
                        trade_book["Index"].append(forloop_ka_i)
                        trade_book["Buy"].append("NaN")
                        trade_book["Stoploss"].append("NaN")
                        trade_book["Risk"].append("NaN")
                        trade_book["Quantity"].append(quantity)
                        trade_book["Total buy amount"].append("NaN")
                        trade_book["Sell"].append(sell)
                        trade_book["Total sell amount"].append(total_sell_amount)
                        trade_book["PnL"].append(profit)
                        trade_book["Net PnL"].append(net_pnl)

                    elif flag == False and close[forloop_ka_i] >= target:
                        print(f"Under TARGET condition, a = {a}, forloop_ka_i = {forloop_ka_i}\n")

                        sell = close[forloop_ka_i]
                        # print(f"The sell value of {forloop_ka_i} candle is {sell}")
                        profit = (sell - buy) * quantity
                        net_pnl = net_pnl + profit
                        flag = True
                        flag2 = False
                        trade_counter = trade_counter + 1
                        total_sell_amount = quantity * sell
                        # print(f"No. of share sold: {quantity} and total amount to sell:{total_sell_amount}")
                        # print(f'Profit of {forloop_ka_i} trade: {profit}')

                        trade_book["EPOCH"].append(epoch[forloop_ka_i])
                        trade_book["Index"].append(forloop_ka_i)
                        trade_book["Buy"].append("NaN")
                        trade_book["Stoploss"].append("NaN")
                        trade_book["Risk"].append("NaN")
                        trade_book["Quantity"].append(quantity)
                        trade_book["Total buy amount"].append("NaN")
                        trade_book["Sell"].append(sell)
                        trade_book["Total sell amount"].append(total_sell_amount)
                        trade_book["PnL"].append(profit)
                        trade_book["Net PnL"].append(net_pnl)

                    elif flag == False and forloop_ka_i >= a and flag2 == True:

                        print(f"Under MARKET CLOSE condition, a = {a}, forloop_ka_i = {forloop_ka_i}\n")

                        sell = close[forloop_ka_i]
                        # print(f"The sell value of {forloop_ka_i} candle is {sell}")
                        profit = (sell - buy) * quantity
                        net_pnl = net_pnl + profit
                        flag = True
                        flag2 = False
                        trade_counter = trade_counter + 1
                        total_sell_amount = quantity * sell

                        trade_book["EPOCH"].append(epoch[forloop_ka_i])
                        trade_book["Index"].append(forloop_ka_i)
                        trade_book["Buy"].append("NaN")
                        trade_book["Stoploss"].append("NaN")
                        trade_book["Risk"].append("NaN")
                        trade_book["Quantity"].append(quantity)
                        trade_book["Total buy amount"].append("NaN")
                        trade_book["Sell"].append(sell)
                        trade_book["Total sell amount"].append(total_sell_amount)
                        trade_book["PnL"].append(profit)
                        trade_book["Net PnL"].append(net_pnl)

                # while wali line
                forloop_ka_i = forloop_ka_i + 1

            print(f"net_pnl: {net_pnl} and no. of trades: {trade_counter} and stoploss counter: {counter} ")
            trade_book_data_frame = pd.DataFrame(trade_book)
            print(trade_book_data_frame.to_string())
            trade_book_data_frame.to_excel("Trade_book.xlsx", "Book1")

            print(pd.DataFrame(entire_stock_data))
            time.sleep(300.0 - ((time.time() - seconds) % 300.0))



