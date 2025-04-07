"""barnamei benevisid ke yek add migire agr morabaee
kamel bod faktoreilsh ro hesab mikone!"""


"""Way 1"""

factorial = int(input("ye add verd konid morabee begiram faktoreyl bedam: "))
if factorial % 4 == 0 or factorial % 4 == 1:
    print("in addadi ke dadi morabee kamele!")
    for i in range(1, factorial):
        factorial *= i
    print("factorial in add barabar: ", factorial)
else:
    print("moraba nist!")
