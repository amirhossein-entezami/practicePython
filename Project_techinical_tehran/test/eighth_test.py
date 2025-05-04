# barnamei benevisid ke gheymat mashid daryaft card age balaye 400m bashe 20% ezafe koneh dar gheyr insorat 10% ezafe koneh.

receive_user = int(input("Enter your price for car: "))

count = 400
if receive_user <= count:
    tax = int(receive_user * .2)
    print(f"Your car price is ${receive_user} and your tax is ${tax} and your payment is ${receive_user + tax}")
elif receive_user >= count:
    tax = int(receive_user * .1)
    print(f"Your car price is ${receive_user} and your tax is ${tax} and your payment is ${receive_user + tax}")
    