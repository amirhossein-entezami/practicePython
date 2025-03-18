""" barnamei benevisid ke ghad va vazn begire shakhes tode badani ro hesab mikone
age BMI kamtar mosavi 18 bod bege kambod vazn age bein 18.5 ta 24.5 bod bege
vzn salem age bein 24.5 ta 30 bod bege ezafe vazn bishtar az 30 khatr"""

height = int(input("Ghad khod ro vared konid(ex. 178): "))
weight = int(input("Vazn khod ro vared konid(ex. 90): "))

height = height / 100
BMI = weight / (height ** 2)
print(f"Shakhes tode badni shoma-> {BMI}")
if BMI <= 18:
    print("shoma kambod vazn darid!")
elif 18.5 <= BMI <= 24.5:
    print("shoma vazneton monasebe!")
elif 24.5 <= BMI <= 30:
    print("Shoma Ezafe Vazn darid!")
elif BMI >= 30:
    print("Warning! You are must be Died!!!!")
    