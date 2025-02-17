import os

print('create `number1`, `number2`, `operation` files')
for f in os.listdir('.'):
    if f == 'number1':
        n1 = int(open(f, 'r').readline().strip())
for f in os.listdir('.'):
    if f == 'number2':
        n2 = int(open(f, 'r').readline().strip())
for f in os.listdir('.'):
    if f == 'operation':
        op = open(f, 'r').readline().strip()
print(n1, n2, op)
