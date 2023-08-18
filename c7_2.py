text = input('何を記録しますか?>>')
with open('duary.txt','a') as file:
    file.write(text + '\n')
