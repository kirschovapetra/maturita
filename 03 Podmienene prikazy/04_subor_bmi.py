"""
V textovom súbore máme zapísané hmotnosti a výšky žiakov triedy. V jednom riadku je informácia
o jednom žiakovi v tvare: hmotnosť v kg a výška v m. Napíšte program, ktorý vypočíta BMI index každého
žiaka. BMI  je telesný hmotnostný index, ktorý sa vypočíta ako podiel hmotnosti v kilogramoch a výšky
v metroch na druhú.
o BMI<18,5 – podváha
o 18,5<=BMI<25 – normálna hmotnosť
o 25<=BMI<30 – nadváha
o BMI>30 – obezita
"""

subor = open("04_subor_bmi.txt", "r")
riadky = subor.readlines()

for riadok in riadky:
    riadok_bez_enteru = riadok[:-1]  # alebo riadok.rstrip()
    riadok_pole = riadok_bez_enteru.split(" ") # rozdeli sa na medzeri na pole s 2 cislami
    hmotnost = float(riadok_pole[0])
    vyska = float(riadok_pole[1])

    #bmi
    bmi = hmotnost / (vyska**2)
    if bmi < 18.5:
        vysledok = "podváha"
    elif bmi < 25:
        vysledok = "normálna hmotnosť"
    elif bmi < 30:
        vysledok = "nadváha"
    else:
        vysledok = "obezita"

    print("Hmotnost:", hmotnost, " Vyska:", vyska, " BMI:", bmi, vysledok)
