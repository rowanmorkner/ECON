

# n = int(input("Enter a number: "))

# for i in range(n):
#     if i % 2 == 0:
#         print(i * 'x')
#         print((n - i) * 'o')10
    

numbers = [5, 2, 5, 2, 2]
print("numbers 1:", numbers)
print(5 in numbers)
print(len(numbers))

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)



