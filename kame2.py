import turtle 
t = turtle.Turtle() #インスタンスの生成
t.shape('turtle') #見た目を亀に
turtle.begin_fill()
for _ in range(5):
    t.forward(100)
    t.right(360/5*2)
turtle.end_fill()
t.home()
turtle.mainloop() #実行を監視
