import time

def aufgabe1():
    print("Zugangskontrolle")
    print("----------------")

    for i in range(30, 0, -1):
        print(f"Noch {i} Parkplaetze verfuegbar")
        print("Bitte einfahren\n")
        time.sleep(0.5)
        print("\n - Signal Zugangskontrolle -")
    
    print("Kein freier Platz mehr verfuegbar")
    
def aufgabe2():
    print("Zugangskontrolle")
    print("----------------")

    counter = 30
    while counter > 0:
        print(f"Noch {counter} Parkplaetze verfuegbar")
        print("Bitte einfahren\n")
        time.sleep(0.5)
        print("\n - Signal Zugangskontrolle -")
        counter -= 1
    
    print("Kein freier Platz mehr verfuegbar")
    
def aufgabe3(n):
    for i in range(0, n, 2):
        print(i)

def aufgabe4(n):
    for i, j in zip(range(0, n, 2), range(n, 0, -1)):
        print(i, "||", j)

def aufgabe5(n: int, x: float):
    for i in range(n+1):
        res = 0
        for j in range(i+1):
            res += x**j
        print(res)



if __name__ == "__main__":
    aufgabe5(5, 15.1)
    