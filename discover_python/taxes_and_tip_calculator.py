""" 
 Python Workshop price calculator program made by Josquin Gaillard.
 Taking input from users about price, taxes and tips and calculating the total.
"""

print "Welcome to the taxes and tip calculator!"
price = float(input("What is the price before tax? "))
tax = float(input("What are the taxes? (in %) "))
tip = float(input("What do you want to tip (in %) "))
total = price + (price * (tax/100)) + ((price + (price * (tax/100))) * (tip/100))
print "The price you need to pay is: $%f " % (total)
