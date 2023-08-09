import random
count = 0
while c == True: 
    count += 1
n = random.randint(1,9999)
print(f'{count}:{n}')
if n == '7777':
     break
print(f'{count}回目に7777がでました!')
