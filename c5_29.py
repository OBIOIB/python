def eat(breakfast,lunch,dinner='カレー',*desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')

print('8月1日')
eat('トースト','パスタ','カレー','アイス','チョコ','カレー')

def sumof(*args):
    total=0
    for i in args:
        total += i
    return total
print(sumof())
print(sumof(3,5))
print(sum((3,5,7)))
