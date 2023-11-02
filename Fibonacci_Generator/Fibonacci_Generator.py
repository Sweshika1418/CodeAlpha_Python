# Generating a Fibonacci Sequence using Generator in Python
def generateFibonacciSequence():
    x2 = 1
    x3 = 1
    while True:
        x1 = x2
        x2 = x3
        x3 = x1 + x2
        yield x1

y = generateFibonacciSequence()
# Here we are generating the first 20 fibanacci numbers
for i in range(20):
    print(next(y),end = ' ')
