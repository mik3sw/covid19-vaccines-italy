import matplotlib.pyplot as plt
import requests
import csv

class Vaccines:
    def __init__(self):
        self.totale_vaccinati = self.get_totale_vaccinati()
        self.categoria = self.get_categoria()
        self.regioni = self.get_regioni()
        self.fasce_eta = self.get_fasce()
    
    def get_totale_vaccinati(self):
        url = "https://raw.githubusercontent.com/ondata/covid19italia/master/webservices/vaccini/processing/latest_sesso.csv"
        r = requests.get(url)
        totv = 0
        if r.status_code != 200:
            print('Errore durante l\'acquisizione dei dati [get_totale_vaccinati]')
        else:
            wrapper = csv.reader(r.text.strip().split('\n'))
            for row in wrapper:
                try:
                    totv = totv + int(row[0]) + int(row[1])
                except:
                    pass
        return int(totv)
    
    def get_categoria(self):
        url = "https://raw.githubusercontent.com/ondata/covid19italia/master/webservices/vaccini/processing/latest_categoria.csv"
        r = requests.get(url)
        categoria = "Vaccinati per categoria:\n"
        if r.status_code != 200:
            print('Errore durante l\'acquisizione dei dati [get_categoria]')
        else:
            wrapper = csv.reader(r.text.strip().split('\n'))
            for row in wrapper:
                try:
                    int(row[1])
                    categoria = categoria + "{} --> {} vaccinati\n".format(row[0], row[1])
                except:
                    pass
        return categoria
    
    def get_grafico_data(self):
        url = "https://raw.githubusercontent.com/ondata/covid19italia/master/webservices/vaccini/processing/sesso.csv"
        r = requests.get(url)
        lista_vaccinati = [0]
        lista_giorni = ['1/2/2021']
        if r.status_code != 200:
            print('Errore durante l\'acquisizione dei dati [get_grafico_data]')
        else:
            wrapper = csv.reader(r.text.strip().split('\n'))
            for row in wrapper:
                try:
                    int(row[0])
                    day = row[2].split()
                    if day[0] == lista_giorni[len(lista_giorni)-1]:
                        lista_vaccinati[len(lista_vaccinati)-1] = int(row[0]) + int(row[1])
                    else:
                        lista_giorni.append(day[0])
                        lista_vaccinati.append(int(row[0]) + int(row[1]))
                except:
                    pass
        return lista_vaccinati, lista_giorni
    
    def get_grafico(self):
        vac, days = self.get_grafico_data()
        with plt.style.context('seaborn-dark'):
            plt.plot(days, vac, 'b-o',  label='Vaccini')
            plt.title('VACCINAZIONI COVID-19 ITALIA')
            plt.xlabel('Giorni')
            plt.ylabel('Persone vaccinate')
            plt.legend()
            plt.show()
    
    def get_regioni(self):
        url = "https://raw.githubusercontent.com/ondata/covid19italia/master/webservices/vaccini/processing/latest_somministrazioni.csv"
        r = requests.get(url)
        regioni = "==========================\nDati vaccini per regione:\n==========================\n\n"
        if r.status_code != 200:
            print('Errore durante l\'acquisizione dei dati [get_regioni]')
        else:
            wrapper = csv.reader(r.text.strip().split('\n'))
            for row in wrapper:
                try:
                    int(row[1])
                    regioni = regioni + "= {} =\nSomministrazioni: {} ({}%)\nDosi Consegnate: {}\n\n".format(row[0], row[1], round(float(row[2]), 2), row[3])
                except:
                    pass
        return regioni
    
    def get_regione(self, reg):
        url = "https://raw.githubusercontent.com/ondata/covid19italia/master/webservices/vaccini/processing/latest_somministrazioni.csv"
        r = requests.get(url)
        regione = "Dati vaccini regione {}:\n".format(reg)
        if r.status_code != 200:
            print('Errore durante l\'acquisizione dei dati [get_regione]')
        else:
            wrapper = csv.reader(r.text.strip().split('\n'))
            for row in wrapper:
                if row[0] == reg:
                    regione = regione + "Somministrazioni: {} ({}%)\nDosi Consegnate: {}\n\n".format(row[1], round(float(row[2]), 2), row[3])
        return regione
    
    def get_grafico_fasce(self):
        url = "https://raw.githubusercontent.com/ondata/covid19italia/master/webservices/vaccini/processing/fasceEta.csv"
        r = requests.get(url)
        fascia1 = [66]
        fascia2 = [4428]
        fascia3 = [8033]
        fascia4 = [10579]
        fascia5 = [13194]
        fascia6 = [6656]
        fascia7 = [805]
        fascia8 = [1314]
        fascia9 = [955]
        lista_giorni = ['1/2/2021']
        if r.status_code != 200:
            print('Errore durante l\'acquisizione dei dati [get_grafico_data]')
        else:
            wrapper = csv.reader(r.text.strip().split('\n'))
            for row in wrapper:
                try:
                    int(row[1])
                    day = row[2].split()
                    if day[0] == lista_giorni[len(lista_giorni)-1]:
                        if row[0] == "16-19":
                            fascia1[len(fascia1)-1] = int(row[1])
                        if row[0] == "20-29" and len(fascia2)<len(fascia1):
                            fascia2.append(int(row[1]))
                        if row[0] == "30-39" and len(fascia3)<len(fascia2):
                            fascia3.append(int(row[1]))
                        if row[0] == "40-49" and len(fascia4)<len(fascia3):
                            fascia4.append(int(row[1]))
                        if row[0] == "50-59" and len(fascia5)<len(fascia4):
                            fascia5.append(int(row[1]))
                        if row[0] == "60-69" and len(fascia6)<len(fascia5):
                            fascia6.append(int(row[1]))
                        if row[0] == "70-79" and len(fascia7)<len(fascia6):
                            fascia7.append(int(row[1]))
                        if row[0] == "80-89" and len(fascia8)<len(fascia7):
                            fascia8.append(int(row[1]))
                        if row[0] == "90+" and len(fascia9)<len(fascia8):
                            fascia9.append(int(row[1]))
                    else:
                        lista_giorni.append(day[0])
                        if row[0] == "16-19":
                            fascia1.append(int(row[1]))
                except:
                    pass
        # creo il grafico
        with plt.style.context('seaborn-dark'):
            plt.plot(lista_giorni, fascia1, '-o', label='16-19')
            plt.plot(lista_giorni, fascia2, '-o', label='20-29')
            plt.plot(lista_giorni, fascia3, '-o', label='30-39')
            plt.plot(lista_giorni, fascia4, '-o', label='40-49')
            plt.plot(lista_giorni, fascia5, '-o', label='50-59')
            plt.plot(lista_giorni, fascia6, '-o', label='60-69')
            plt.plot(lista_giorni, fascia7, '-o', label='70-79')
            plt.plot(lista_giorni, fascia8, '-o', label='80-89')
            plt.plot(lista_giorni, fascia9, '-o', label='90+')
            plt.title('VACCINAZIONI COVID-19 ITALIA')
            plt.xlabel('Giorni')
            plt.ylabel('Persone vaccinate')
            plt.legend()
            plt.show()
        # fine funzione [grafico per fasce d'età]

    def get_fasce(self):
        url = "https://raw.githubusercontent.com/ondata/covid19italia/master/webservices/vaccini/processing/latest_fasceEta.csv"
        r = requests.get(url)
        fasce = "==========================\nDati vaccini fasce età:\n==========================\n\n"
        if r.status_code != 200:
            print('Errore durante l\'acquisizione dei dati [get_regioni]')
        else:
            wrapper = csv.reader(r.text.strip().split('\n'))
            for row in wrapper:
                try:
                    int(row[1])
                    fasce = fasce + "= Fascia {} anni =\nVaccinazioni: {}\n\n".format(row[0], row[1])
                except:
                    pass
        return fasce                         