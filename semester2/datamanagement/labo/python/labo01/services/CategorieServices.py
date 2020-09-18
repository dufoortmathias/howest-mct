from repositories.CategorieRepository import CategorieRepository
from models.Categorie import Categorie
from tabulate import tabulate

def print_all_categories():
    table = []
    for cat in CategorieRepository.read_all():
        table.append([cat.categorienummer, cat.categorienaam, cat.beschrijving])
    return tabulate(table)

def print_details_categorie(categorienummer=-1):
    if not categorienummer:
        return f"Ongeldig categorienummer: {categorienummer}"
    if categorienummer == -1:
        return f"Geen categorienummer gespecifieerd"
    result = CategorieRepository.details(categorienummer)
    if result is None:
        print(f"Categorie {categorienummer} is niet gevonden.")
    else:
        table = []
        table.append([result.categorienummer, result.categorienaam, result.beschrijving])
        print(tabulate(table, headers=["Categorienummer", "Naam", "Beschrijving"]))
    return result

    
