import math
def hundealter_berechnen(age):
    return age * 7

def neu_hundealter_berechnen(age):
    return 16 * math.log(age, 10) + 31

if __name__ == "__main__":
    name = input("Wie heißt Ihr Hund: ")
    alter = int(input("Wie alt ist Ihr Hund: "))
    hundealter = round(neu_hundealter_berechnen(alter), 2)
    print(f"Ihr Hund heißt {name} und ist {hundealter} Jahre alt")