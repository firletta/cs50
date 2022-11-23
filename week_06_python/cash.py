# Implement a program that calculates the minimum number of coins required to give a user change.

# $ python cash.py
# Change owed: 0.41
# 4

while True:
    try:
        amount = float(input("Cash: "))
        if amount > 0:
            break
        else:
            print("Please input a positive amount.")
    except ValueError:
        print("Please input an amount.")

total_coins = 0

for coin in [0.25, 0.10, 0.05, 0.01]:
    number_of_coins = amount // coin
    amount = round(amount - coin * number_of_coins, 2)
    total_coins += int(number_of_coins)

print(f"Change: {total_coins}")
    


