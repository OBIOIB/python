p1 ={'映画','散歩','ゲーム','写真','読書'}
p2 ={'ゲーム','散歩','料理','天体観測','登山'}
input('心の準備ができたらEnterキーを押してください')
print(f'二人の相性度は{len(p1 & p2)/len(p1 | p2)*100:.1f}%')
