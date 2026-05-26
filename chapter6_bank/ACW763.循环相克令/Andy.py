a,b=input().split();w={('Hunter','Gun'),('Bear','Hunter'),('Gun','Bear')}
if a==b:print('Tie')
elif(a,b)in w:print('Player1')
else:print('Player2')
