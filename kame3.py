import turtle 
t = turtle.Turtle() #インスタンスの生成
t.shape('turtle') #見た目を亀に
t.color('#00f')
t.forward(100) #向いている方向に100移動
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.penup()
t.home()
turtle.mainloop() #実行を監視
