#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define numquest 3                  //numero domande
#define nicklenght 800       //numero caratteri nickname consentiti

void presentazione() {   //intro del gioco
    printf ("\nBenvenuto!!\n");
    printf("Il gioco sta per cominciare\n");
    printf ("Rispondete correttamente per collezionare punti.\n");
    printf ("Ogni risposta esatta garantisce 1 punto!\n");
    printf ("Buona fortuna!\n");
    }
    
void Menu() { //menu di scelta
    printf("Vuoi iniziare a giocare?\n");
    printf("Digita A per cominciare o un tasto a tua scelta per uscire dal gioco.\n"); 
}

int main() {
    char scelta;
    char nickname[nicklenght];
    int punteggio = 0;
    
    char domande[numquest][nicklenght] = {  //array di domande
        "Quanti stomaci ha una mucca?\nA) 2\nB) 3\nC) 4\n"
        "Quante ore al giorno mangia una mucca?\nA) 12\nB) 17\nC) 20\n"
        "Quanti chili, in media, pesa una mucca adulta?\nA) 400\nB) 800\nC) 600"
    };
    
    char risposteUtente[numquest] = {'C', 'B', 'C'};  //array di risposte
    
    presentazione();
    Menu();
    scanf(" %c", &scelta);
    
    if (scelta == 'A' || scelta == 'a') {
        printf("Inserisci il tuo nickname: ");
        scanf("%s", nickname);
        printf("Rispondi in sequenza premendo INVIO dopo ogni risposta\n\n.");
        
        for (int i = 0; i < numquest; i++) {
            char risposta;
            printf("%s\n", domande[i]);
            printf("Inserisci la tua risposta: ");
            scanf(" %c", &risposta);
            
            if (risposta == risposteUtente[i]) {
                punteggio++;
            }
        }
        
        printf("Hai totalizzato: %d\n", punteggio);
        
    } else {
        printf("Grazie, torna a giocare quando vuoi!\n");
    }
    
    return 0;
}