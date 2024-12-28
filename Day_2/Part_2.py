"""
Advent of code : Day 2
Part 2
"""

# Creates a empty list that will contain all reports from the input file
report_list = []

# Adds all the reports to the list
with open("input.txt") as file:
    for line in file:
        report_list.append(line.strip().split(" "))

# Converts all levels from string to int in the report list
for report in report_list:
    for level in range(len(report)):
        report[level] = int(report[level])

# Initializes the safe reports counter to 0
safe_reports_number = 0

# Goes trough each report in the report list
# Initialises the safeness of report to true
# Checks all conditions, if the report is safe, adds 1 to tu counter
for report in report_list:
    report_is_safe = True

    # Checks the ascending or descending order of the first items and then checks if all the rest is in the
    # same order, also validates that the difference between level is between 1 and 3.
    if report[0] < report[1]:
        for i in range(len(report)-1):
            if report[i] > report[i+1]:
                report_is_safe = False
            if abs(report[i] - report[i+1]) > 3 or abs(report[i] - report[i+1]) < 1 :
                report_is_safe = False

    elif report[0] > report[1]:
        for i in range(len(report)-1):
            if report[i] < report[i+1]:
                report_is_safe = False
            if abs(report[i] - report[i+1]) > 3 or abs(report[i] - report[i+1]) < 1 :
                report_is_safe = False

    # If the first item is not bigger or smaller than the 2nd, they are equal so the rapport is not safe
    else:
        report_is_safe = False

    # After calidation loops, adds one to the counter if the report is considered safe
    if report_is_safe:
        safe_reports_number +=1

    #Part Two Starts here :)
    #Comments incomming
    if not report_is_safe:
        dampened_report_list = []
        for a in range(len(report)):
            dampened_report_list.append(report[:a]+report[a+1:])

        damp_report_safe_counter = 0

        for damp_report in dampened_report_list:
            damp_report_is_safe = True

            # Checks the ascending or descending order of the first items and then checks if all the rest is in the
            # same order, also validates that the difference between level is between 1 and 3.
            if damp_report[0] < damp_report[1]:
                for i in range(len(damp_report) - 1):
                    if damp_report[i] > damp_report[i + 1]:
                        damp_report_is_safe = False
                    if abs(damp_report[i] - damp_report[i + 1]) > 3 or abs(damp_report[i] - damp_report[i + 1]) < 1:
                        damp_report_is_safe = False

            elif damp_report[0] > damp_report[1]:
                for i in range(len(damp_report) - 1):
                    if damp_report[i] < damp_report[i + 1]:
                        damp_report_is_safe = False
                    if abs(damp_report[i] - damp_report[i + 1]) > 3 or abs(damp_report[i] - damp_report[i + 1]) < 1:
                        damp_report_is_safe = False

            # If the first item is not bigger or smaller than the 2nd, they are equal so the rapport is not safe
            else:
                damp_report_is_safe = False

            # After calidation loops, adds one to the counter if the report is considered safe
            if damp_report_is_safe:
                damp_report_safe_counter += 1
        if damp_report_safe_counter > 0:
            safe_reports_number += 1

# Prints the result
print(safe_reports_number)