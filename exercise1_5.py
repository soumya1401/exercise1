import math
c=50
h=30
numbers = input("Enter numbers separating with comma:")
my_list= numbers.split(",")
my_list = list(my_list)
final_list=[]
for d in my_list:
    a = (2*c*int(d))%h
    q = math.sqrt(a)
    final_list.append(str(q))
print(','.join(final_list))
# with this program not getting required result