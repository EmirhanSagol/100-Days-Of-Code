import os
import Art

dict_of_bid = {}
say_no = False
clear = lambda: os.system('cls')

print(Art.logo)

while not say_no:
  i_name = input("What is your name? ")
  dict_of_bid[i_name] = int(input("What is your bid? "))
  yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'. ")
  
  if yes_or_no == "no":
    max_value = max(dict_of_bid.values())
    for name in dict_of_bid:
      if dict_of_bid[name] == max_value:
        key_of_max_value = name
    print(f"The winner is {key_of_max_value} with a bid of {max_value}.")
    say_no = True
  elif yes_or_no == "yes":
    clear()

  
