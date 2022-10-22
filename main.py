#Weight_Converter_Program
#Developed using Python
#Created by Cephas Cardozo

#welcome_print
print("Weight Converter Program\nBy Cephas Cardozo\n")

#variables
unit_value = 0.45
user_w = int(input("Whats your weight? : "))
or_opt = input("Is it (L)bs or (K)gs : ").upper()

#conditionals
if or_opt == "K":
  print(f"/nYou'r weight is {user_w * unit_value} pounds")
elif or_opt == "L":
  print(f"/nYou'r weight is {user_w / unit_value} kilograms")
else:
  print("An ERROR occured!")
#end_of_code