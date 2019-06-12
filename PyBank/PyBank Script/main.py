import os, csv


#access and read csv file
budgetdata_csv = os.path.join("..", "budget_data.csv")

date_list = []
profit_loss_list = []
sumprofit = 0
profit = 0
profit_loss = 0



with open(budgetdata_csv, newline="", encoding="UTF8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader, None)

    #print(csv_header)

    for row in csv_reader:
        date_list.append(row[0])
        profit_loss_list.append(row[1])

        
    
    # sum of profit and loss
        profit = int(row[1])
        if profit > 0: 
            sumprofit = profit + sumprofit
        elif profit < 0:
            profit_loss = profit + profit_loss

        totalprofitloss = sumprofit + profit_loss

#define the revenue change for average
greatest_profit = profit_loss_list[0]
greatest_loss = profit_loss_list[0]
tot_revenue_for_change = 0

for r in range(len(profit_loss_list)):
    if profit_loss_list[r] >= greatest_profit:
        greatest_profit = profit_loss_list[r]
        greatest_profit_month = date_list[r]

    elif profit_loss_list[r] <= greatest_loss:
        greatest_loss = profit_loss_list[r]
        greatest_loss_month = date_list[r]

# print(greatest_loss)
# print(greatest_profit)


        # if int(greatest_profit[1]) < int(profit_loss_list[1])


        # print(date)
        # print(profit_loss)


print("Financial Analysis")
print("-" * 20)
print("Total Months:",len(date_list))
print("Total: $", totalprofitloss)
print("Greatest Increase in Profits: " + greatest_profit)
print("Greatest Decrease in Profits: " + greatest_loss)
# print("Average Change: $" + Average)



# print(sumprofit) 
# print(totalprofitloss)




        




    














