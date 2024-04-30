# criar um progama que receba duas  notas do aluno faça uma funçao que calcule a 
# sua media e por fim apresente na tela se o aluno foi aprovado ( media7 )
try:
    student_grade1 = float(input("Nota1: "))
    student_grade2 = float(input("Nota2: "))

    def calc_avg(grade1, grade2):
      return  (grade1 + grade2) / 2
    

    avg  = round(calc_avg(student_grade1, student_grade2), 1)

    if avg >= 7:
        print(f"Aprovado com {avg}")
    else:
        print(f"Reprovado com {avg}")
    
except ValueError:
 print("Valor invalido!")
except:
    print("Erro na operaçao!")         