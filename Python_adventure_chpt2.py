drinks = ["chokolate","coffie","decadf"]
flavors = ["caramel","vanilla","peppermint","fruitmint","raspberry","plain"]
toppings = ["chocolate","cinnamon","caramel"]
print ("Valeriia CAFE menu")
print ("Onze drankjes")
print ("-------------")

# print (drinks)
i = 1
for d in drinks:
    print (i, d)
    i = i+1
drink = input ("Kies je drankje: ")
print ("Onze smaaktoepassingen")
print ("----------------------")  
i = 1   
for f in flavors:
    print (i, f)
    i = i + 1
flavor = input ("Kies je smaaktoepassingen: ")
print ("Onze toppings")
print ("-------------")
i = 1
for top in toppings:
    print (i, top)
    i = i + 1
topping = input ("Kies je topping: ")
