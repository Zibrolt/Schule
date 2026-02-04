import time

if __name__ == "__main__":

    print("Zugangskontrolle")
    print("----------------")

    for i in range(30, 0, -1):
        print(f"Noch {i} Parkplaetze verfuegbar")
        print("Bitte einfahren\n")
        time.sleep(0.5)
        print("\n - Signal Zugangskontrolle -")
    
    print("Kein freier Platz mehr verfuegbar")