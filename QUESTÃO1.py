s=input('digite apenas aspas,chaves ou colchetes:')
w=['[',']','{','}','(',')']
ok=False
if s in w:
    print(True) 
    print(s)
else:
    print('letras n aceitas')    
    print(False)