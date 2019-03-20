
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('output', 'budget_data.txt')


total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 867884
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []



with open(csvpath, newline='') as csvfile:

    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
	

   
    for row in csvreader:
		
      
        total_months += 1

        
        total_revenue = total_revenue + int(row[1])

      
        revenue_change = float(row[1])- previous_revenue
        previous_revenue = float(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        
             
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= round(revenue_change)
            greatest_increase[0] = row[0]

  
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= round(revenue_change)
            greatest_decrease[0] = row[0]
    
	
    print("\n")
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_change_list) / (len(revenue_change_list)-1),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

	

with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: " + str(total_months)+"\n")
    file.write("Total: " + "$" + str(total_revenue)+"\n")
    file.write("Average Change: " + "$" + str(round(sum(revenue_change_list) / (len(revenue_change_list)-1),2))+"\n")
    file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")\n")
    file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")