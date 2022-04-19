# Exercise - Pizza order 
print("Welcome to Mario's Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L. ")

if size == "S":
  S = 15
  print("That will be $15!")
if size == "M":
  M = 20
  print("That will be $20!")
if size == "L":
  L = 25
  print("That will be $25!")

add_pepperoni = input("Do you want pepperoni? Y or N ")
pepperoni_small = 2
pepperoni_medium_large = 3
if add_pepperoni == "Y":
  if size == "S":
    print(f"That will be ${S + pepperoni_small}.") 
  if size == "M" or "L":
    print(f"That will be ${(M or L) + pepperoni_medium_large}.")

extra_cheese = input("Do you want extra cheese? Y or N ")
any_size_cheese = 1
if extra_cheese == "Y":
  if size == "S":
    if add_pepperoni == "Y":
      print(f"That will be ${S + pepperoni_small + any_size_cheese}.")
    else:
      print(f"That will be ${S + any_size_cheese}.")
  if size == "M" or "L":
    if add_pepperoni == "Y":
      print(f"That will be ${M or L + pepperoni_medium_large + any_size_cheese}.")
    else:
      print(f"That will be ${M or L + any_size_cheese}.")
else:
  print("Goodbyeee!")

          