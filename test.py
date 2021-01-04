# importa la classe dal file
from vaccines import Vaccines
v = Vaccines()

# Stampa il numero totale delle persona vaccinate
# il numero è restituito come int
print(v.totale_vaccinati)

# Stampa il totale dei vaccinati per categoria
# Personale sanitario, ospiti, [...]
# il valore ritornato è una stringa
print(v.categoria)

# Stampa i dati sui vaccini per tutte le regioni
# come dosi, persone vaccinate, percentuale, [...]
# il valore ritornato è una stringa
print(v.regioni)

# Stampa i dati sui vaccini per una regione fornita
# come argomento della funzione, consultare il README
# per gli argomenti accettati
# il valore ritornato è una stringa
print(v.get_regione("Lombardia"))

# Stampa i dati delle persone vaccinate 
# divise per fasce d'età
# il valore ritornato è una stringa
print(v.fasce_eta)

# Crea un grafico sull'andamento delle
# vaccinazioni basato sulle somministrazioni
# totali
v.get_grafico()

# Crea un grafico sull'andamento delle 
# vaccinazioni basato sulle somministrazioni
# per fascia d'età
v.get_grafico_fasce()