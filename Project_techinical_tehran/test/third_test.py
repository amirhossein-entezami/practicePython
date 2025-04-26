# barnamei benvisid ke yek add begire be milimeter bad bege on add chnd metre vo chnd santimetro o chand milimetere?

receive_user = int(input("Enter your number as milimeter: "))

# receive user is milimeter
meter = int(receive_user / 1000)
centimeter = int((receive_user - (meter * 1000)) / 10)
milimeter = int(receive_user - ((meter * 1000) + (centimeter * 10)))
print(f"{meter}-> meter, {centimeter} -> centimeter , {milimeter}-> milimeter")
