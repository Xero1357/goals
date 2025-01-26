with open('data.txt', 'r') as file: 
    textfile= file.read()
    textfile1 = textfile.split('\n') 

with open('data1.txt', 'r') as file: 
    textfile= file.read()
    textfile2 = textfile.split('\n') 

list1 = textfile1 # ['47|53', '97|13', '97|61']
list2 = textfile2 # ['75,47,61,53,29', '97,61,53,29,13']

list1A = [char.replace('|', ',') for char in textfile1] #['47,53', '97,13', '97,61']
list1B = [[x] for x in list1A] #[['47,53'], ['97,13'], ['97,61']]
list1C  = [tuple(map(int, char[0].split(','))) for char in list1B] #[(47, 53), (97, 13), (97, 61)]
#print (list1C)

list2A = [[x] for x in list2] #[['75,47,61,53,29'], ['97,61,53,29,13'], ['75,29,13'], ['75,97,47,61,53'], ['61,13,29'], ['97,13,75,29,47']]
list2B = [[int(num) for num in inner[0].split(',')] for inner in list2A]

combined = [[list1C[i] for i in range(len(list1C)) if all(str(x) in list2A[i1][0] for x in list1C[i])] for i1 in range(len(list2A))]
#print(combined)

C = [[(list2B[i].index(x[0]), list2B[i].index(x[1])) for x in b] for i, b in enumerate(combined)]
#print(C)
verifiedlists = [group if all(x[1] > x[0] for x in group) else [] for group in C]
print(verifiedlists)

verifiedlists2 = [a for a, b in zip(list2B, verifiedlists) if b]
#print(verifiedlists)

CenterValues_summed = sum(sublist[len(sublist) // 2] for sublist in verifiedlists2)
#print(CenterValues_summed)
