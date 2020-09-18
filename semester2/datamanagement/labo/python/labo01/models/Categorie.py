class Categorie:
    def __init__(self, par_categorienummer, par_categorienaam, par_beschrijving):
        self._valueErrors = {}
        self.categorienummer = par_categorienummer
        self.categorienaam = par_categorienaam
        self.beschrijving = par_beschrijving

    def __str__(self):
        return "{0}, {1}, {2}".format(self.categorienummer, self.categorienaam, self.beschrijving)

    @property
    def valueErrors(self):
        return self._valueErrors

    @property
    def isValid(self):
        return (len(self._valueErrors) == 0)

    @property
    def categorienummer(self):
        return self._categorienummer
        

    @categorienummer.setter
    def categorienummer(self, value):
        if type(value) is int:
            self._categorienummer = value
        else:
            self._valueErrors['catogorienummer'] = ValueError("Geen geldig nummer")
            #raise ValueError("Geen geldig categorienummer")

    @property
    def beschrijving(self):
        return self._beschrijving

    @beschrijving.setter 
    def beschrijving(self, value):
        if type(value) == str:
            self._beschrijving = value
        else:
            self._valueErrors['beschrijving'] = ValueError("Foute beschrijving")
        
        if len(value) > 60:
            self._valueErrors['beschrijving lengte'] = ValueError("Maximaal 50 karakters.")


    
