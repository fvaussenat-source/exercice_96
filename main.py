class Voiture():
    def __init__(self, marque, prix, couleur):
        self.marque = marque
        self.prix = prix
        self.couleur = couleur

    def __str__(self):
        return f"Votre voiture est une {self.marque} {self.couleur} et coûte {self.prix}"

    def __repr__(self):
        return f"Votre voiture est une {self.marque} {self.couleur} et coûte {self.prix}"

super_voiture = Voiture("Lamborghini", 150000, "rouge")
print(super_voiture)