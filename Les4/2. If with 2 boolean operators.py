leeftijdMeerderjarig = 18
bezitPaspoort = ['Ja', 'ja', 'yes', 'Yes', 'y', 'Y', 'j', 'J',]
while True:
    try:
        leeftijd = int(input("Geef je leeftijd: "))
    except ValueError:
        print("Voer een geldig getal in!")
    else:
        break
NederlandsPaspoort = input('Ben je in bezit van een Nederlands passpoort?: ')
if leeftijd > leeftijdMeerderjarig and  NederlandsPaspoort in bezitPaspoort :
    print('Gefeliciteerd, je mag stemmen!')
else:
    print('Je mag niet stemmen')