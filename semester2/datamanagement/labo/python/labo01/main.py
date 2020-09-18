from repositories.CategorieRepository import CategorieRepository
from services import CategorieServices
from services import KlantServices
#print(CategorieRepository.read_all())

#print(CategorieServices.print_all_categories())

# print(CategorieServices.print_details_categorie(4))
# print(CategorieServices.print_details_categorie(912))
# print(CategorieServices.print_details_categorie())

print("Kies een optie: Kies een optie: R=Read, S=Search, X=Exit \n\
-----------------------------------------------------")
choice = ""

while(choice.upper() != 'X'):
    choice = input("Jouw optie[R Klant, S Klant] = ")
    if choice[0].upper() == 'R':
        if choice [2:].lower() == 'klant':
            print(KlantServices.print_all_klanten())
        elif choice[2:].lower() == 'categorie':
            print(CategorieServices.print_all_categories())
    elif choice[0].upper() == 'S':
        nummer = input("Geef een nummer: ")
        try:
            nummer = int(nummer)
        except ValueError as e:
            print("Geef een getal in")
            continue

        if choice[2:].lower() == 'klant':
            print(KlantServices.print_details_klant(nummer))
        elif choice[2:].lower() == 'categorie':
            print(CategorieServices.print_details_categorie(nummer))

        
        



