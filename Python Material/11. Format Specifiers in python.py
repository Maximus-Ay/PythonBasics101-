'''
    FORMAT SPECIFIERS IN PYTHON
    => In the context of f strings that we have been using right from the onset, 
       allow us to format values based on what we call flags.
    => These flags have specific significance depending on what you wish to do with them.
    => The format with them include: {value: flags} 

'''

#Example: Let's say we have 2 floating point numbers and we
# will make them have the number of decimal points we want

price = 3.1415
price2 = 56.789272
price3 = 100000000.56276

print(f"price1 = {price:.2f}FCFA")  # .2f is a flag that means that make the number have only 2 decimal places

print(f"price1 = {price:10}") # This means that the output should the space of 10 characters

print(f"price1 = {price:010}") # All the 10 spaces will have 0's

print(f"price1 = {price:<10}") # Left justify a value

print(f"price1 = {price:>10}") # right justify a value

print(f"price1 = {price:^10}") # center align a value

print(f"price1 = {price:+}") # preceed the number with a positive sign

print(f"price2 = {price2:-}") # preceed the number with a negative sign

print(f"price3 = {price3:,}") # A thouand seperator




