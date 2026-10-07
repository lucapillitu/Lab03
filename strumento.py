class Strumento:
    def __init__(self, codice, tipo, marca, anno, valore):
        self.__codice = codice
        # senza "__" → passano dai setter, quindi vengono controllati
        self.tipo = tipo
        self.marca = marca
        self.anno = anno
        self.valore = valore

    def __str__(self):
        return f"{self.__codice} - {self.__tipo} - {self.__marca} - {self.__anno} - {self.__valore:.2f} €"

    def __repr__(self):
        return f"Strumento:({self.__codice!r}, {self.__tipo!r}, {self.__marca!r}, {self.__anno}, {self.__valore})"

    @property
    def codice(self):          # sola lettura: nessun setter
        return self.__codice

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valore):
        if not valore.strip():
            raise ValueError("Tipo non valido")
        self.__tipo = valore.strip()

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valore):
        if not valore.strip():
            raise ValueError("Marca non valida")
        self.__marca = valore.strip().title()

    @property
    def anno(self):
        return self.__anno

    @anno.setter
    def anno(self, valore):
        if not isinstance(valore, int) or valore < 0:
            raise ValueError("Anno non valido")
        self.__anno = valore

    @property
    def valore(self):
        return self.__valore

    @valore.setter
    def valore(self, valore):
        if isinstance(valore, bool) or not isinstance(valore, (int, float)) or valore < 0:
            raise ValueError("Valore non valido")
        self.__valore = valore