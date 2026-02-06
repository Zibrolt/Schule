import time
from abc import ABC, abstractmethod

class Zustand(ABC):

    @abstractmethod
    def entry(self):
        pass
    
    @abstractmethod
    def do(self):
        pass

    @abstractmethod
    def exit(self):
        pass

# Konkrete Zustaende
class ZustandZuHoch(Zustand):
    def entry(self):
        print("Kuehlung eingeschaltet")

    def do(self):
        print("Kuehlen...")
        return -0.1

    def exit(self):
        print("Kuehlung ausgeschaltet")

class ZustandIO(Zustand):
    def entry(self) -> None:
        print("Warten gestartet")

    def do(self) -> None:
        print("Warten...")
        return 0

    def exit(self) -> None:
        print("Warten beendet")

class ZustandZuNiedrig(Zustand):
    def entry(self): 
        print("Heizung eingeschaltet")

    def do(self): 
        print("Heizen...")
        return 0.1

    def exit(self): 
        print("Heizung ausgeschaltet")

class ZustandFehler(Zustand):

    def entry(self):
        print("FEHLER in der Temperatur")
    
    def do(self):
        raise Exception("Ungueltige Temperatur")
    
    def exit(self):
        return super().exit()
    
# Hauptklasse für die Regelung
class Raumluftregelung:
    def __init__(self, soll_temp): # 'soll_temp' ist der Parameter
        self.sollTemperatur=soll_temp
        self.istTemperatur= self.frage_istTemperatur()
        self.aktuellerZustand=ZustandIO()

    def wechselZustand(self, neuer_zustand):
        self.aktuellerZustand.exit()
        self.aktuellerZustand=neuer_zustand
        self.aktuellerZustand.entry()

    def starteRegelung(self):
        while True:
            self.pruefeTemperatur()
            try:
                self.istTemperatur += self.aktuellerZustand.do()
            except Exception as e:
                print(e)
                break
            self.istTemperatur = round(self.istTemperatur, 2)
            print(f"IST: {self.istTemperatur} || SOLL: {self.sollTemperatur}")
            time.sleep(0.2)

    def frage_istTemperatur(self):
        return float(input("Geben Sie die Temperatur ein: "))

    def pruefeTemperatur(self):

        if self.istTemperatur > 40 or self.istTemperatur < 0:
            self.wechselZustand(ZustandFehler())

        elif self.istTemperatur > self.sollTemperatur:
            self.wechselZustand(ZustandZuHoch())
        
        elif self.istTemperatur < self.sollTemperatur:
            self.wechselZustand(ZustandZuNiedrig())

        elif self.istTemperatur == self.sollTemperatur:
            self.wechselZustand(ZustandIO())


regelung=Raumluftregelung(soll_temp=22.0) # '22.0' ist das Argument
regelung.starteRegelung()