Q = int(input())
Energia = 0
Golpe = 0

for i in range(Q):
	P = int(input())
	Energia += 5
	Golpe = P

if(Energia >= Golpe):
	print("Escolheu o seu destino!")		
else:
	print("Fez de mim o que eu sou!")
