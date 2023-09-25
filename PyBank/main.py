import os
import csv

tot_months = 0
net_PL = 0
prev_PL = 0

PL_changes = []
months = []

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        date = row[0]
        PL = int(row[1])

        tot_months += 1

        net_PL += PL

        if tot_months >>1:
            change = PL - prev_PL
            PL_changes.append(change)
            months.append(date)

        prev_PL = PL

avg_chg = sum(PL_changes) / len(PL_changes)

increase = max(PL_changes)
decrease = min(PL_changes)

inc_ind = PL_changes.index(increase)
dec_ind = PL_changes.index(decrease)

inc_dt = months[inc_ind]
dec_dt = months[dec_ind]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {tot_months}")
print(f"Total: ${net_PL}")
print(f"Average Change: ${avg_chg:.2f}")
print(f"Greatest Increase in Profits: {inc_dt} (${increase})")
print(f"Greatest Decrease in Profits: {dec_dt} (${decrease})")


output_file_path = "financial_analysis.txt"
with open(output_file_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write(f"Total Months: {tot_months}\n")
    output_file.write(f"Total: ${net_PL}\n")
    output_file.write(f"Average Change: ${avg_chg:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {inc_dt} (${increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {dec_dt} (${decrease})\n")
