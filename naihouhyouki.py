#内包表記
ls = [ i for i in range(1,11)]
print(ls) #[1,2,3....10]
ls = [ i**2 for i in range(1,11)]
print(ls) #[1,4,9....100]

#サイコロを3回振ったときの目をリストにする
dices=[random.randint(1,6) for i in range(3)]
print(dices) #[4,2,6]
