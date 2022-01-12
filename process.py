# This line is opening the file um-server-01.txt and assigning to the variable log_file.
log_file = open("um-server-01.txt") 

# This block of Python code is creating a function called sales_reports and
# looping throught each line and removing any white space at the end of each
# line. Then the sales_reports function is looping over each line again and
# filtering out any line that does not start with Tues. Lastly, the function is
# instructed to print the lines specified.
def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

# This line of code is calling the sales_reports function to fun on the opened file.
sales_reports(log_file)

# def melon_order(log_file):
#     for line in log_file:
#         line = line.rstrip()

#         melon_amt = line[16:18]
#         melon_amt = int(melon_amt.rstrp())
        
#         if melon_amt > 10:
#             print(line)

# melon_order(log_file)