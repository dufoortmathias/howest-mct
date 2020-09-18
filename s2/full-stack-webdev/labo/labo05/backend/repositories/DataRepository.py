from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    #########  Klanten  #########
    @staticmethod
    def read_klanten():
        sql = 'SELECT * FROM tblklant'
        return Database.get_rows(sql)

    @staticmethod
    def read_klant(klant_id):
        sql = 'SELECT * FROM tblklant WHERE KlantID = %s'
        params = [klant_id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_klant(naam, voornaam, straat, nr, postcode, gemeente):
        sql = "INSERT INTO tblKlant(FNaam, VNaam, Straat, Nummer, Postcode, Gemeente) VALUE ( % s, % s, % s, % s, % s, % s)"
        params = [naam, voornaam, straat, nr, postcode, gemeente]
        return Database.execute_sql(sql, params)


    @staticmethod
    def update_klant(naam, voornaam, straat, nr, postcode, gemeente, klant_id):
        sql = "UPDATE tblklant SET FNaam = %s, VNaam = %s, straat = %s, nummer = %s, postcode = %s, Gemeente = %s WHERE KlantID = %s"
        params = [naam, voornaam, straat, nr, postcode, gemeente, klant_id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_klant(klantid):
        sql = "DELETE FROM tblklant WHERE klantID = %s"
        params = [klantid]
        return Database.execute_sql(sql, params)

    #########  Bestemmingen  #########
    @staticmethod
    def read_bestemmingen():
        sql = 'SELECT * FROM tblbestemming'
        return Database.get_rows(sql)

    @staticmethod
    def read_bestemming(bestemming_id):
        sql = 'SELECT * FROM tblbestemming WHERE BestemmingID = %s'
        params = [bestemming_id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def create_bestemming(afkorting, voluit, land, typevlucht):
        sql = "INSERT INTO tblbestemming(afkorting, voluit, land, typevlucht) VALUE ( % s, % s, % s, % s, % s, % s)"
        params = [afkorting, voluit, land, typevlucht]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_bestemming(afkorting, voluit, land, typevlucht, bestemming_id):
        sql = "UPDATE tblbestemming SET afkorting = %s, voluit = %s, land = %s, typevlucht = %s WHERE BestemmingID = %s"
        params = [afkorting, voluit, land, typevlucht, bestemming_id]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_bestemming(bestemming_id):
        sql = "DELETE FROM tblbestemming WHERE BestemmingID = %s"
        params = [bestemming_id]
        return Database.execute_sql(sql, params)
