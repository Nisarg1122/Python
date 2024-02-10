amt = float(input("Enter Amount : "))
intr = float(input("Enter Intrest Rate : "))
tm = float(input("Enter Time (In Years) : "))

intrest = amt * intr * tm/100

print("Total Intrest Of",tm,"Years = ",intrest)