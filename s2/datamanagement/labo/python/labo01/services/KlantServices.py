from repositories.KlantRepository import KlantRepository
from models.Klant import Klant
from tabulate import tabulate


def print_all_klanten():
    table = []
    for klant in KlantRepository.read_all():
        table.append(
            [klant.klantnummer, klant.naam, klant.klanttype, klant.gemeente, klant.gemeente, klant.saldo])
    return tabulate(table)


def print_details_klant(klantnummer=-1):
    if not klantnummer:
        return f"Ongeldig klantnummer: {klantnummer}"
    if klantnummer == -1:
        return "Geen klantnummer gespecifieerd"
    result = KlantRepository.details(klantnummer)
    if result is None:
        print(f"Klantnummer {klantnummer} is niet gevonden.")
    else:
        table = []
        table.append(
            [result.klantnummer, result.naam, result.klanttype, result.gemeente, result.gemeente, result.saldo])
        print(tabulate(table, headers=[
              "Klantnummer", "Naam", "Klanttype", "Gemeente", "Saldo"]))
    return result
