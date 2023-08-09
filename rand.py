import random
"""
num = random.randint(5,10) #5~10の値をランダムに一個生成
print(num)
"""
dices =list()
count = int(input('何回振る?>>'))

for _ in range(count): #回す回数だけならforとinのあいだに_だけでもいいらしい
    dices.append(random.randint(1,6))
print(dices)
print(f'合計は{sum(dices)}でした')
