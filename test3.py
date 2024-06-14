import pandas as pd

data = pd.read_csv("test2_2.csv")
data['profit_level'] = ''
data.to_csv('test3.csv', index=0)

data = pd.read_csv("test3.csv")
data_cy = data.copy()
for i in range(len(data)):
    if(str(data['budget'][i]) == '0' or str(data['budget'][i]) == '1' or str(data['revenue'][i]) == '0' or str(data['budget'][i]) == '1'):
        data_cy['profit_level'][i] = '0'
    else:
        profit_ratio = (int(data['revenue'][i]) - int(data['budget'][i])) / int(data['budget'][i])
        if profit_ratio >= float(1):
            profit_level = 3
            print(profit_level)
            data_cy['profit_level'][i] = '3'
        elif float(0.5) <= profit_ratio < float(1):
            profit_level = 2
            print(profit_level)
            data_cy['profit_level'][i] = '2'
        else:
            profit_level = 1
            print(profit_level)
            data_cy['profit_level'][i] = '1'
data = data_cy.copy()
data.to_csv('test3_1.csv', index=0)

