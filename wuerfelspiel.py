import random #Importiert die Random-Bibliothek
import time #importiert die time-bib
SpielWiederholen = 0
while(SpielWiederholen == 0):

    Start = int(input("Gebe den Ratebereich an. Von:")) # Eingabeaufforderung der Variable, welche die niedrigst mögliche zufällige Zahl angibt
    Stopp = int(input("Bis:")) # Eingabeaufforderung der Variable, welche die höchst mögliche zufällige Zahl angibt

    #Eine Zufallszahl wird generiert und in der Variable "MeineZufallsZahl" abgespeichert
    MeineZufallsZahl = random.randrange(Start, Stopp)

    #Dem Benutzer wird mitgeteilt dass eine zufällige Zahl generiert wurde
    print("Ich habe mir eine zufällige Zahl ausgedacht zwischen",Start, "und", Stopp)
    Kondition = 0

    while(Kondition == 0):
        
        # Der Nutzer wird aufgefordert dass er eine Zahl eingeben soll
        Eingabe = input("Rate eine Zahl: ")
        if Eingabe.isnumeric() == False: #Die Eingabe wird auf Zahl kontrolliert. True/False
            print("Das ist keine ganze Zahl!", end="")
            time.sleep(3)
        else:
            EingabeInt = int(Eingabe)#Die Eingabe wird von str zu integer gewandelt
            if (EingabeInt > MeineZufallsZahl):
                print("Die Zahl",Eingabe,"ist zu groß!")
            if(EingabeInt < MeineZufallsZahl):
                print("Die Zahl",Eingabe,"ist zu klein!")
            if(EingabeInt == MeineZufallsZahl):
                print("Richtig, herzlichen Glückwunsch!")
                Kondition = 1 #Die Wiederholungs Kondition wird auf 1 gesetzt, die 2. Schleife(while) wird nicht wiederholt.
                Beenden = input("Willst du das Spiel nochmal spielen? (J)a oder (N)ein ").lower() #Eingabe wird in Kleinbuchstaben gewandelt
                #BeendenInt = int(Beenden)
                if(Beenden == "n"):
                    SpielWiederholen = 1 #Setze die SpielWiederholen Variable auf 1. Damit wird die 1. Schleife(while) unterbrochen
            