# Aufgabe 1:
# while 1/ while true erzeugt eine Endlosschleife

# Aufgabe 2:
# Mit Moduklen rein theoretisch so wie in Word
# Oder falls Sie Variablen in nem print meinen dann
# print("text" +var+ "text")
# print("text", var, "text")
# print(f"text {var} text")

# Aufgabe 3
"""
print("Willkomen beim BMI Rechner")
groesse = int(input("Ihre Grße in cm: "))
gewicht = int(input("Ihr Gewicht in kg: "))
BMI = round(gewicht / ((groesse/100)**2), 1)

print("Ihr BMI ist: ", BMI)
print("\nVielen Dank für Ihr Vertrauen!!")
"""

# Aufgabe 4
"""
print("Willkommen beim Binärrechner")
binaer = input("Bitte geben Sie eine Binärzahl ein: ")
print("Ihre Dezimalzahl ist", int(binaer, 2))
"""

# Aufgabe 5
"""
print("Willkomen beim Kryptographie-Tool")
text = input("Text eingeben: ")
shift_factor = 1
encrypted_text = ""
for char in text.upper():
    char_number = ord(char)
    char_shifted_number = ((char_number - 65) + shift_factor) % 24
    shifted_char = chr(char_shifted_number + 65)  
    encrypted_text += shifted_char

print("Verschluesselt: ", encrypted_text)
"""

# Aufgabe 6
"""
print("Willkommen beim Oktalrechner")
octal = input("Oktalzahl eingeben: ")
print("Dezimalzahl: ", int(octal, 8))
print("Vielen Dank")
"""
