#self assesment questions
#1 The first bug I spotted was the miswsing colon on the second part of the code line57 msising the colon and breaking for/in statement.
#2 Apply_discount(price ,tier) applies the discount and reads the tier of the disocunt right next to it. If I am right  I believe a collegue can use it without reading the body due to its simplicity.
#3 I used chat gpt to better understand what errors were being made on the broken sales document buyt it help me understand what error there was rather than just plain showing it.
#exercise one
def calculate_tax(price, rate):
    return price * rate  #call the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: {calculate_tax(350, 0.05):.2f}")
#exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

#calling funtion with ddiferent tiers
original_price = 200

for tier in [ "gold", "silver", "bronze", "none"]:

    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#exercise 3 
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

#calling the fina;_price function
print(f"final_price(200, 0.07, 'gold) = ${final_price(200, 0.07, 'gold'):.2f}")

#exercise 4
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

#exercise 5
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # so i found it wrong that the total = 90 so iaked chatgpt what was wrong and it explained that there was forgotten plus sign and so the straight up equal sign makes python think your looking for the first sale on the list rather than adding all of them up and creatingthe total.
print(f"Total: ${total}")

count = 0
for sale in sales: # I found this on my with help from a classmate who pointed it out in class
    count += 1
print(f"Count: {count}")

i = 0
for i in range(len(sales)): #chatgpt said that python is searching for an item that dosen't exist and saying the loop is counting too far.
    print(sales[i])
    i += 1 
sales = [120, 80, 250, 175, 90]






#exercise 6

x = 100 # global

def double_it():
    x = 999 
    return x * 2

print(x) #100 comes out
print(double_it()) #1998 come out
print(x) # 100 come out again because python reads in llines and 100 was the first line of code out.