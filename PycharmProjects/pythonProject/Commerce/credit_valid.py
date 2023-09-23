discount = 0
down_payment = 0
second_down_payment = 0
price = 100
creds = 0
# total = 0
credit_score = input("Enter credit score")
# while creds >= 10:
for creds in range(1, 11):
    credit_score = int(input("Enter credit score"))
    # total = credit_score + total
    discount = (price + credit_score) / 10
    down_payment = (price + credit_score) / 10
    # creds = creds +1
    if credit_score < 10:
        # credit_score = input(" below credit benchmark")
        second_down_payment = (price + credit_score) / 25
    # creds = creds +1    # if credit_score < 10:
    #     # discount = price / 10
    #     down_payment = price / 25

# credit_score = input("")

print("Your discount is ", discount, "You are to make a down payment of ", down_payment,
      "Due to you low credit score,you are to make a down payment of ", second_down_payment)