milk = "leite desnatado"
volume = 2.5
print(volume)
print(type(milk))
print(type(volume))


preparation1 = volume + 1
preparation2 = milk + "10"
print (preparation1)
print (preparation2)

life_cat = str(volume + 5)
print("o gato bebe " + milk + " e tem " + life_cat + " vidas")

print(f"o gato bebe {milk} e tem {life_cat} vidas " )

name = "Francisco"
age = 17
is_admin = True  # boolean true or false

# primitive types

print(is_admin)
print(type(is_admin))

# structural Types (collections)

animes = ["Dragon Ball", "Naruto", "Jojo", "Death Note"]
#             =>  0            1        2          3
#             <= -4           -3       -2         -1
print(animes)
print(type(animes))
print(animes[0])
print(animes[3])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]
print(list[0])
print(list[3])
print(list[-1])
print(list[-1][-1])
# para modificar algum elemento da lista
list[2] = False
list[-1][0] = "D"
print(list)
print(len(list)) # length

#tuple
tuple = ("A", 123, True)
print(type(tuple))
print(tuple[1])
 # a tuple é imutavel
#tuple[1] = 789
#print(tuple) # erro: tuple is immutable

# dict
dict = {}
print(dict)
print(type(dict))

dict = {
"name": "Francisco",
"age": 17,
"is_admin":True
}
print(dict["name"])
print(dict["age"])
print(dict["is_admin"])


