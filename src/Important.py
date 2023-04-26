# 1. EMA Strategy
# EMA_VALUES = repository.get_ema(CLOSE_VALUES, 5)
# repository.ema_initializer(HIGH_VALUES,CLOSE_VALUES,LOW_VALUES,EMA_VALUES,5, length_of_entire_stock_data, quantity, symbol,type,BUY_SIDE,SELL_SIDE,product_type,limit_price, 2)



# INDEX_LIST = []
# for i in range (0,12):
#     INDEX_LIST.append(i)
#     print(i)
# for i in range (75,86):
#     INDEX_LIST.append(i)
#     print(i)
# for i in range (150,161):
#     INDEX_LIST.append(i)
#     print(i)
# for i in range (225,236):
#     INDEX_LIST.append(i)
#     print(i)
# for i in range (300,311):
#     INDEX_LIST.append(i)
#     print(i)
# print(INDEX_LIST)


# import time

#important code

# sum_buy = 0
# sum_sell = 0
# a = 0
# buy_value = 0
# trade_counter = 0 # it will count sell orders
# trade_diff_result = []
# discrete_diff = 0
#
# INDEX_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# for i in range(len(INDEX_LIST)):
#     if CLOSE_VALUES[INDEX_LIST[i]] > repository.get_dema(repository.list_to_numpy_array(CLOSE_VALUES),
# dema_time_period)[INDEX_LIST[i]] and repository.get_supertrend(dataframe_data, supertrend_ATR, supertrend_Multiplier)["Supertrend"][INDEX_LIST[i]]:
#         print(INDEX_LIST[i],"BUy @ ", i )

# for i in range(len(CLOSE_VALUES)):
#     if CLOSE_VALUES[i] > repository.get_dema(repository.list_to_numpy_array(CLOSE_VALUES),
#                                              dema_time_period)[i] and \
#             repository.get_supertrend(dataframe_data, supertrend_ATR, supertrend_Multiplier)["Supertrend"][i] and a != 1:
#         print("BUY @ UserIndex: ", (i+1), " SystemIndex: ", i)
#         sum_buy += CLOSE_VALUES[i]
#         buy_value = CLOSE_VALUES[i]
#         buy_index = i
#         a = 1
#     elif (repository.get_supertrend(dataframe_data, supertrend_ATR, supertrend_Multiplier)["Supertrend"][i] == False or (buy_value * (per) <
#                                                                                                                          CLOSE_VALUES[i])) and a == 1:
#         print("SELL @ UserIndex: ", (i+1), " SystemIndex: ", i)
#         sum_sell += CLOSE_VALUES[i]
#         trade_counter = trade_counter + 1
#         sell_value = CLOSE_VALUES[i]
#         a = 0
#
#
#         buy_dict = {
#             "index": buy_index,
#             "value": buy_value
#         }
#
#         sell_dict = {
#             "index": i,
#             "value": sell_value
#         }
#
#         trade_diff = sell_value - buy_value
#         serial_number = trade_counter
#
#         temp_list = []
#         discrete_diff = trade_diff + discrete_diff
#
#         temp_list.append(serial_number)
#         temp_list.append(buy_dict)
#         temp_list.append(sell_dict)
#         temp_list.append(trade_diff)
#         temp_list.append(discrete_diff)
#
#         trade_diff_result.append(temp_list)


# print(repository.get_dema(repository.list_to_numpy_array(CLOSE_VALUES),dema_time_period))
# print(pandas.DataFrame(trade_diff_result).to_string())


# dataframe_data = pd.DataFrame(
#     {"HIGH": repository.list_to_numpy_array(HIGH_VALUES), "LOW": repository.list_to_numpy_array(LOW_VALUES),
#      "CLOSE": repository.list_to_numpy_array(CLOSE_VALUES)})

# from datetime import datetime
#
# now = datetime.now()
#
# current_time = now.strftime("%H")
# print("Current Time =", current_time)
#
# import repository



# from urllib.parse import urlparse, parse_qs
#
# url = "https://api.fyers.in/api/v2/generate-authcode?client_id=JBGZVR59OA-100&redirect_uri=https%3A%2F%2Fwww.google.com%2F&response_type=code&state=None"
#
# parsed_url = urlparse(url)
# query_params = parse_qs(parsed_url.query)
#
# key_to_retrieve = 'client_id'
#
# if key_to_retrieve in query_params:
#     value = query_params[key_to_retrieve][0]
#     print(f'The value of {key_to_retrieve} is {value}')
# else:
#     print(f'The key {key_to_retrieve} is not present in the URL')


# import pyperclip
# import pyautogui
# import time
#
# # Simulate the keyboard shortcut to copy the URL to the clipboard
# pyautogui.hotkey('ctrl', 'l')
# pyautogui.hotkey('ctrl', 'c')
#
# # Wait for a short time to ensure the clipboard has been updated
# time.sleep(0.5)
#
# # Retrieve the URL from the clipboard using the pyperclip library
# url = pyperclip.paste()
#
# # Print the retrieved URL
# print(url)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import webbrowser





for i in range(10):
    if i > 2:
        print(123232)
    if i> 3:
        print("sdf")



# 1645030750 for feb 17 2022
# 1652720350 for may 17 2022


import openpyxl
import pandas
import pandas as pd

a = {"a": [100]}
b = {"b": [200]}
c = {"a": [1000]}

# with pandas.ExcelWriter('1.xlsx', mode='a') as writer:
#     pandas.DataFrame(a).to_excel(writer, sheet_name='sheet A', index=False)
#     pandas.DataFrame(b).to_excel(writer, sheet_name='sheet B', index=False)
#     pandas.DataFrame(c).to_excel(writer,sheet_name='sheet A')

# # read the demo2.xlsx file
# df = pd.read_excel("1.xlsx")
#
# # appending the data of df after the data of demo1.xlsx
# with pd.ExcelWriter("1.xlsx",mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
#     pd.DataFrame(c).to_excel(writer, sheet_name="sheet A",header=None, startrow=writer.sheets["sheet A"].max_row,index=False)'


# Create a new workbook

openpyxl.Workbook().save("123.xlsx")

# wb = openpyxl.Workbook()
# openpyxl.Workbook().get_sheet_by_name("123.xlsx")


# Load the existing workbook
workbook = openpyxl.load_workbook('123.xlsx')

# Create new empty worksheets
worksheet2 = workbook.create_sheet('Sheet2')
worksheet3 = workbook.create_sheet('Sheet3')
worksheet4 = workbook.create_sheet('Sheet4')

# Save the workbook
workbook.save('123.xlsx')

# wb.create_sheet("sheet aaaaa", )
# wb.create_sheet("sheet nbnbvdbs", )


print("done")





