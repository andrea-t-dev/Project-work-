"""
PROPRIETÀ INTELLETTUALE DI: Evoluzione S.r.l.
TUTTI I DIRITTI RISERVATI © 2026

Descrizione: Previsione produzione stagionale di pomodori 
Versione:    1.0
Autore:      Tettoia Andrea

----------------------------------------------------------------------------
AVVISO DI RISERVATEZZA E RESTRIZIONE ALL'USO
----------------------------------------------------------------------------
Questo codice sorgente e le informazioni in esso contenute sono di natura 
strettamente confidenziale e costituiscono segreto industriale di proprietà
esclusiva di Evoluzione S.r.l.

È SEVERAMENTE VIETATA la copia, la riproduzione, la distribuzione, la 
modifica o la divulgazione, totale o parziale, di questo codice con 
qualsiasi mezzo, senza il preventivo consenso scritto del proprietario.

L'accesso non autorizzato o la distribuzione non consentita saranno 
perseguiti a norma delle leggi vigenti sul diritto d'autore (L. 633/1941).
----------------------------------------------------------------------------
"""

import importlib
import subprocess
import sys
import random
from math import ceil


    
banner= r"""

+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

 ######                                                                                                                                                                                              
 #     # #####  ###### #    # #  ####  #  ####  #    # ######    #####  #####   ####  #####  #    # ###### #  ####  #    # ######     ####  #####   ##    ####  #  ####  #    #   ##   #      ###### 
 #     # #    # #      #    # # #      # #    # ##   # #         #    # #    # #    # #    # #    #     #  # #    # ##   # #         #        #    #  #  #    # # #    # ##   #  #  #  #      #      
 ######  #    # #####  #    # #  ####  # #    # # #  # #####     #    # #    # #    # #    # #    #    #   # #    # # #  # #####      ####    #   #    # #      # #    # # #  # #    # #      #####  
 #       #####  #      #    # #      # # #    # #  # # #         #####  #####  #    # #    # #    #   #    # #    # #  # # #              #   #   ###### #  ### # #    # #  # # ###### #      #      
 #       #   #  #       #  #  # #    # # #    # #   ## #         #      #   #  #    # #    # #    #  #     # #    # #   ## #         #    #   #   #    # #    # # #    # #   ## #    # #      #      
 #       #    # ######   ##   #  ####  #  ####  #    # ######    #      #    #  ####  #####   ####  ###### #  ####  #    # ######     ####    #   #    #  ####  #  ####  #    # #    # ###### ###### 

+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=                                                                                                                                                                                                                                                                                                          

"""                                                                                                    

print(banner)

librerie = ['tabulate','matplotlib','numpy']


def controllo_librerie(librerie): #funzione utilizzata per controllare se le librerie tabulate, matplotlib e numpy siano effettivamente installate nel sistema

    for libreria in librerie:
        try:
            importlib.import_module(libreria)
        except ModuleNotFoundError:
            print(f'ATTENZIONE!! {libreria} non è installata nel sistema. Tentativo di installazione in corso...')
            try:
                subprocess.check_call([sys.executable, '-m', 'pip','install',libreria])
                print(f'{libreria} installata correttamente.\n')
            except subprocess.CalledProcessError:
                print(f'ATTENZIONE!! Impossibile installare {libreria}. Verifica il nome della libreria che desideri installare')
                sys.exit(1)

controllo_librerie(librerie)

from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

def richiesta_ettaro(): #funzione che permette di impostare quanti ettari di terreno vengano coltivati durante la produzione stagionale. 

    while True:
        try:
            ettaro = int(input('Ettari massimi coltivabili 5. Quanti ettari si vogliono coltivare? '))
            if ettaro > 5:
                print("\nL'azienda possiede massimo 5 ettari di terreno coltivabile\n")
                continue
            else: 
                return ettaro
        except ValueError:
            print('Sono permessi solo valori numerici interi')

#calcolo dell'obiettivo di produzione che si aspetta l'azienda in una stagione, calcolato in maniera randomica su un ettaro di terra. 
def quantità_da_produrre(ettaro):
   
        t_totali_terra = round(ettaro * random.uniform(40,60),2) #fissati i quantitativi massimi e minimi in coltivazione terraria previste per ettaro di terra
        t_totali_idro = round(ettaro * random.uniform(250, 500),2) #fissati i quantitativi massimi e minimi in coltivazione idroponica previste per ettaro di terra
        dati = [['Tonnellate',t_totali_idro, t_totali_terra]]
        intestazioni = ['Coltivazione Idroponica','Coltivazione Terraria']
        if ettaro == 1:
            print('\nOBIETTIVO PRODUZIONE STAGIONALE POSTO DALL\'AZIENDA CALCOLATO SU UN ETTARO')
        else:
            print(f'\nOBIETTIVO PRODUZIONE STAGIONALE POSTO DALL\'AZIENDA CALCOLATO SU {ettaro} ETTARI')
        print(tabulate(dati, headers=intestazioni, colalign=('center','center','center'), tablefmt='grid'))

        return t_totali_terra,t_totali_idro

# Setting da parte dell'operatore delle previsioni meteo durante la fase di produzione di pomodori in coltivazione terraria che potrebbe influire sul raccolto 
def meteo():

    print('\nProbabili condizioni meteo stagionali impattanti sul raccolto della coltivazione terraria:\n')
    print('1 - Eccellente (Soleggiato, piogge regolari)\n')
    print('2 - Variabile (Sbalzi termici, piogge brevi ma di grande intensità)\n')
    print('3 - Avverso (Siccità o piogge eccessive)\n')

    while True: # controllo dell'input
        try:
            scelta = int(input('\nInserire la probabile condizione meteo: '))
        except ValueError:
            print('\nInserire un valore tra 1 e 3\n')
            continue

        if scelta == 1: #se la scelta ricade su Eccellente avremo una percentuale di pomodori di prima e seconda scelta più alta
            percentuale_prima_scelta = random.uniform(0.65, 0.80)
            percentuale_seconda_scelta = random.uniform(0.15, 0.20)
            break
        elif scelta == 2: #se la scelta ricade su Variabile avremo una percentuale di pomodori di prima e seconda scelta più bassa
            percentuale_prima_scelta = random.uniform(0.40, 0.50)
            percentuale_seconda_scelta = random.uniform(0.35, 0.45)
            break
        elif scelta == 3:
            percentuale_prima_scelta = random.uniform(0.10, 0.20) # se la scelta ricade su Avverso si ha una percentuale di pomodori di prima e seconda scelta molto bassa andando ad inefficiare il raccolto e una propensione al materiale di scarto più alto
            percentuale_seconda_scelta = random.uniform(0.20, 0.30)
            break
        else:
            print('\nInserisci il valore adeguato')
    
    return percentuale_prima_scelta, percentuale_seconda_scelta

def coltivazione_idroponica(t_totali_idro): # funzione che calcola la produzione di pomodori di prima scelta, seconda scelta e materiale di scarto sulla base dell'obiettivo complessivo di produzione posto dall'azienda con una variazione percentuale che viene scelta randomicamente. Essendo una coltivazione controllata le percentuali sono fissate da un minimo ad un massimo.
    
    prima_scelta = round(t_totali_idro * random.uniform (0.55, 0.60),2)
    seconda_scelta = round(t_totali_idro * random.uniform (0.25, 0.30),2)
    scarto = round(t_totali_idro - (prima_scelta + seconda_scelta),2)    
    return prima_scelta,seconda_scelta,scarto     
    

def coltivazione_terraria(t_totali_terra,percentuali_prima_scelta,percentuali_seconda_scelta): # funzione che calcola la produzione di pomodori di prima, seconda scelta e materiale di scarto sulla base dell'obiettivo complessivo di produzione posto dall'azienda con una variazione percentuale che viene scelta randomicamente sulla base delle condizioni meteo previste durante la stagione tramite la funzione meteo().
    
    prima_scelta = round((t_totali_terra * percentuali_prima_scelta),2)
    seconda_scelta = round((t_totali_terra * percentuali_seconda_scelta),2)
    scarto = round(t_totali_terra - (prima_scelta + seconda_scelta),2)
    return prima_scelta,seconda_scelta,scarto

def tabella(t_totali_idro,t_totali_terra,prima_scelta_idro,seconda_scelta_idro,scarto_idro,prima_scelta_terra,seconda_scelta_terra,scarto_terra): #creo una funzione che mi restituisca una tabella per mostrare l'output delle funzioni coltivazione_idroponica() e coltivazione_terraria() avendo una visione chiara della differenza di produzione dei cicli produttivi divisi per tipologia

    dati = [['Prima scelta',str(prima_scelta_idro) +' t',str(prima_scelta_terra) + ' t'],['Seconda scelta', str(seconda_scelta_idro) + ' t', str(seconda_scelta_terra) + ' t'],['Scarto',str(scarto_idro) + ' t',str(scarto_terra) + ' t'], ['TOTALE', str(t_totali_idro) + ' t', str(t_totali_terra) + ' t']]
    intestazioni = ['Pomodori', 'Coltivazione Idroponica','Coltivazione Terraria']
    print('\nPREVISIONE SUDDIVISIONE DEL RACCOLTO')
    print(tabulate(dati, headers=intestazioni, colalign=('center','center','center'), tablefmt='grid'))

def coltivazione_maturazione(): #calcolo maturazione dell'ortaggio pronto per essere raccolto
    
    maturazione_idro =  random.randint(45,60) #giorni che intercorrono dal trapianto della piantina al sistema idroponico
    maturazione_terra = random.randint(60,85) #giorni che intercorrono dal trapianto della piantina al terreno
    dati = [['Giorni', str(maturazione_idro),str(maturazione_terra)]]
    intestazioni = ['Coltivazione Idroponica', 'Coltivazione Terraria']
    print('\nGIORNI PREVISTI PER LA MATURAZIONE')
    print(tabulate(dati, headers=intestazioni, colalign=('center','center','center'), tablefmt='grid'))

def raccolta (t_totali_terra,t_totali_idro,prima_scelta_idro,seconda_scelta_idro,scarto_idro):

    operai = 30 #operai dedicati alla raccolta    
    ore_lavorate = 8 #8 ore di lavoro giornaliere
    tonnellate_orarie_operaio = 0.3 # tonnellate di pomodori raccolti per operaio
    forza_lavoro_operaio = tonnellate_orarie_operaio * ore_lavorate #calcolo forza lavorativa per singolo operaio
    forza_lavoro_totale = forza_lavoro_operaio * operai #calcolo della forza lavoro complessiva per la raccolta
    giorni_lavorati_idro = ceil(t_totali_idro / forza_lavoro_totale)
    giorni_lavorati_terra = ceil(t_totali_terra / forza_lavoro_totale)
  
    print('\nIl tempo di raccolta e selezione per i pomodori prodotti in serra idroponica è di giorni: ' + str(giorni_lavorati_idro))

    stagionali = 0
    p_idro_eff, s_idro_eff, scarto_idro_eff = prima_scelta_idro,seconda_scelta_idro,scarto_idro

    if giorni_lavorati_idro > 5: #controllo per verificare che la raccolta avvenga in 5 giorni massimo, se i giorni sono più di 5 si effettua il calcolo di quanti operai ci sia bisogno di assumere per rimanere nei termini previsti di raccolto
        forza_lavoro_necessaria = t_totali_idro / 5
        assunzione = int(forza_lavoro_necessaria / forza_lavoro_operaio)
        stagionali = assunzione - operai
        print(f'\nATTENZIONE!! Si richiede maggiore manovalanza per accelerare la fase di raccolto ed effettuarla in massimo 5 giorni. Valutare assunzione stagionale di ulteriori {stagionali} operai')

        while True:
            scelta = input("\nVuoi procedere con l'assunzione dei lavoratori stagionali? (si/no): ").lower().strip()
            if scelta in ['si', 's']:
                print("\nAssunzione confermata. Tutto il raccolto verrà processato.")
                break
            elif scelta in ['no', 'n']:
                # Se l'utente rifiuta, applichiamo la raccolta ottimizzata
                stagionali = 0 
                p_idro_eff, s_idro_eff, scarto_idro_eff = raccolta_ottimizzata(t_totali_idro, prima_scelta_idro,seconda_scelta_idro,scarto_idro)
                break
            else:
                print("\nInserire 'si' o 'no'.")

    print('\nIl tempo di raccolta e selezione per i pomodori prodotti da coltivazione terraria è di giorni: ' + str(giorni_lavorati_terra))
    return stagionali,p_idro_eff, s_idro_eff, scarto_idro_eff

def raccolta_ottimizzata(t_totali_idro, p_idro, s_idro, scarto_idro):
    # Capacità totale di raccolta dei 30 operai in 5 giorni 
    capacita_totale = 30 * 8 * 0.3 * 5
    
    print(f"\n--- LOGICA DI EMERGENZA: OTTIMIZZAZIONE SULLA PRIMA SCELTA ---")
    print(f"\nCapacità massima di raccolta in 5 giorni: {capacita_totale} t")
    
    #Raccolta Prima Scelta
    p_eff = round(min(p_idro, capacita_totale), 2)
    capacita_residua = max(0, capacita_totale - p_eff)
    
    #Raccolta Seconda Scelta (con la capacità che avanza)
    s_eff = round(min(s_idro, capacita_residua), 2)
       
    # tutto ciò che rimane fuori dalla raccolta entrerà a far parte del materiale di scarto
    scarto_eff = round(t_totali_idro - p_eff - s_eff, 2)
    
    declassato = round(scarto_eff - scarto_idro, 2)
    
    if declassato > 0:
        print(f"\nAVVISO: {declassato} t di prodotto sono state declassate a SCARTO per mancanza di personale.")
    
    print(f"\nRiepilogo: Prima Scelta: {p_eff}t, Seconda Scelta: {s_eff}t, Scarto Totale: {scarto_eff}t")
    
    return p_eff, s_eff, scarto_eff

def ricavo_guadagno(stagionali,ettaro,prima_scelta_idro,seconda_scelta_idro,scarto_idro,prima_scelta_terra,seconda_scelta_terra,scarto_terra): #funzione che calcola il ricavo e guadagno ipotizzando la vendita complessiva di tutti i pomodori coltivati

    def validazione_input(messaggio, minimo, massimo): #controllo e validazione dell'input sul prezzo di vendita massimo e minimo su ogni tipologia di prodotto venduto
        while True:
            try:
                importo = int(input(messaggio))
                if minimo <= importo <= massimo:
                    return importo
                else:
                    print(f'\nAttenzione, inserire importo compreso tra {minimo} e {massimo}')
            except ValueError:
                print('\nInserire solo valori numerici interi')

    while True:
        richiesta = input('\nSi vuole conoscere l\'ipotetico ricavo e guadagno stagionale? (Digitare si o no) ').lower().strip()
        if richiesta == 'si' or richiesta == 's':
            costo_lavoratori_stagionali = stagionali * 1600 #costo mano d'opera extra per raggiungere gli obiettivi prefissati di raccolta 
            costi_fissi_terra = (25700 * ettaro) #costi fissi per la produzione stagionale dei pomodori con coltivazione terraria per ogni ettaro di terreno coltivato.
            costi_fissi_idro = (83600 * ettaro) + costo_lavoratori_stagionali #costi fissi per la produzione stagionale dei pomodori in coltivazione idroponica per ogni ettaro di coltivazione idroponica.
        
            a = validazione_input('\nInserire il prezzo di vendita dei pomodori di prima scelta in coltivazione idroponica che varia dai 1100€ ai 1200€ a tonnellata: ',1100,1200)
            if seconda_scelta_idro > 0:
                b = validazione_input('\nInserire il prezzo di vendita dei pomodori di seconda scelta in coltivazione idroponica che varia dai 920€ ai 1000€ a tonnellata: ',920,1000)
            else:
                b = 0
            if scarto_idro > 0:
                c = validazione_input('\nInserire il prezzo di vendita del materiale di scarto proveniente dalla coltivazionbe idroponica che varia dai 450€ ai 600€ a tonnellata: ',450,600)
            else:
                c = 0
            d = validazione_input('\nInserire il prezzo di vendita dei pomodori di prima scelta in coltivazione terraria che varia dai 800€ ai 1000€ a tonnellata: ',800,1000)
            e = validazione_input('\nInserire il prezzo di vendita di pomodori dei seconda scelta in coltivazione terraria che varia dai 650€ ai 700€ a tonnellata: ',650,700)
            f = validazione_input('\nInserire il prezzo di vendita del materiale di scarto proveniente dalla coltivazione terraria che varia dai 280€ ai 400€ a tonnellata: ',280,400)
            
            #una volta inseriti gli input si passa al calcolo dei ricavi.
            ricavo_prima_scelta_idro = round((prima_scelta_idro * a),2) 
            ricavo_seconda_scelta_idro = round((seconda_scelta_idro * b),2)
            ricavo_scarto_idro = round((scarto_idro * c),2)
            ricavo_prima_scelta_terra = round((prima_scelta_terra * d),2)
            ricavo_seconda_scelta_terra = round((seconda_scelta_terra * e),2)
            ricavo_scarto_terra = round((scarto_terra * f),2)
            tot_ricavi_idro = ricavo_prima_scelta_idro + ricavo_seconda_scelta_idro + ricavo_scarto_idro
            tot_ricavi_terra = ricavo_prima_scelta_terra + ricavo_seconda_scelta_terra + ricavo_scarto_terra
            print(f'\nIl totale dei ricavi provenienti dalla vendita della coltivazione idroponica sarà di: {tot_ricavi_idro} €')
            print (f'\nIl totale dei ricavi provenienti dalla vendita della coltivazione terraria sarà di: {tot_ricavi_terra} €')
            #andando a sottrarre i costi fissi delle due tipologie di coltivazioni otteniamo il guadagno.
            guadagno_idro = tot_ricavi_idro - costi_fissi_idro - costo_lavoratori_stagionali
            guadagno_terra = tot_ricavi_terra - costi_fissi_terra
            print(f'\nIl guadagno ricavato dalla coltivazione idroponica sarà di: {guadagno_idro:.2f} €')
            print(f'\nIl guadagno ricavato dalla coltivazione terraria sarà di : {guadagno_terra:.2f} €')
            break

        elif richiesta == 'no' or richiesta =='n':
            print('\nGrazie per aver utilizzato il programma')
            sys.exit()
        else:
            print('\nInserire si o no')
            continue

def grafico(prima_scelta_idro,seconda_scelta_idro,scarto_idro,prima_scelta_terra,seconda_scelta_terra,scarto_terra,nome_file='Comparazione'): #funzione che permette la creazione del grafico e nel caso essa venga eseguita salva l'immagine nella stessa cartella di esecuzione del programma

    while True:
        richiesta = input('\nSi vuole scaricare un grafico che compari le due tipologie di coltivazioni? (Digitare si o no) ').lower().strip()
        if richiesta == 'si' or richiesta == 's':
            valori_idro = [prima_scelta_idro,seconda_scelta_idro,scarto_idro]
            valori_terra = [prima_scelta_terra,seconda_scelta_terra,scarto_terra]

            categorie = ['Prima scelta','Seconda scelta', 'Scarto']
            x = np.arange(len(categorie))
            width = 0.20

            plt.figure(figsize=(8,6),facecolor='#f2f2f2') #setting della dimensione del grafico con sfondo grigio chiaro
            plt.bar(x - width/2,valori_idro,width,label='Idroponica', color="#4C9A2A") #si setta la barra leggermente più spostata a sinistra passandogli i dati per impostare l'altezza, si setta la larghezza e con label viene impostato il nome per la legenda 
            plt.bar(x + width/2,valori_terra,width,label='Terraria', color="#2A6FA0") #si setta la barra più spostata a destra per affiancarla

            plt.xticks(x, categorie) #vengono sostituiti i numeri con le etichette testuali inserite in categorie
            plt.ylabel("Tonnellate") #etichetta sull'asse Y
            plt.title("Comparazione produzioni di pomodori su un ciclo")
            plt.legend()
            plt.tight_layout()

            grafico_path = f"{nome_file}.png"
            plt.savefig(grafico_path) #viene salvata l'immagine del grafico creato nello stesso percorso di dove risiede il programma 
            print(f"\nGrafico salvato con il nome di: {grafico_path}")
            break
        elif richiesta == 'no' or richiesta =='n':
            break
        else:
            print('\nInserire si o no')
            continue

def main():

    ettaro = richiesta_ettaro() 

    t_totali_terra,t_totali_idro = quantità_da_produrre(ettaro) #calcolo complessivo delle tonnellate su cui pone l'obiettivo l'azienda per i due ciclo produttivo 

    percentuali_prima_scelta, percentuali_seconda_scelta = meteo() #avvio funzione per richiesta di previsione meteo durante la stagione che va a spostare il livello di percentuale del raccolto nella coltivazione terraria.

    prima_scelta_idro,seconda_scelta_idro,scarto_idro = coltivazione_idroponica(t_totali_idro) #calcolo della distribuzione degli output sulla coltivazione idroponica

    prima_scelta_terra,seconda_scelta_terra,scarto_terra = coltivazione_terraria(t_totali_terra,percentuali_prima_scelta,percentuali_seconda_scelta) #calcolo della distribuzione degli output sulla coltivazione iterraria

    tabella(t_totali_idro,t_totali_terra,prima_scelta_idro,seconda_scelta_idro,scarto_idro,prima_scelta_terra,seconda_scelta_terra,scarto_terra) #funzione che restituisce una tabella comparativa

    grafico(prima_scelta_idro,seconda_scelta_idro,scarto_idro,prima_scelta_terra,seconda_scelta_terra,scarto_terra) #richiesta creazione grafico e salvataggio dello stesso sulla macchina locale
    
    coltivazione_maturazione() #calcolo della maturazione dei pomodori dal momenti in cui viene trapiantata la pianta nella serra e nella terra.

    stagionali,p_idro_eff, s_idro_eff, scarto_idro_eff = raccolta(t_totali_terra,t_totali_idro,prima_scelta_idro,seconda_scelta_idro,scarto_idro) #previsione dei giorni necessari a raccogliere e smistare l'intera produzione sia per la coltivazione idroponica che quella terraria

    ricavo_guadagno(stagionali,ettaro, p_idro_eff, s_idro_eff, scarto_idro_eff,prima_scelta_terra,seconda_scelta_terra,scarto_terra) #calcolo dei ricavi e guadagni

main() # avvio del programma