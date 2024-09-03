import math

def yksikkohinta_per_neliometri(halkaisija_cm, hinta_euro):
    # Muutetaan halkaisija senttimetreistä metreiksi
    halkaisija_m = halkaisija_cm / 100

    # Lasketaan pizzan säde
    sade_m = halkaisija_m / 2

    pinta_ala_m2 = math.pi * sade_m ** 2

    yksikkohinta = hinta_euro / pinta_ala_m2

    return yksikkohinta

def main():

    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta euroina: "))

    halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
    hinta2 = float(input("Anna toisen pizzan hinta euroina: "))

    yksikkohinta1 = yksikkohinta_per_neliometri(halkaisija1, hinta1)
    yksikkohinta2 = yksikkohinta_per_neliometri(halkaisija2, hinta2)

    print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} euroa per neliömetri")
    print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} euroa per neliömetri")

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza tarjoaa paremman vastineen rahalle.")
    elif yksikkohinta1 > yksikkohinta2:
        print("Toinen pizza tarjoaa paremman vastineen rahalle.")
    else:
        print("Molemmilla pizzoilla on sama yksikköhinta.")


main()
