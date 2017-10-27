import csv
import os

# file path
csvpath=("budget_data_2.csv")

#open the csv file
with open(csvpath, newline="") as csvfile:
    # Reading each row of the csv file as a dictionary
    csvReader = csv.DictReader(csvfile, delimiter=",")
    
    # create lists to store the revenues, dates and dates split
    revenueList = []
    dateList = []
    month = []
    monthlyRevenues = []
    # creating lists to store the revenues for each month across the year
    revenueDiffList = []
    JanRevenueList = []
    FebRevenueList = []
    MarRevenueList = []
    AprRevenueList = []
    MayRevenueList = []
    JunRevenueList = []
    JulRevenueList = []
    AugRevenueList = []
    SepRevenueList = []
    OctRevenueList = []
    NovRevenueList = []
    DecRevenueList = []
   
    for row in csvReader :
        # acessing each row in the csv file
        # appending items to the revenue list
        revenueList.append(int(row["Revenue"]))

        # appending items to the date list
        dateList.append(row["Date"])

        # appending items to the date split(month) list
        month.append((row["Date"]).split("-"))

        # appending the revenues to the corresponding month revenue list
        if(((row["Date"]).split("-"))[0] == "Jan") :
            JanRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Feb") :
            FebRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Mar") :
            MarRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Apr") :
            AprRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "May") :
            MayRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Jun") :
            JunRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Jul") :
            JulRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Aug") :
            AugRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Sep") :
            SepRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Oct") :
            OctRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Nov") :
            NovRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Nov") :
            NovRevenueList.append(int(row["Revenue"]))
        elif (((row["Date"]).split("-"))[0] == "Dec") :
            DecRevenueList.append(int(row["Revenue"]))
            
    # finding the total revenues
    sumOfRevenues = sum(revenueList)

    # Add all the revenues within each month revenue list and append them to monthly revenue list
    monthlyRevenues.append(sum(JanRevenueList))
    monthlyRevenues.append(sum(FebRevenueList))
    monthlyRevenues.append(sum(MarRevenueList))
    monthlyRevenues.append(sum(AprRevenueList))
    monthlyRevenues.append(sum(MayRevenueList))
    monthlyRevenues.append(sum(JunRevenueList))
    monthlyRevenues.append(sum(JulRevenueList))
    monthlyRevenues.append(sum(AugRevenueList))
    monthlyRevenues.append(sum(SepRevenueList))
    monthlyRevenues.append(sum(OctRevenueList))
    monthlyRevenues.append(sum(NovRevenueList))
    monthlyRevenues.append(sum(DecRevenueList))

    # finding the month over month revenue difference
    monthsRevenueDiffList = [l - p for p, l in zip(monthlyRevenues, monthlyRevenues[1:])]
   

    # finding Average change in revenue across the months in the entire year
    AvgChangeInRevenue = (sum(monthsRevenueDiffList))/(len(monthsRevenueDiffList))
   
   
    # calculating the Greatest increase and Decrease in revenues over the entire period
    revenueDiffList = [t - s for s, t in zip(revenueList, revenueList[1:])]
   
    maxRevDiff = max(revenueDiffList)
    revIndexMax = revenueDiffList.index(maxRevDiff)
    greatestIncreaseRevDate = dateList[(revIndexMax + 1)]

    minRevDiff = min(revenueDiffList)
    revIndexMin = revenueDiffList.index(minRevDiff)
    greatestDecreaseRevDate = dateList[(revIndexMin + 1)]

    # print the results to the terminal
    print(f'                          ')
    print(f' Financial Analysis ')
    print(f'---------------------------------------------')
    print(f'Total months : {len(revenueList)}')
    print(f'Total Revenue: ${sumOfRevenues}' )
    print(f'Average Change in Revenue: ${round(AvgChangeInRevenue)}')
    print(f'Greatest Increase in Revenue: {greatestIncreaseRevDate} (${maxRevDiff})')
    print(f'Greatest Decrease in Revenue: {greatestDecreaseRevDate} (${minRevDiff})')

    output_filepath = "OutPyBank2.txt"
    with open(output_filepath,"w") as write_file :
        # write the results to a text file
        write_file.write('\nFinancial Analysis\n')
        write_file.write("-----------------------------------\n")
        write_file.write('Total months: %s\n' %len(revenueList))
        write_file.write('Total Revenue: $%s\n' %sumOfRevenues)
        write_file.write('Average Change In Revenue: $%s\n' %round(AvgChangeInRevenue))
        write_file.write('Greatest Increase In Revenue: %s' %greatestIncreaseRevDate)
        write_file.write('($%s)\n' %maxRevDiff)
        write_file.write('Greatest Decrease In Revenue: %s' %greatestDecreaseRevDate)
        write_file.write('($%s)\n' %minRevDiff)

    