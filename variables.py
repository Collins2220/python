#if=do some code only if condition is true
      # Else do something else
# Variables for bank payment
payment_processed = False
sufficient_funds = True

# Check bank payment status
if payment_processed and sufficient_funds:
    print("Payment successful!")
else:
    print("Payment failed. Please check your account.")

age=int(input("how old are you:"))

if age==18:
    print("you are signed in !")
elif age==17:
    print("you are signed out!")
else:
    print("in process")

is_teaching=True

if is_teaching:
    print("very well")
else:
    print("very bad")

delicious_food="pizza"

if delicious_food=="pizza":
    print("i love good food")
elif delicious_food=="salad":
    print("salad is nice!")
else:
    print("they are both tasty")

name="james"

if name=="james":
    print("excellent")
elif name=="collins":
    print("services assured")
else:
    print("nice one")

is_praying=True

if is_praying:
    print("he went to church")
else:
    print("he didn't go to church")
