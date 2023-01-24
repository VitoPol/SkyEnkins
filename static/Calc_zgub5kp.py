expr = input()
l = len(expr)
num = []
priority = []
pr = 0
oper = []
N = ''

def sum(a, b):
    result = a + b
    return result
def subtract(a, b):
   result = a - b
   return result
 
def multiply(a, b):
   result = a * b
   return result
  
def divide(a, b):
   result = a / b
   return result

def max(list):
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return list.index(max)

for i in range(0, l):
    if expr[i] in ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',):
        N = N + expr[i]
    match expr[i]:
        case '(':
            pr += 10
        case ')':
            pr -= 10
        case '+':
            oper.append(expr[i])
            priority.append(1 + pr)
            num.append(float(N))
            N = ''
        case '-':
            oper.append(expr[i])
            priority.append(1 + pr)
            num.append(float(N))
            N = ''
        case '*':
            oper.append(expr[i])
            priority.append(2 + pr)
            num.append(float(N))
            N = ''
        case '/':
            oper.append(expr[i])
            priority.append(2 + pr)
            num.append(float(N))
            N = ''

num.append(float(N))

l = len(oper)

while(l > 0):
    i = max(priority)
    match oper[i]:
        case '+':
            num[i+1] = sum(num[i], num[i+1])
            oper.pop(i)
            num.pop(i)
            priority.pop(i)
        case '-':
            num[i+1] = subtract(num[i], num[i+1])
            oper.pop(i)
            num.pop(i)
            priority.pop(i)
        case '*':
            num[i+1] = multiply(num[i], num[i+1])
            oper.pop(i)
            num.pop(i)
            priority.pop(i)
        case '/':
            num[i+1] = divide(num[i], num[i+1])
            oper.pop(i)
            num.pop(i)
            priority.pop(i)
    l -= 1
    

print(oper)
print(priority)
print(num)
