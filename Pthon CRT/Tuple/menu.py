menu=("manchurian","dragon chicken","chicken magestic","biryanis")
price=(100,200,170,350)
print("Menu card:")
print(menu)
n=int(input("Enter the number of words:"))
i=1
j=1
total=0
while(i<=n):
    word=input("Enter the word of food:")
    index=menu.index(word)
    print(f"{word}-{price[index]}")
    i+=1
m = int(input("Enter the number of food items you want to order: "))
while j <= m:
    food = input(f"\nEnter name of food item: ")
    if food in menu:
        qty = int(input(f"Enter quantity for {food.title()}: "))
        index = menu.index(food)
        item_price = price[index] * qty
        print(f"{food.title()} x {qty} = ₹{item_price}")
        total += item_price
    else:
        print("Sorry, item not available in the menu.")
    j += 1
print("\n--- Billing Information ---")
phone = input("Enter your phone number: ")
feedback = input("Please provide your feedback: ")
tip = float(input("Enter tip amount (₹): "))

gst = total * 0.18
final_amount = total + gst + tip

print("--- Final Bill Summary ---")
print(f"Phone Number: {phone}")
print(f"Food Bill: ₹{total}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Tip: ₹{tip}")
print(f"Total Amount to Pay: ₹{final_amount}")
print(f"Feedback: {feedback}")
print("Thank you for your order...!")
