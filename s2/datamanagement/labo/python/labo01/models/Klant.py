class Klant:
    def __init__(self, Klantnummer, Naam, Klanttype, Gemeente, Saldo):
        self._valueErrors = {}
        self.klantnummer = Klantnummer
        self.naam = Naam
        self.klanttype = Klanttype
        self.gemeente = Gemeente
        self.saldo = Saldo

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(self.klantnummer, self.naam, self.klanttype, self.gemeente, self.saldo)

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return (len(self._valueErrors) == 0)

    @property
    def klantnummer(self):
        return self._klantnummer

    @klantnummer.setter
    def klantnummer(self, value):
        if type(value) is int:
            self._klantnummer = value
        else:
            self._valueErrors['klantnummer'] = ValueError("Geen geldig nummer")


    @property
    def naam(self):
        return self._naam

    @naam.setter
    def naam(self, value):
        if type(value) == str:
            self._naam = value
        else:
            self._valueErrors['naam'] = ValueError("Foute naam")

        if len(value) > 50:
            self._valueErrors['naam lengte'] = ValueError(
                "Maximaal 50 karakters.")

    @property
    def klanttype(self):
        return self._klanttype

    @klanttype.setter
    def klanttype(self, value):
        if type(value) == str:
            self._klanttype = str(value).upper()
        else:
            self._valueErrors['klanttype'] = ValueError("Fout klanttype")
        if len(value) != 1:
            self._valueErrors['klanttype lengte'] = ValueError(
                "Klanttype bestaat uit 1 letter.")

    @property
    def gemeente(self):
        return self._gemeente

    @gemeente.setter
    def gemeente(self, value):
        if type(value) == str:
            self._gemeente = value
        else:
            self._valueErrors['gemeente'] = ValueError("Foute gemeente")

        if len(value) > 50:
            self._valueErrors['gemeente lengte'] = ValueError(
                "Maximaal 50 karakters.")

    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
        try:
            value = int(value)
            self._saldo = value
            if value < 0:
                self._valueErrors['saldo lengte'] = ValueError("Saldo moet groter zijn dan 0.")
        except:
            self._valueErrors['saldo'] = ValueError("Fout saldo")

        


