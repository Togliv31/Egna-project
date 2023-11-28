def packa_upp(textrad : list):
    # En av outputsen ska vara vilka språk som finns
    språk = []
    for i in range(len(textrad)):
        # "textrad" är en lista med 4 strängar, då filen som läses in
        # har 4 rader. Varje rad ska delas upp i språket som är i början av
        # raden, och isolera de enskilda glosorna, som är det raden under
        # är till för.
        textrad[i] = textrad[i].replace("\n", "").replace(": ", ", ").split(", ")
        # Nedanstående 3 rader tar ut språken, som alltid är först i sin rad.
        save = textrad[i].pop(0)
        save = save.lower()
        språk.append(save)
        # Denna for-loop ska dela upp alla glosor som har mer än 1 svar,
        # som indentifieras av att det står "/" mellan alternativen
    for i in range(1, len(textrad)):
        for g in range(0, len(textrad[i])):
            textrad[i][g] = textrad[i][g].split("/")

    return textrad, språk

def para(lista : list, språk : list):
    # Den här funktionen omvandlar glosorna till formatet:
    # {"ord på svenska" : {"språk1" : "[ord på språk1]", "språk2" : "[ord på språk2]"}}
    # osv. för varje ord på svenska. Svaren är i listor för att kunna ha
    # flera svar på samma ord för samma språk
    spara = {}
    glosor = {}
    
    for g in range(len(lista[0])):
        for i in range(1, len(lista)):
            spara[språk[i]] = lista[i][g]
        glosor[lista[0][g]] = spara
        spara = {}
    return glosor

def radera(ta_bort : dict, glosor : dict):
    # Den här funktionen tar bort alla ord där svaret varit rätt
    for key, value in ta_bort.items():
        for m in value:
            del glosor[key][m]
            # Om ordet inte har några svar kvar (alltså alla har varit rätt)
            # så tas ordet bort från dictionaryn
            if glosor[key] == {}:
                del glosor[key]
    # då listor är mutable så behöver inget returneras

def välja_språk(språk : list):
    # Den här funktionen frågar användaren om den vill öva igenom alla språk,
    # och låter användaren välja vilka språk om den inte vill öva igenom alla.
    svar2 = ""
    ogiltigt_svar = True
    # Nedanstående rad finns för att göra så att printen två rader efter
    # skriver ut språken fint.
    alla_språk = ", ".join(språk)
    while ogiltigt_svar == True:
        # Frågar om användaren vill öva alla språk.
        svar = input(f"Tillgängliga språk: {alla_språk}\nVill du öva glosor på alla språk?\n").lower()
        # Om ja, bryt loopen, hoppa över resten av funktionen, den gör inget mer.
        if svar == "ja":
            break
        # Om nej, användaren får välja vilka språk.
        elif svar == "nej":
            while True:
                # Svaret bryts upp i en lista för att kolla att alla
                # angivna språk finns tillgängliga.
                svar2 = input("Vilka språk vill du öva?\n").lower().split(", ")
                for i in svar2:
                    # Kollar om alla språk finns tillgängliga.
                    if i not in språk:
                        # Om minst en av språken inte finns.
                        print('Något/några av språken du valde finns inte tillgängliga.\nOm du vill öva flera språk bör de separeras med ", ".')
                        break
                else:
                    ogiltigt_svar = False
                    break
        else:
            # Om svaret inte är giltigt.
            print("Du måste svara ja/nej.")
    return svar2

def ta_bort_onödiga(glosor : dict, p : list):
    # Som namnet antyder tar den här funktionen bort glosor som användaren
    # valt att inte öva denna gång programmet körs, samt tomma glosor.
    ta_bort = {}
    spara = []
    for k, v in glosor.items():
        for a, b in v.items():
            # Kollar om någon av glosorna har en nyckel eller värde
            # som användaren valt att exkludera. Nyckeln sparas
            # (oavsett om nyckeln eller värdet identifierar
            # ifall det ska bort).
            for l in p:
                if l in b or l == a:
                    spara.append(a)
        if len(spara) > 0:
            # Tar bort alla dubletter.
            spara = list(set(spara))
            ta_bort[k] = spara
            spara = []
    for x, y in ta_bort.items():
        for i in y:
            # Tar bort den nyckeln för glosan. Om huvudnyckeln
            # (ordet på svenska) har en tom value tas den bort.
            del glosor[x][i]
            if glosor[x] == {}:
                del glosor[x]

onödiga = [""]
första_gången = True
är_rätt = False
ta_bort = {}
rätt = 0
fel = 0
glosor = {}
temp = [] # temp står för temporär

svar = open("Random Projekt/Glosprogram/Glosor.txt", "r", encoding="utf-8")

y = svar.readlines()

y, språk = packa_upp(y)

glosor = para(y, språk)

ha_kvar_språk = välja_språk(språk)

# Fråga till Hampus: Jag tycker att nedanstående for-loop inte bör vara i en
# funktion, håller du med om det?

# len(ha_kvar_språk) = 0 om man svarat ja på att öva alla språk.
if len(ha_kvar_språk) > 0:
    for u in språk:
        # Då man returnerat vilka språk som ska stanna, så indentifieras
        # alla språk som ska bort, och sedan tas dem bort.
        if u not in ha_kvar_språk:
            onödiga.append(u)

ta_bort_onödiga(glosor, onödiga)

while len(glosor) > 0:
    # a är ordet på svenska, b är dictionaryn med svaren
    for a, b in glosor.items():
        # key är språket på svaret, value är svaret
        for key, value in b.items():
            # ex.: "Vad är "sovrum" på spanska?"
            svar = input(f"Vad är \"{a}\" på {key}?\n").lower()
            # Det är "in" istället för "==" p.g.a. att ett ord kan ha
            # fler än ett svar. Då blir de olika svaren i en lista.
            # Om ordet bara har ett svar på ett av språken ligger
            # svaret i en lista där den är det enda elementet.
            if svar in value:
                print("Rätt!")
                är_rätt = True
                # temp sparar språket för svaret, så att den senare kan tas bort.
                temp.append(key)
                # Programmet ska inte ge 1 "poäng" på något som man tidigare
                # har haft fel på, därför kan man bara få poäng första rundan.
                if första_gången == True:
                    rätt += 1
            else:
                print(f"Fel! Rätt svar var:", ", ".join(value))
                # Kan också bara få "felpoäng" första gången. Ska ge en
                # överblick över hur väl man kan glosorna.
                if första_gången == True:
                    fel += 1
        # Om någon av svaren var rätt så läggs de till här, annars händer inget.
        if är_rätt == True:
            ta_bort[a] = temp
            temp = []
        # Återställer variabeln är_rätt
        är_rätt = False

    # Alla rätta glosor tas bort så att loopen kan gå iterera igen med endast
    # de fel svaren.
    radera(ta_bort, glosor)

    ta_bort = {}
    första_gången = False
    # Printar en tom rad. sep är tom rad som default, så antingen skriver jag
    # print("\n", sep= "") eller så skriver jag som det står, som jag tyckte
    # var lättare
    print("")

# Jag tycker att denna del förklarar sig själv.
if fel == 0:
    print("Du fick alla rätt!")
else:
    print(f"Du fick {rätt} rätt och {fel} fel.")