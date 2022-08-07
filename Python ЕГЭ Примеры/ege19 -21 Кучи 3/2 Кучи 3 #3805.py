'''




3805

'''
# S – количество камней, с – текущий ход, m - количество ходов
def f(a,b,c,m):
    #1,3,5 ход левой стороны (Петя)
    #2,4,6 ход правой стороны (Ваня)
    if a+b<=20: return c%2==m%2
    if c==m: return 0

    h = [f(a-1,b,c+1,m), f(a,b-1,c+1,m),f((a+1)//2,b,c+1,m),f(a,(b+1)//2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for b in range(11,200):
    for m in range(1,5):
        if f(10,b,0,m) == 1: #1 это логическое да
            print(b,m)
            #if m == 2: #Первый ход Вани
            #if m == 3: print(b,m)#Второй ход Пети
            #if m == 4:  print(b,m) #Второй ход Вани
            break
