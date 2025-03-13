from Domanda import Domanda
import random
from Giocatori import Giocatore

AllGiocatori= []

def leggi_domande(domande: str) -> list[Domanda]:
    domandel = []
    with open(domande, "r", encoding="utf-8") as file:
        righe = [riga.strip() for riga in file.readlines()]

    i = 0
    while i < len(righe):
        if righe[i] == "":  # Salta le righe vuote
            i += 1
            continue

        if i + 5 < len(righe):  # Controlla che ci siano abbastanza righe per una domanda
            testo = righe[i]
            difficolta = righe[i + 1]
            risposta_corretta = righe[i + 2]
            errata1 = righe[i + 3]
            errata2 = righe[i + 4]
            errata3 = righe[i + 5]

            # Creiamo la lista delle risposte errate
            risposte_errate = [errata1, errata2, errata3]

            # Aggiungiamo la domanda alla lista
            domandel.append(Domanda(testo, difficolta, risposta_corretta, errata1,errata2,errata3))

        i += 7  # Passa alla prossima domanda

    return domandel


# Testiamo la funzione nel main
'''if __name__ == "__main__":
    domande = leggi_domande("domande.txt")

    print(f"Numero di domande caricate: {len(domande)}\n")

    # Stampiamo solo le prime 3 domande per verifica
    for d in domande[:3]:
        print(f"Domanda: {d.testo}")
        print(f"Difficoltà: {d.difficolta}")
        print(f"Risposta corretta: {d.rispcorretta}")
        print(f"Risposte errate: {d.errata1}, {d.errata2}, {d.errata3}")
        '''

'''def salva_punteggio (nome, punti):
    with open("punti.txt", "r", encoding="utf-8") as file:
        righe = [riga.strip() for riga in file.readlines()]
        for riga in righe:
            if nome in righe:
                indice = righe.index(nome)
                righe[indice] = f"{nome}  {punti}"
                with open("punti.txt", "w", encoding="utf-8") as file:
                    for riga in righe:
                        file.write(riga)
                return
            else:
                righe.append(f"{nome}  {punti}")
                with open("punti.txt", "w", encoding="utf-8") as file:
                    file.write(righe[len(righe)-1])'''
def carica_giocatori():
    with open("punti.txt", "r", encoding="utf-8") as file:
        righe = [riga.strip() for riga in file.readlines()]
        for riga in righe:
            nome, punti = riga.split()
            AllGiocatori.append(Giocatore(nome, int(punti)))

def salva_punteggio (nome, punti):
   NewGiocatore = Giocatore(nome,punti)
   trovato = False
   carica_giocatori()
   if len(AllGiocatori)!=0:
       for giocatore in AllGiocatori:
            if giocatore.nome == nome:
               giocatore.punti = punti
               trovato = True
               break

            if not trovato:
               AllGiocatori.append(NewGiocatore)
   else:
       AllGiocatori.append(NewGiocatore)

   with open ("punti.txt", "w", encoding="utf-8") as file:
       for g in AllGiocatori:
           file.write(f"{g.nome}  {g.punti}\n")


def game ( ):
    domandeall = leggi_domande("domande.txt")
    diff = 0
    contatore_punti=0
    while True:

        domande_diff_0 = [d2 for d2 in domandeall if int(d2.difficolta) == diff]
        if len(domande_diff_0)==0 and diff!=0:
            diff-=1
            domande_diff_0 = [d2 for d2 in domandeall if int(d2.difficolta) == diff]
        if domande_diff_0:
            domanda_selezionata = random.choice(domande_diff_0)
            risposteall= [(domanda_selezionata.rispcorretta,'corretta'),(domanda_selezionata.errata1,'errata'),(domanda_selezionata.errata2,'errata'),(domanda_selezionata.errata3,'errata')]
            random.shuffle(risposteall)
            print(f"Domanda: {domanda_selezionata.testo}")
            print(f"Difficoltà: {domanda_selezionata.difficolta}")
            print("Risposte:")
            for i, risposta in enumerate(risposteall, 1):
                print(f"{i}. {risposta}")

            rispostadata = input("Seleziona una risposta: ")
            risposta_utente = risposteall [ int(rispostadata) - 1]
            if risposta_utente[1] == 'corretta':
                print("Hai indovinato!")
                diff+=1
                contatore_punti+=1
            else:
                print("Hai perso!")
                nome_giocatore = input("Inserisci il tuo nome: ")
                salva_punteggio(nome_giocatore,contatore_punti)

                break


        else:
            diff += 1

game()



