# barnamei ke 2 add bigire bege tashkil moraba midn ya na
receive_user_a = int(input("Enter your first zele: "))
receive_user_b = int(input("Enter your second zele: "))

if receive_user_a == receive_user_b:
    moraba = ((receive_user_a + receive_user_b) / 2) ** 2 - receive_user_a ** 2 / 4
    print(f"bale tashkil mishavad va add nahaii ine -> {moraba}")
else:
    print("na tashkil nemishe! ")
