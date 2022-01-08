delenec = int(input("Napíš delené číslo:"))
delitel = int(input("Napíš číslo, ktorým chceš deliť:"))
#Číslo musí byť celé = integer, keby chceme desatinné, je potrebné pred input namiesto int napísať float
podiel_celociselny = delenec // delitel
zvysok_po_deleni = delenec % delitel

print(f"Výsledok celočíslného delenia je {podiel_celociselny} a zvyšok je {zvysok_po_deleni}.")