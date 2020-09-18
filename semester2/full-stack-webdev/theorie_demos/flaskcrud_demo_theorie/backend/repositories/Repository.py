from .Database import Database

class DataRepository:
    @staticmethod
    def read_klanten():
        sql = "SELECT * FROM tblklant"
        return Database.get_rows(sql)
        
    @staticmethod
    def read_klant(KlantID):
        sql = "SELECT * FROM tblklant WHERE KlantID = %s"
        params = [id]
        return Database.get_one_row(sql, params)
