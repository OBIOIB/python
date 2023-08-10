import turtle 
t1 = turtle.Turtle() #インスタンスの生成
t1.shape('turtle') #見た目を亀に
t1.color('#00f')
t2 = turtle.Turtle() #インスタンスの生成
t2.shape('turtle') #見た目を亀に
t2.color('#f00')
def make_square(t):
    for i in range(4):
        t.forward(100)
        t.right(90)

def make_spiral(t):
    for i in range(36):
        make_square(t)
        t.right(10)

make_spiral(t1)
t2.right(5)
make_spiral(t2)
turtle.mainloop() #実行を監視
