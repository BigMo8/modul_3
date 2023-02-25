lista_zakupow = {
    "warzywniak": ("marchew", "groch"),
    "piekarnia" : "bułka",
    "kiosk":"gazeta",
    "papiernik":"bibulka"
}
print (lista_zakupow)

for shops,products in lista_zakupow.items():
    print ("Idę do", shops, "i kupuję tam:", products)
print ("łączanie kupuję tam:", len(products), "rzeczy")

numbers_chosen = ([])
for numbers in range (1,50):
    if numbers % 5 == 0:
            numbers_chosen.append(numbers)
print (numbers_chosen)

cubes=[]
for numbers in numbers_chosen:
    cubes.append(numbers*numbers*numbers)
print(cubes)

squares=[]
for numbers in numbers_chosen:
    squares.append(numbers*numbers)
print(squares)

print("hello Master!")
print("Hello Coworker!")