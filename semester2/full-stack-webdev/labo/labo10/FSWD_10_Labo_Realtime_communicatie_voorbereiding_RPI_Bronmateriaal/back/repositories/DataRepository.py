from .Database import Database


class DataRepository:
    @staticmethod
    def json_or_formdata(request):
        if request.content_type == 'application/json':
            gegevens = request.get_json()
        else:
            gegevens = request.form.to_dict()
        return gegevens


    # vraag alle info van lampen op
    @staticmethod
    def read_status_lampen():
        sql = "SELECT * from lampen"
        return Database.get_rows(sql)

    # Vraag alle info op, van de lamp die hoort bij een bepaald id.
    @staticmethod
    def read_status_lamp_by_id(id):
        sql = "SELECT * from lampen WHERE id LIKE %s"
        params = [id]
        return Database.get_one_row(sql, params)

    # pas lamp status aan (0 of 1)
    @staticmethod
    def update_status_lamp(id, status):
        sql = "UPDATE lampen SET status = %s WHERE id = %s"
        params = [status, id]
        return Database.execute_sql(sql, params)

    #pas alle lampen aan
    @staticmethod
    def update_status_alle_lampen(status):
        sql = "UPDATE lampen SET status = %s"
        params = [status]
        return Database.execute_sql(sql, params)