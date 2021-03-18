result = []
total = 0
result2 = []
totalvat = 0
vat = 0

def vatadded():
    for i in result:
     global result2
     global totalvat
     result2.append(i*(23/100)+i)
     totalvat = totalvat + (i*(23/100))

    return totalvat

for a in range(1,100):
    numberEntered = int(input("Please enter a number "))

    if (numberEntered==-1):
           break

    total = total + numberEntered
        
    result.append(numberEntered)
    
vatadded()

total = total + totalvat

print("the sales figures entered were", result)
print("the sales figures with vat included", result2)
print("the total vat was", "%.2f" % round(totalvat,2))
print("the total price included vat", "%.2f" % round(total,2))
