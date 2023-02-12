
exp = [2000, 2300, 1500, 500];
# print(exp)
print("Total expenses are: ", exp[0] + exp[1] + exp[2] + exp[3])
# So if we have hundreds of items, then it is very difficult to display the result...
# We need to write each of them separately.
# To avoid this we can use for loop or for statements:
total = 0
for items in exp:
    total = total + items
print("Total expenses are: ", total)

# We can display a specific range using for statement.
for l in range(1, 10):
    print(l)

# We can also display each month name with its expenses:
total = 0
for i in range(len(exp)):
     print("Month: ", (i+1), " Expense: ", exp[i])
     total = total + exp[i]
print("Total expense is: ", total)

#simple while loop example:
i = 0
while i <= 10:
    print(i)
    i = i + 1






