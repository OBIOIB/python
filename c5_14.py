def plus(x,y):
    answer = x+y
    return answer
answer=plus(100,50)
print(f'足し算の答えは{answer}です')

hoge = plus
n = hoge(5,8)
print(f'足し算の答えは{n}です')
