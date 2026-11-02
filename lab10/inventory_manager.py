#1 The most surprising thing about Python lists is how easy it is to store multiple values in one variable and work with all of them using a loop. Before learning about lists, I thought I would have to create a separate variable for every value
#2 One situation where a Python list would have saved me time is tracking daily sales for a business. Instead of manually adding sales numbers together in Excel, I could store all the sales in a Python list and use a loop to calculate the total.

#exercise 1 
inventory = ["pen", "notebook", "tape", "stapler", "marker"]
print(inventory)
print(len(inventory))
#exercise 2
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle]) #grabs middle item in the list(not hard coded)

#exercise 3 
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#exercise 4
inventory.append("envelope")
inventory.remove("tape")
inventory.sort()
print(inventory)





#exercise 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError: {error}")
    print("Tuples protect coordinates from being changed by accident.")

#exercise 6
sales = [100,250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"best sale: {max(sales)}")
print(f"worst sale: {min(sales)}")