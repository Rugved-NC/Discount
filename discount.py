price = float(input("Enter price: "))
discount = float(input("Enter discount %: "))

final_price = price - (price * discount / 100)

print(f"Final price: {final_price}")
