from operator import attrgetter
from strumento import Strumento
from prestito import Prestito


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.__nome = nome
        self.__responsabile = responsabile

### metodi get e set :
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valore):
        if not valore.strip():
            raise ValueError("Nome deposito non valido")
        self.__nome = valore.strip()

    @property
    def responsabile(self):
        return self.__responsabile

    @responsabile.setter
    def responsabile(self, valore):
        if not valore.strip():
            raise ValueError("Nome responsabile non valido")
        self.__responsabile = valore.strip()
###


    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        #deve prima rovare l'ultimo codice inserito,--> max(int(s.codice[1:]) for s in self.strumenti)
        '''nuovo_num = max((int(s.codice[1:]) for s in self.strumenti), default=0) + 1
            nuovo_codice = f"S{nuovo_num}"
            oppure per evitare problemi di higher or lower : return sorted(self.strumenti, key=lambda s: s.marca.lower())
            
        '''
        # TODO

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico : from operator import attrgetter

def strumenti_ordinati_per_marca(self):
    return sorted(self.strumenti, key=attrgetter("marca"))"""
        # TODO

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
