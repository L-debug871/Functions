sequence = []

def is_valid(num):
    return num.isdigit() or num.startwith('-') and num[1:].isdigit()

def even_num(num):
    return int(num)%2 ==0

while True:
    number = input("Enter a number (or 'DONE' to End):\n")
    if number == "DONE":
        break
    if is_valid(number):
        number = int(number)
        sequence.append(number)
        
pairs= 0
sum_of_pairs = 0

for i in range(len(sequence)-1):
    num_1 = sequence[i]
    num_2 = sequence[i+1]
    
    if even_num(num_1) and even_num(num_2):
        pairs+=1
        sum_of_pairs+= num_1+num_2
print(f"Number of pairs of adjacent even numbers: {pairs}.")
print(f"Sum of pairs of adjacent even numbers: {sum_of_pairs}.")