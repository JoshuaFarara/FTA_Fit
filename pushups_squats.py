'''
Calculates pushups where the person does 10 push ups decrementing by 1 to one
and find the total number of push ups they have done by the end of the workout

'''

total_pushups = 0

for i in range(10, 0, -1):
    print("Doing", i, "pushups")
    total_pushups += i
    print("Total pushups done:", total_pushups)
#     print(i, total_pushups)
    
for i in range(1, 11, 1):
    total_pushups += i
    print(i, total_pushups)