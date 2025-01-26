with open('data.txt', 'r') as file: 
    textfile= file.read()
    textfile1 = textfile.split('\n') # using ['71 73 74 76 78 80 77', '78 81 84 87 87'] as example

A1 = [tuple(map(int, a.split())) for a in textfile1]
A2 = [[A1[j][i] - A1[j][i + 1] for i in range(len(A1[j]) - 1)] for j in range(len(A1))]
A3 = [sublist for sublist in A2 if (all(x > 0 for x in sublist) or all(x < 0 for x in sublist)) and 0 not in sublist]
A4 = [sublist for sublist in A3 if all(abs(x) <= 3 for x in sublist)]
A5 = [[num <= 3 for num in A4[j]] for j in range(len(A4))]
A6 = sum(all(sublist) for sublist in A5)


B = [row for row in A2 if row not in A4]
B1 = [[abs(sum(pair)) for pair in zip(a, a[1:])] for a in B] 
B2 = [group for group in B1 if sum(1 for x in group if abs(x) > 3) == 1]
print(len(B2))
