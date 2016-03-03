Fonctionnement des primitives :

Chaque comportement dois se faire dans un fichier .py séparé.
Chaque comportement est une classe dérivant de LoopPrimitve ou de Primitive

Pour les LoopPrimitive, se referer à wave.py :
	- La fonction setup() est appelée une fois lorsque l'on lance la primitive, elle sert à initialiser le mouvement.
	- La fonction update() est appeler à intervalle régulier
	- La fonction teardown() est appelée lorsque l'on arrête la primitive, elle sert à terminer le mouvement
	- Pour plus d'info, cf la classe LoopPrimitive de la librairie pypot


Pour faire fonctionner ces primitives, il faut instancier cette classe et l'attacher au robot dans le fichier ../cherry.py
puis lancer cette primitive dans example.py ou via un notebook et example.ipynb