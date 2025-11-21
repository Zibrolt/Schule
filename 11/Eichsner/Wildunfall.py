class Wildunfall:

    def __init__(self):
        pass
    
    def main(self):
        stop_dist = self.calcStopDistance()
        
        print(f"Weg bis zum Hindernis: {self.dist}")
        print(f"Anhalteweg: {stop_dist}")

        if stop_dist < self.dist:
            print("Glueck gehabt!!")
        else:
            print("CRASH!!")



    def calcStopDistance(self):
        self.eingabe()
        react_dist = self.calcReactionDistance(self.vel, self.react)
        break_dist = self.calcBreakDistance(self.vel, self.delay)
        return react_dist + break_dist

    def calcBreakDistance(self, vel, delay):
        return vel**2 / (2 * delay)
    
    def calcReactionDistance(self, vel, react):
        return vel * react

    def eingabe(self):
        self.vel = float(input("Geben Sie die Geschwindigkeit an: "))/3.6
        self.dist = int(input("Geben Sie die Distanz ein: "))
        self.react = int(input("Geben Sie die Reaktionsgeschwindigkeit ein: "))
        print("Die Verzögerungswerte zu folgenden Situationen sind vorhanden: \n\n")
        print("1: Nasser Asphalt\n2: Nasser Beton\n3: Trockener Asphalt\n4: Trockener Beton")
        self.choice = int(input("Bitte geben Sie einen Menuepunkt ein: "))
        match(self.choice):
            case 1: self.delay = 3
            case 2: self.delay = 5
            case 3: self.delay = 7
            case 4: self.delay = 9
            case _: raise Exception("No Valid Argument")

if __name__ == "__main__":
    wildunfall = Wildunfall()
    wildunfall.main()