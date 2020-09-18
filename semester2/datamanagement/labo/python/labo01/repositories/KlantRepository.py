from models.Klant import Klant
from repositories.Database import Database


class KlantRepository:

    @staticmethod
    def read_all():
        klanten = []
        sql = "SELECT Klantnummer, Naam, Type, Gemeente, Saldo FROM artemis.tblklanten"
        rows = Database.get_rows(sql)
        if not (rows is None):
            for row in rows:
                # mapping naar object
                klanten.append(KlantRepository.map_to_object(row))
        return klanten

    @staticmethod
    def map_to_object(row):
        if (row is not None and type(row) is dict):
            Klantnummer = int(row['Klantnummer'])
            Naam = KlantRepository.checkColumn(row, 'Naam')
            Klanttype = KlantRepository.checkColumn(row, 'Type')
            Gemeente = KlantRepository.checkColumn(row, 'Gemeente')
            Saldo = KlantRepository.checkColumn(row, 'Saldo')
        return Klant(Klantnummer, Naam, Klanttype, Gemeente, Saldo)

    @staticmethod
    def checkColumn(row, columnName):
        result = ""
        if (columnName in row.keys() and row[columnName] is not None):
            result = row[columnName]
        return result

    @staticmethod
    def details(id):
        # 1. Valideer de gebruikersinput
        if not id:
            return "Ongeldig klantnummer, probeer opnieuw"
        # 2. Maak sql expressie met SQL parameters
        sql = "SELECT Klantnummer, Naam, Type, Gemeente, Saldo FROM artemis.tblKlanten WHERE Klantnummer = %s "
        values = [id]
        # 3. Evalueer het resultaat (dictionary) met foutcontrole.
        # data ophalen, of foutboodschap
        result = Database.get_one_row(sql, values)
        # Levert de expressie geen None op?
        # 4. mapping van een geslaagd SQL resultaat naar een Python object
        if type(result) is dict:
            result = KlantRepository.map_to_object(result)
        # 5. return het resultaat (als een verzameling van Python objecten).
        return result
