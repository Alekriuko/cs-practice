limit = float(input())
n = int(input())
error_c = 0
count = 0
bal = 0
sumt = 0
maxt = float('-inf')
for i in range(n):
    r = input()
    if r == 'error':
        error_c +=1
    else:
        r = float(r)
        maxt = max(r, maxt)
        sumt +=r
        count +=1
        if r>limit:
            bal +=1
if count == 0:
    count = 1
print(n)
print(error_c)
print(bal)
print(f'{maxt:.1f}')
print(f'{(sumt/count):.1f}')
