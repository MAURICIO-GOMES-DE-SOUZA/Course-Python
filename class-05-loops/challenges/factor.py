# crie uma funçao que receba um numero como parametro e calcule
# seu fatorial
def factor(num):
    total = 1
    # while num > 0:
    #     total *= num
    #     num -= 1
    for value in range(num, 1, -1):
        total *= value  
        
    return total 
print(factor(5))

def factor_r(num):
    if num == 1:
        return 1
    
    return num * factor_r(num -1)
 