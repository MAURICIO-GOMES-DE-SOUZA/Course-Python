# conditionals

age = 71
cnh = True

if age >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

    
if age >= 18 and cnh:
    print("Pode dirigir")
else:
    print("Nao pode dirigir")

if age >= 18 and age < 70:
    print("Voto obrigatorio")

elif age < 16:
    print("Nao pode votar") 
else:   
    print("Voto facultativo")    
    
try:
    print(2/"a") 
except ZeroDivisionError:
    print("Nao pode dividir por zero!")
except TypeError:
    print("Formato invalido!")
except:
    print("Erro!")
finally:
    print("Fim da requisiçao!")

    print("running!")

    
