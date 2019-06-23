import os
import csv

csvpath = os.path.join('Bank.csv')
Results = 'results.txt'
outpath = os.path.join('Results')
Months = []
Revenue = []
Mchange = []


with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        Months.append(row[0])
        Revenue.append(int(row[1]))


Tmonth = len(Months)


Ginc = Revenue[0]
Gdec = Revenue[0]
total_revenue = 0
sum_revenue = Revenue[0]
sum_revenue_change = 0
previous_revenue = Revenue[0]
total_change = 0


for r in range(len(Revenue)):
    if Revenue[r] >= Ginc:
        Ginc = Revenue[r]
        great_inc_month = Months[r]
    elif Revenue[r] <= Gdec:
        Gdec = Revenue[r]
        great_dec_month = Months[r]
    total_revenue += Revenue[r]
    
    sum_revenue = sum_revenue + Revenue[r]

            #find change in revenue between this month and last month
    revenue_change = Revenue[r] - previous_revenue

            #add change in revenue to net change in revenue for data set
    sum_revenue_change = sum_revenue_change + revenue_change
    Mchange.append(sum_revenue_change)
    total_change += Mchange[r]

average_change = round(total_revenue/Tmonth)
avchange = round(total_change/Tmonth)

print("Total months: " + str(Tmonth))
print("Total: " + str(total_revenue))
print ("Average Change: " +str(average_change))
print ("Greatest Increase in Profits:" + str(Ginc))
print ("Greatest Decrease in Profits: " + str(Gdec))


with open(outpath, "w") as txt_file:
    txt_file.write("Total months: " + str(Tmonth))
    txt_file.write("Total: " + str(total_revenue))
    txt_file.write("Average Change: " +str(average_change))
    txt_file.write ("Greatest Increase in Profits:" + str(Ginc))
    txt_file.write ("Greatest Decrease in Profits: " + str(Gdec))

