import math

username = input("please input name: ")
print("username is " + username)

# BMI = weight / (height ** 2)
weight = input("please input weight: ")
height = input("please input height: ")

print("your BMI is " + str(float(weight) / math.pow(float(height), 2)))
