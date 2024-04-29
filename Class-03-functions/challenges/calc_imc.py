def my_imc(heighnt, weighnt):
    total = weighnt / (heighnt * heighnt) 
    return total

heighnt = float(input("digite sua altura(m)"))

weighnt = float(input("digite seu peso(k)"))
imc = my_imc(heighnt, weighnt)

print(f"Seu IMC é {imc:.2f}")