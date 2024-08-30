# Python function that calculates the final price after applying a discount:

def calculate_discount(price, discount_percent):
    
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
       
        # Calculate the final price after discount
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        
        # Return the original price if discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Print the final price
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")

except ValueError:
    print("Please enter valid numerical values for the price and discount percentage.")
