from random import choice
from numpy import array, dot, random

def etape(x):
    if (x < 0):
		return 0
    else:
		return 1

print("Porte-Logiqueser une porte logique: 'Et' 'Ou'(defaut) 'NonEt' 'NonOu'")
choix = raw_input()

Et = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 0),
    (array([1,0,1]), 0),
    (array([1,1,1]), 1),
]

Ou = [
    (array([0,0,1]), 0),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 1),
]

NonEt = [
    (array([0,0,1]), 1),
    (array([0,1,1]), 1),
    (array([1,0,1]), 1),
    (array([1,1,1]), 0),
]

NonOu = [
    (array([0,0,1]), 1),
    (array([0,1,1]), 0),
    (array([1,0,1]), 0),
    (array([1,1,1]), 0),
]

if choix == "Et":
	PorteLogique = Et
elif choix == "Ou":
	PorteLogique = Ou
elif choix == "NonEt":
	PorteLogique = NonEt
elif choix == "NonOu":
	PorteLogique = NonOu
else:
   PorteLogique = Ou

poid = random.rand(3)
eta = 0.2
boucle = 100

for i in xrange(boucle):
    x, expected = choice(PorteLogique)
    result = dot(poid, x)
    error = expected - etape(result)
    poid += eta * error * x

for x, _ in PorteLogique:
    result = dot(x, poid)
    print("{}: {} -> {}".format(x, result, etape(result)))
