class Bank_account:
  
  def __init__(self, balance = 0):
    self.__balance = balance
    self.__file = "project/files/transactions.txt"

  def deposit(self, amount):
    self.__balance += amount
    try:
      with open(self.__file, "a") as file:
        file.write(f"Deposito (+), {amount}\n")
    except:
      print("Algo deu errado em abrir o arquivo!")
      pass

    print(f"Deposito de R${amount} realizado!")    

account = Bank_account()
wating_menu = False #flag
while True:
     if wating_menu == True:
       input("\n Pressione Enter para seguir...")

    #  print("\033[H\033[J") # terminal clear
     print("\033c", end="") # terminal clear
     wating_menu = True


     print('''
    === Automated Teller Machine ===
      [1] Ver extrato  
      [2] Fazer o depósito 
      [3] Fazer saque 
      [4] Sair
    ================================ 
      ''')
     option = input("\bEscolha uma opçao: ")
     print("")
    


     if option == "1":
      print("Extrato")
     elif option == "2":
      amount = float(input("Digite o valor para depositar:"))
      account.deposit(amount)

      print("Deposito")
     elif option == "3":
       print("Saque")
     elif option == "4":
       print("Progama encerrado!\n")
       break
     else:
       print("Opçao inválida!")  
     


   