A_data = input("enter")
A1_reader = [A_data[i] for i in range(0, len(A_data), 1)] 
A2_directions = {'v': 'y-1', '^': 'y+1', '>': 'x+1', '<': 'x-1'}
A3_direction_reader = [A2_directions[char] for char in A1_reader] 
A4_list = []
#print(A1) #['v', '>', 'v', '<', 'v', 'v', '>', '>', '>', '<']
#print(A3) # ['y-1', 'x+1', 'y-1', 'x-1', 'y-1', 'y-1', 'x+1', 'x+1', 'x+1', 'x-1']
y, x = 0, 0
for A3 in A3_direction_reader:
    if A3_direction_reader == "y+1":
        y += 1
    elif A3_direction_reader == "y-1":
        y -= 1  
    elif A3_direction_reader == "x+1":
        x += 1
    elif A3_direction_reader == "x-1":
        x -= 1
    list.append((y, x)) 
#print (A4) [(-1, 0), (-1, 1), (-2, 1), (-2, 0), (-3, 0), (-4, 0), (-4, 1), (-4, 2), (-4, 3), (-4, 2)]
A5_visited_coordinates = len(set(list))
print (A5_visited_coordinates)
