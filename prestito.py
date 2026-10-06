class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.__codice = codice
        self.__data = data
        self.__id_strumento = id_strumento
        # senza "__" → passa dal setter, quindi viene controllato
        self.cognome_allievo = cognome_allievo

    def __str__(self):
        return f"{self.__codice} - {self.__data} - {self.__id_strumento} - {self.__cognome_allievo}"

    def __repr__(self):
        return f"Prestito:({self.__codice!r}, {self.__data!r}, {self.__id_strumento!r}, {self.__cognome_allievo!r})"

    @property
    def codice(self):
        return self.__codice

    @property
    def data(self):
        return self.__data

    @property
    def id_strumento(self):
        return self.__id_strumento

    @property
    def cognome_allievo(self):
        return self.__cognome_allievo

    @cognome_allievo.setter
    def cognome_allievo(self, valore):
        if not valore.strip():
            raise ValueError("Cognome allievo non valido")
        self.__cognome_allievo = valore.strip()
