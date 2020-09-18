from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens

    #########  Treinen  #########
    @staticmethod
    def read_treinen():
        sql = "SELECT * FROM treinen"
        return Database.get_rows(sql)

    @staticmethod
    def read_trein(id):
        sql = "SELECT * FROM treinen WHERE idtrein = %s"
        params = [id]
        return Database.get_one_row(sql, params)

    @staticmethod
    def read_treinen_met_bestemming(bestemmingid):
        sql = "SELECT * \
            FROM treinen t \
            INNER JOIN bestemmingen b ON t.bestemmingID = b.idbestemming \
            WHERE idbestemming = %s"
        params = [bestemmingid]
        return Database.get_rows(sql, params)

    @staticmethod
    def create_trein(vertrek, bestemmingID, spoor, vertraging, afgeschaft):
        sql = "insert into treinen(vertrek, bestemmingid, spoor, vertraging, afgeschaft) values (%s, %s, %s, %s, %s)"
        params = [vertrek, bestemmingID, spoor, vertraging, afgeschaft]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_trein(vertrek, bestemmingID, spoor, vertraging, afgeschaft, idtrein):
        sql = "update treinen set vertrek = %s, bestemmingid = %s, spoor = %s, vertraging = %s, afgeschaft = %s where idtrein = %s"
        params = [vertrek, bestemmingID, spoor,
                  vertraging, afgeschaft, idtrein]
        return Database.execute_sql(sql, params)

    @staticmethod
    def delete_trein(idtrein):
        sql = "delete from treinen where idtrein = %s"
        params = [idtrein]
        return Database.execute_sql(sql, params)

    @staticmethod
    def update_trein_vertraging(idtrein, vertraging):
        sql = "UPDATE treinen set vertraging = %s where idtrein = %s"
        params = [vertraging, idtrein]
        return Database.execute_sql(sql, params)

    #########  Bestemmingen  #########
    @staticmethod
    def read_bestemmingen():
        sql = "SELECT idbestemming, stad FROM bestemmingen"
        return Database.get_rows(sql)

