import random
def F():
    i = random.randint(0,2)
    a = []
    if i == 0:
        a.extend([1,0,0])
    elif i == 1:
        a.extend([0,1,0])
    else:
        a.extend([0,0,1])
    chose =a[random.randint(0,2)]
    a.remove(chose)
    a.remove(0)
    chose = int(a[0])
    return chose
    
total = 100
list1=[]
for i in range(0,total):
    list1.append(F())
rate = 0
for get_prize in list1:
    if get_prize == 1:
        rate +=1
final_rate = rate/total
print(final_rate)