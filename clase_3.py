import sys
# print(sys.maxsize)
def is_primo(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i ==0:
            return False
    return True

for i in range(20):
    print(f"El numero {i} {is_primo(i)} \n")
