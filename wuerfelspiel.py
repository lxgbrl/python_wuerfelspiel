import random #Importiert die Random-Bibliothek
import time #importiert die time-bib
SpielWiederholen = 0
while(SpielWiederholen == 0):

    BereichStart = 0 # Eine Variable, welche die niedrigst mögliche zufällige Zahl angibt
    BereichStopp = 1000 # Eine Variable, welche die höchst mögliche zufällige Zahl angibt

    #Eine Zufallszahl wird generiert und in der Variable "MeineZufallsZahl" abgespeichert
    MeineZufallsZahl = random.randrange(BereichStart, BereichStopp)

    #Dem Benutzer wird mitgeteilt dass eine zufällige Zahl generiert wurde
    print("Ich habe mir eine zufällige Zahl ausgedacht")

    Kondition = 0

    while(Kondition == 0):
        
        # Der Nutzer wird aufgefordert dass er eine Zahl eingeben soll
        Eingabe = input("Rate eine Zahl: ")
        if Eingabe.isnumeric() == False:
            print("Das ist keine ganze Zahl!", end="")
            time.sleep(3)
        else:
            EingabeInt = int(Eingabe)
            if (EingabeInt > MeineZufallsZahl):
                print("Die Zahl",Eingabe,"ist zu groß!")
            if(EingabeInt < MeineZufallsZahl):
                print("Die Zahl",Eingabe,"ist zu klein!")
            if(EingabeInt == MeineZufallsZahl):
                print("Richtig, herzlichen Glückwunsch!")
                Kondition = 1
                print("Willst du das Spiel nochmal spielen? (J)a oder (N)ein ")
                SpielBeenden = input() #Es wird gefragt ob der Spielende das Spiel wiederholen möchte.            
                SpielBeendenAlsInt = int(SpielBeenden)
                if(SpielBeendenAlsInt == 1): #Wenn der Spieler ein "N" eingibt, dann....
                    SpielWiederholen = 1 #...Setze die SpielWiederholen Variable auf 1. Damit wird die Während-Wiederholung unterbrochen
            