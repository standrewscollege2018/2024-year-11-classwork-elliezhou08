''' take in a num and double it'''

# take input as a float print output (i dont like commenting)



try:
    coolnum = float(input("number: "))
except ValueError:
    print("i said a NUMBER (idiot)")

print(coolnum*2)
