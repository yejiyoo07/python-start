
print("test")

print(8 // 2 * (2 + 2))
print(8 // (2 * (2 + 2)))

평균속도 = 0.8
시간 = 110
print(평균속도 * 시간)


def print_list(a):
    for i in a:
        print(i)
  
def myLenReturnVer(a):
    count = 0
    for i in a:
        count = count + 1
    return count
        
def myLen(a):
    count = 0
    for i in a:
        count = count + 1
    print(count)
    
def myLen(a,b):
    count = 0
    countb = 0
    for i in a:
        count = count + 1
    for i in b:
        countb = countb + 1
    print(count + countb)
    
def myLen():
    print('nothing')  
    return 0 
    
def boy():
    print('boy')
    print('girl')
    
def quiz():
    ans = input('1 + 2 = ')
    return 1 + 2 == int(ans)

def gugudan():
    for i in [2,3,4,5,6,7,8,9]:
        first = i
    for j in [2,3,4,5,6,7,8,9]:
        second = j
    값 = first * second
    return 값
    
m = 2
for n in range(1,10):
    print(f'{m} * {n} = {m*n:3d}')
    
def gugudan():
    for m in range(2,10):
        for n in range(1,10):
            print(f'{m} * {n} = {m*n:2d}')