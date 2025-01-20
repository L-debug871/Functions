sequence = []


def is_valid_number(num):
    return num.isdigit() or (num.startswith('-') and num[1::].isdigit())

def multiple_4(num):
    return int(num) % 4 == 0
   
while True:
    number = input("Enter a number (or 'DONE' to End):\n")
   
    if number == 'DONE':
        break
   
    if is_valid_number(number):
        number = int(number)
        sequence.append(number)
       
adjacent_pairs = 0
sum_of_pairs = 0

for i in range(len(sequence) - 1):
    num1 = sequence[i]
    num2 = sequence[i + 1]
   
    if multiple_4(num1) and multiple_4(num2):
        adjacent_pairs += 1
        sum_of_pairs += num1 + num2
       

print(adjacent_pairs)
print(sum_of_pairs)