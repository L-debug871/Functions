Write a program called ‘testc.py’ that asks the user to enter a series of integer numbers, one per line, finishing with the word ‘DONE’. The program will count and sum up the number of adjacent pairs of values where the first number is a factor of the second number in the sequence.

Say, for example, the user enters the following series of numbers: 3, 2, 2, 1, 4, 4, 6. There are three pairs of adjacent values that meet the criterion: (2, 2), (1, 4) and (4, 4). Their sum is 17.

 

HINT: Given two integers a and b, a is a factor of b if b % a == 0.

 

Sample IO (The input from the user is shown in bold font – do not program this):

Enter a number (or 'DONE' to End):

3

Enter a number (or 'DONE' to End):

2

Enter a number (or 'DONE' to End):

2

Enter a number (or 'DONE' to End):

1

Enter a number (or 'DONE' to End):

4

Enter a number (or 'DONE' to End):

4

Enter a number (or 'DONE' to End):

6

Enter a number (or 'DONE' to End):

DONE

Number of adjacent pairs where the 1st number is a factor of the 2nd number: 3.

Sum of adjacent pairs where the 1st number is a factor of the 2nd number: 17.

 

Sample IO (The input from the user is shown in bold font – do not program this):

Enter a number (or 'DONE' to End):

24

Enter a number (or 'DONE' to End):

24

Enter a number (or 'DONE' to End):

24

Enter a number (or 'DONE' to End):

24

Enter a number (or 'DONE' to End):

DONE

Number of adjacent pairs where the 1st number is a factor of the 2nd number: 3.

Sum of adjacent pairs where the 1st number is a factor of the 2nd number: 96.