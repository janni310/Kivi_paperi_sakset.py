import random

pelit = 0
voitot = 0
tasapelit = 0



while True:
    omaValinta = input("Kivi, paperi vai sakset? (Lopeta lopettaa): ")
    omaValinta1 = omaValinta.lower()

    tietokone = random.randint(0, 2)

    if tietokone == 0:
        tietokone = "kivi"
    elif tietokone == 1:
        tietokone = "paperi"
    elif tietokone == 2:
        tietokone = "sakset"

    if omaValinta1 == tietokone:
        print("Sinä valitsit: ", omaValinta1)
        print("Tietokone valitsi: ", tietokone)
        print("Tasapeli!")
        pelit += 1
        tasapelit += 1

    elif omaValinta1 == "kivi" and tietokone == "paperi":
        print("Sinä valitsit: ", omaValinta1)
        print("Tietokone valitsi: ", tietokone)
        print("Hävisit!")
        pelit += 1

    elif omaValinta1 == "paperi" and tietokone == "kivi":
        print("Sinä valitsit: ", omaValinta1)
        print("Tietokone valitsi: ", tietokone)
        print("Voitit!")
        pelit += 1
        voitot += 1
        
    elif omaValinta1 == "kivi" and tietokone == "sakset":
        print("Sinä valitsit: ", omaValinta1)
        print("Tietokone valitsi: ", tietokone)
        print("Voitit!")
        pelit += 1
        voitot += 1
        
    elif omaValinta1 == "sakset" and tietokone == "paperi":
        print("Sinä valitsit: ", omaValinta1)
        print("Tietokone valitsi: ", tietokone)
        print("Voitit!")
        pelit += 1
        voitot += 1
        
    elif omaValinta1 == "sakset" and tietokone == "kivi":
        print("Sinä valitsit: ", omaValinta1)
        print("Tietokone valitsi: ", tietokone)
        print("Hävisit!")
        pelit += 1
        
    elif omaValinta1 == "paperi" and tietokone == "sakset":
        print("Sinä valitsit: ", omaValinta1)
        print("Tietokone valitsi: ", tietokone)
        print("Hävisit!")
        pelit += 1
        
    elif omaValinta1 == "lopeta":
        print("Pelasit", pelit, "kierrosta, joista voitit", voitot, "ja pelasit tasan", tasapelit, "peliä.")
        break
