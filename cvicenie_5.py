roky = int(input('Koľko máš rokov?: '))
mesiace = int(input('Koľko mesiacov prešlo od tvojich narodenín?: '))

# Vypočítame počet dní 
dni = roky * 365 + mesiace * 30
print('počet dní =', dni)

# Vypočítame počet sekúnd
sekundy = dni*24*3600
print('počet sekúnd =', sekundy)
print('zaokrúhlené sekundy =', round(sekundy, -6))