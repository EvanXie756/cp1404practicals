name = input("Enter name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.readline().strip()
in_file.close()
print(f"hi {name}")

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
result = number1 + number2
print(result)

total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
print(total)
