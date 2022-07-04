class golf:
    "a golfing score class"
    def __init__(self,hole, score, par):
        self.hole = hole
        self.par = par
def evaluateAndDisplayScore():
    global results
    global par
    global hole
    results = "blank"
    if score < par:
        results = "Under par"
    elif score > par:
        results = "Over par"
    else:
        results = "At Par"
    print("You scored", results, "on hole #",hole)
score = 0
hole1=golf(1, score, 3)
hole2=golf(2, score, 4)
hole3=golf(3, score, 5)
enterHole = int(input("Enter hole number: "))
if enterHole == 1:
    hole = 1
    score = int(input("Enter score: "))
    par = hole1.par
    evaluateAndDisplayScore()
elif enterHole == 2:
    hole = 2
    score = int(input("Enter score: "))
    par = hole2.par
    evaluateAndDisplayScore()
elif enterHole == 3:
    hole = 3
    score = int(input("Enter score: "))
    par = hole3.par
    evaluateAndDisplayScore()
else:
    print("Invalid hole number")
    exit()