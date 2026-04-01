def bonjour():
    return "Bonjour, le monde!"
if __name__ == "__main__":
    print(bonjour())

def calculer_remise(prix, taux):
    remise = prix * taux
    prix_final = prix - remise
    return prix_final
if __name__ == "__main__":
    prix = 100
    taux = 0.2
    print(calculer_remise(prix, taux))

def calculer_tva(prix, taux=0.20):
    tva = prix * taux
    prix_ttc = prix + tva
    return prix_ttc
if __name__ == "__main__":    prix = 100
print(calculer_tva(prix))
