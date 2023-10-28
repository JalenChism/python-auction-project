def item_listing():
  item_name = input("Hello what item would you like to purchase?: ")
  return item_name
  
def bidding_process():
  listed_price = input("How much is the item?: $")

  print("\nThe price is: $", listed_price)

  bid_amount = input("How much would you like to bid?: $")

  while(int(bid_amount) >= 0):
    if(listed_price <= bid_amount):
      print("\nYOU HAVE WON THE BID!\nYou have 24 hours to pay the seller.")
    receipt()
    return bid_amount
    
    if(listed_price > bid_amount):
      print("YOu list the bid")
      choice = input("Would you like to bid again? 1 for Yes, 2 for No: ")

      if(choice == 1):
        bid_amount = input("How much would you like to bid?: $")

      if(choice ==2):
        break
  return bid_amount

  
def receipt():
  first_name = input("\nPlease Enter your first name: ")
  
  last_name = input("\nPlease Enter your last name: ")
  
  address = input("\nPlease Enter your address: ")
  
  city = input("\nPlease Enter your city: ")
  
  state = input("\nPlease Enter your state: ")
  
  zip_code = input("\nPlease Enter your zip code: ")
  
  print("Receipt:\n", first_name, last_name, "\n", address, "\n", city, state, zip_code)
  return


item_name = item_listing()
result = bidding_process()


print("\n Item: ",item_name)
print("\nTotal: $",result)