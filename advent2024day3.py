with open('data.txt', 'r') as file: 
    textfile= file.read()
    textfile1 = textfile.split('\n') 
print(textfile1)
#part1
data = [x.split(')')[0] for x1 in textfile1 for x in x1.split('mul(')[1:]] # ['"xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"']
mul_data = [x for x in data if all(i.isdigit() for i in x.split(','))] # ['2,4', '5,5', '32,64](', '11,8', '8,5']
values = [int(x.split(',')[0]) * int(x.split(',')[1]) for x in mul_data] # ['2,4', '5,5', '11,8', '8,5']
total = sum(values)
print(total)
