n = int(input())
prob = input()
index = [0] * n

for i in range(n):
    index[i] = int(input())
    
stack = []

for j in prob:
    if "A" <= j <= "Z":
        stack.append(index[ord(j) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()
        
        if j == "+":
            stack.append(a + b)
        elif j == "-":
            stack.append(a - b)
        elif j == "*":
            stack.append(a * b)
        elif j == "/":
            stack.append(a / b)

print("%.2f" % stack[0])