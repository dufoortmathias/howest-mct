from models.Categorie import Categorie
from repositories.Database import Database


class CategorieRepository:

    @staticmethod
    def read_all():
        categories = []
        sql = "SELECT Categorienummer, Categorienaam, "
        sql += "Bijschrijving FROM artemis.tblcategorieen"
        rows = Database.get_rows(sql)
        if not (rows is None):
            for row in rows:
                # mapping naar object
                categories.append(CategorieRepository.map_to_object(row))
        return categories

    @staticmethod
    def map_to_object(row):
        if (row is not None and type(row) is dict):
            nummer = int(row['Categorienummer'])
            naam = CategorieRepository.checkColumn(row, 'Categorienaam')
            beschrijving = CategorieRepository.checkColumn(row, 'Bijschrijving')
        return Categorie(nummer, naam, beschrijving)

    @staticmethod
    def checkColumn(row, columnName):
        result = ""
        if (columnName in row.keys() and row[columnName] is not None):
            result = row[columnName]
        return result

    @staticmethod
    def details(id, withProducts=False):
        # 1. Valideer de gebruikersinput
        if not id or id == -1:
            return "Ongeldig categorienummer, probeer opnieuw"
        # 2. Maak sql expressie met SQL parameters
        sql = "SELECT Categorienummer, Categorienaam, Bijschrijving "
        sql += " FROM artemis.tblcategorieen WHERE Categorienummer = %s "
        values = [id]
        # 3. Evalueer het resultaat (dictionary) met foutcontrole.
        # data ophalen, of foutboodschap
        result = Database.get_one_row(sql, values)
        # Levert de expressie geen None op?
        # 4. mapping van een geslaagd SQL resultaat naar een Python object
        if type(result) is dict:
            result = CategorieRepository.map_to_object(result)
        # 5. return het resultaat (als een verzameling van Python objecten).
        return result