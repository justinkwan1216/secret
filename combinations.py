from itertools import combinations
x=[[1,2,3],[1,4],[2,5]]
test_array=[1,2,3,5]
predict_number=4
all_combinations=[]
for i in range(len(test_array)):
    combinations_object = combinations(test_array, i)
    combinations_list = list(combinations_object)
    
    all_combinations += combinations_list
    


for each in all_combinations:
    #print("each")
    print(each)
    for element in x:
        if set(each).issubset(set(element)):
            print(element)
