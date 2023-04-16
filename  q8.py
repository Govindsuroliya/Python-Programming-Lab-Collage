n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

if n == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c