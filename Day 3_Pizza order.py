print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Would you like to add extra cheese? Y or N: ")

s_price = 15
m_price = 20
l_price = 25
bill = 0

if add_pepperoni == "Y":
    if size == "S":
        bill = s_price + 2
    elif size == "M":
        bill = m_price + 3
    else:
        bill = l_price + 3
else:
    if size == "S":
        bill = s_price
    elif size == "M":
        bill = m_price
    else:
        bill = l_price
if extra_cheese == "Y":
    bill += 1

print(f'Your final bill is: ${bill}')
