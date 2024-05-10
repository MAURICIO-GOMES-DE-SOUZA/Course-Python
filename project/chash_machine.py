class Bank_account:
  
  def __init__(self, balance = 0):
    self.__balance = balance
    self.__file = "project/files/transactions.txt"
    self.__transaction = []
    self.__load_transactions()
  
  def check_statement(self):
    print("======= Extrato =====")
  
    for transaction in self.__transaction:
      print(f"{transaction[0]}: {transaction[1]}")

    print("=====================")
    print(f"Saldo (=): {self.__balance}")
    print("======================")

  def __load_transactions(self):
    try:
      with open(self.__file, "r") as file:
        for line in file:
          transaction, amount =  line.strip().split(", ")
          amount = float(amount)

          self.__transaction.append((transaction, amount))

          if transaction == "Deposito (+)":
            self.__balance += amount
          elif transaction == "Saque (-)":
            self.__balance -= amount
    except:
      print("Algo deu errado em abrir o arquivo!")
      pass          

  def deposit(self, amount):
    self.__balance += amount


    try:
      with open(self.__file, "a") as file:
        file.write(f"Deposito (+), {amount}\n")
        self.__transaction.append(("deposito (+)", amount))
    except:
      print("Algo deu errado em abrir o arquivo!")
      pass

    print(f"Deposito de R${amount} realizado!") 


  def withdraw(self, amount):
    if amount == 0:
      return print("Saque deve ser maior que zero!")
    if amount <= self.__balance:
      self.__balance -= amount
      try:
        with open(self.__file, "a") as file:
          file.write(f"saque (-), {amount}\n")
          self.__transaction.append(("saque (-)", amount))
      except:
        print("Algo deu errado em abrir o arquivo!")
        pass

      print(f"Saque de R${amount} realizado!") 
    else:
      print("Saldo insuficiente!")
    #eii acessa o meu arquivo tbm
    #\\172.16.72.47 aperta windows+R e cola esse ip ahí com essas contrabarra do jeito que está ahí..

     # deu certo nao bixo cheguei num negocio la estranho 
# o que faz depois pra acessar

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
      account.check_statement()
     elif option == "2":
      amount = float(input("Digite o valor para depositar:"))
      account.deposit(amount)
     elif option == "3":
      amount = float(input("Digite o valor para saque:"))
      account.withdraw(amount)     
     elif option == "4":
       print("Progama encerrado!\n")
       break
     else:
       print("Opçao inválida!")  
     


   