import gradio as gr

def calculate_total(s90_mult, s45_mult, pro_os_mult, pro_vs_mult, scarico_choice, a90_mult, a45_mult, pro_oa_mult, pro_va_mult, aspirazione_choice, tee):
    # Convert tee checkbox value to numeric multiplier
    tee_mult = 5.8 if tee else 0

    # Base values
    a90_base = 2.3
    s90_base = 2.5
    a45_base = 2.0
    s45_base = 2.0
    pro_oa_base = 1.0
    pro_os_base = 1.3
    pro_va_base = 1.0
    pro_vs_base = 1.3

    # Dictionaries for the base values based on radio choices
    scarico_base_values = {"Scarico uscita sul tetto": 1.0, "Scarico uscita a parete": 3.6}
    aspirazione_base_values = {"Aspirazione sul tetto": 1.15, "Aspirazione a parete": 1.0}

    # Calculating total
    total = (a90_base * a90_mult + s90_base * s90_mult + a45_base * a45_mult + s45_base * s45_mult +
             pro_oa_base * pro_oa_mult + pro_os_base * pro_os_mult +
             pro_va_base * pro_va_mult + pro_vs_base * pro_vs_mult +
             scarico_base_values[scarico_choice] + aspirazione_base_values[aspirazione_choice] +
             tee_mult)
    
    # Determine the image and message based on total value
    if total > 21:
        image = "no.png"
        message = "<div style='font-size: 30px; text-align: center;'>Avviso: Installazione negata per superamento della perdita di carico totale degli accessori oltre 21,0 mmH2O.</div>"
    elif 0 <= total <= 5:
        image = "image1.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>Piega i settori dal 1 al 5</div>"
    elif 5.1 <= total <= 7.5:
        image = "image2.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>Piega i settori dal 1 al 6</div>"
    elif 7.6 <= total <= 10:
        image = "image3.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>Piega i settori dal 1 al 7</div>"
    elif 10.1 <= total <= 15:
        image = "image4.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>Piega i settori dal 1 al 8</div>"
    elif 15.1 <= total <= 20:
        image = "image5.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>Piega i settori dal 1 al 9</div>"
    elif 20.1 <= total <= 21:
        image = "image6.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>Piega tutti i settori</div>"
    else:
        image = "no.png"
        message = "<div style='font-size: 30px; text-align: center;'>Valore non previsto</div>"

    return message, image

def calculate_total_coax(a90_coax_mult, s45_coax_mult, pro_o_coax_mult, pro_v_coax_mult):
    # Base values coax
    a90_coax = 1
    a45_coax = 0.5
    pro_v_coax = 1.0
    pro_o_coax = 1.0
    
    # Calculating total_coax
    total_coax = (a90_coax * a90_coax_mult +  a45_coax * s45_coax_mult + 
                  pro_o_coax_mult * pro_v_coax_mult)
                 
    # Determine if installation is possible
    if total_coax > 7.5:
        image = "no.png"
        message = "<div style='font-size: 30px; text-align: center;'>Avviso: Installazione negata per superamento della perdita di carico totale degli accessori oltre 21,0 mmH2O.</div>"
    elif 0 <= total_coax <= 5:
        image = "image1.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>tutto bene</div>"
    elif 5.1 <= total_coax <= 7.5:
        image = "image2.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>tutto bene</div>"
    elif 7.6 <= total_coax <= 10:
        image = "image3.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>tutto bene</div>"
    elif 10.1 <= total_coax <= 15:
        image = "image4.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>tutto bene</div>"
    elif 15.1 <= total_coax <= 20:
        image = "image5.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>tutto bene</div>"
    elif 20.1 <= total_coax <= 21:
        image = "image6.jpg"
        message = "<div style='font-size: 30px; text-align: center;'>tutto bene</div>"
    else:
        image = "no.png"
        message = "<div style='font-size: 30px; text-align: center;'>tutto bene</div>"

    return message, image

def placeholder_page():
    return "<div style='font-size: 30px; text-align: center;'>Coming soon...</div>", "placeholder.png"

if __name__ == "__main__":
    with gr.Blocks() as demo:
        gr.Image(value="logo.png", label="Kava e MeTTi", show_label=False, show_download_button=False, show_share_button=False)
        
        with gr.Tabs():
            with gr.Tab("AVVERTENZE GENERALI"):
                gr.Image(value="uniqa.PNG", label="Kava e MeTTi", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
**Contenuto:** Manuale, dima per montaggio, certificati, libretto d'impianto e tasselli.
### Locale d'Installazione:
- Rispetta le norme tecniche e la legislazione vigente.
- Deve avere adeguate aperture di aerazione se di “TIPO B”.
- Temperatura minima: non inferiore a -5 °C.
- verifica che la parete possa sostenere il peso della caldaia.
### Nuova Installazione o Sostituzione:
- Verifica canna fumaria, impianto elettrico, linea di adduzione del combustibile e eventuale vaso di espansione.
- Assicura che l'impianto sia pulito, lavato e a tenuta.
                """)
            with gr.Tab("DIMENSIONI E MONTAGGIO"):
                gr.Image(value="distanze.PNG", label="distanze", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
### Dimensioni e Peso:
- **Larghezza:** 400 mm
- **Profondità:** 345 mm
- **Altezza:** 700 mm
- **Peso:** 45 kg
### Montaggio:
- Utilizza la dima di carta per posizionare e forare la parete.
- Inserisci tasselli ad espansione e viti a doppia filettatura.
- Aggancia la caldaia alle viti, inserisci rondelle ammortizzanti e piane, e blocca con i dadi.
- Assicurati che la caldaia sia verticale per facilitare manutenzione e smontaggio.
                """)
            with gr.Tab("ALLACCIAMENTI E ACCESSORI"):
                gr.Image(value="allacciamenti.PNG", label="allacciamenti", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
### Trattamento Acqua Impianto:
- Utilizza acqua con pH: 6–8 e durezza < 25°f.
- Se necessario, usa un filtro di sicurezza e un sistema di trattamento chimico per proteggere dalla corrosione e incrostazioni.
### Dimensioni e Attacchi:
- Mandata Impianto (M): Ø 3/4" G
- Ritorno Impianto (R): Ø 3/4" G
- Uscita Acqua Sanitaria (U): Ø 1/2" G
- Entrata Acqua Sanitaria (E): Ø 1/2" G
- Alimentazione Gas (G): Ø 3/4" G
- Larghezza (L): 400 mm
### Alimentazione Gas
Assicurati che il tipo di gas corrisponda a quello per cui l'apparecchio è predisposto. Le caldaie sono predisposte per gas G20.
La tubazione del gas deve essere di dimensione uguale o superiore a quella del raccordo della caldaia (G 3/4”) e con perdita di carico minore o uguale alla prevista.
È consigliato l'uso di un filtro sulla linea gas per prevenire eventuali problemi.
                """)
            with gr.Tab("CONDOTTI COASSIALI"):

                gr.Image(value="coassiali.png", label="coassiali", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
- C12 Scarico fumi a parete concentrico. I tubi possono partire dalla caldaia indipendenti, ma le uscite devono essere concentriche o abbastanza vicine (entro 50 cm) da essere sottoposte a condizioni di vento simili.
- C32 Scarico concentrico a tetto. Uscite come C12.
- C42 Scarico e aspirazione in canne fumarie comuni separate ma sottoposte a simili condizioni di vento.
### VERIFICA 

                """)
                
                s90_coax = gr.Slider(0, 5, value=0, label="Curva a 90° MF", step=1)
                s45coax = gr.Slider(0, 5, value=0, label="Curva a 45° MF", step=1)
                pro_o_coax = gr.Slider(0, 10, value=0, label="Prolunga orizzontale m", step=0.1)
                pro_v_coax = gr.Slider(0, 10, value=0, label="Prolunga verticale m", step=0.1)
                calc_button = gr.Button("Calcola")
                result = gr.Markdown(label="Soluzione")
                image_display = gr.Image(label="Risultato Immagine", show_label=False, show_download_button=False, show_share_button=False)
                
                calc_button.click(
                    calculate_total_coax, 
                    inputs=[s90_coax, s45coax, pro_o_coax, pro_v_coax], 
                    outputs=[result, image_display]
                )
                gr.Image(value="coassiale.jpg", label="coassiale", show_label=False, show_download_button=False, show_share_button=False)
                gr.Image(value="coassiale2.jpg", label="coassiale2", show_label=False, show_download_button=False, show_share_button=False)    
            with gr.Tab("CONDOTTI SEPARATI"):
                gr.Image(value="separati.png", label="separati", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
- C10 Apparecchio collegato a una canna collettiva. Tale canna è costituita da due condotti con terminale coassiale. Usare clapet
- B32 Aspirazione aria comburente in ambiente e scarico fumi in canna fumaria singola. Apertura per aria comburente (15 cm2 x kW).
- C52 Scarico e aspirazione separati a parete o a tetto e comunque in zone a pressioni diverse. Lo scarico e l‘aspirazione non devono mai essere
posizionati su pareti opposte.
- C82 Scarico in canna fumaria singola o comune e aspirazione a parete.
### CALCOLO CONFIGURAZIONE DIAFRAMMA
                """)
                    
                scarico_choice = gr.Radio(["Scarico uscita sul tetto", "Scarico uscita a parete"], label="SCARICO", value="Scarico uscita sul tetto")
                s90 = gr.Slider(0, 5, value=0, label="Curva a 90° MF", step=1)
                s45 = gr.Slider(0, 5, value=0, label="Curva a 45° MF", step=1)
                pro_os = gr.Slider(0, 10, value=0, label="Prolunga orizzontale m", step=0.1)
                pro_vs = gr.Slider(0, 10, value=0, label="Prolunga verticale m", step=0.1)
            
                aspirazione_choice = gr.Radio(["Aspirazione sul tetto", "Aspirazione a parete"], label="ASPIRAZIONE", value="Aspirazione sul tetto")
                a90 = gr.Slider(0, 5, value=0, label="Curva a 90° MF", step=1)
                a45 = gr.Slider(0, 5, value=0, label="Curva a 45° MF", step=1)
                pro_oa = gr.Slider(0, 10, value=0, label="Prolunga orizzontale m", step=0.1)
                pro_va = gr.Slider(0, 10, value=0, label="Prolunga verticale m", step=0.1)

                tee = gr.Checkbox(value=False, label="Tee recupero condensa: Sì/No")
                
                calc_button = gr.Button("Calcola")
                result = gr.Markdown(label="Soluzione")
                image_display = gr.Image(label="Risultato Immagine", show_label=False, show_download_button=False, show_share_button=False)
                
                calc_button.click(
                    calculate_total, 
                    inputs=[s90, s45, pro_os, pro_vs, scarico_choice, a90, a45, pro_oa, pro_va, aspirazione_choice, tee], 
                    outputs=[result, image_display]
                )
                
            with gr.Tab("COLLEGAMENTI ELETTRICI"):
                gr.Image(value="forza.png", label="forza", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
### Utilizzare un interruttore magnetotermico conforme alle Norme EN.
- Assicurarsi che il cavo di terra sia collegato a un impianto di messa a terra efficace.
- È vietato utilizzare i tubi dell’acqua per la messa a terra.
                """)
                gr.Image(value="curvac.png", label="curva", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
### Sonda Esterna
La caldaia può collegarsi a una sonda esterna per operare a temperatura scorrevole.
La temperatura di mandata varia in base alla temperatura esterna secondo la curva climatica selezionata.
Montaggio:
Seguire le istruzioni sulla confezione per il montaggio della sonda all’esterno dell’edificio.
Selezione della Curva Climatica:
Premere il tasto 'riscaldamento' per 1 secondo e usare i tasti + o - per selezionare la curva climatica desiderata (K=0.0 ÷ K=9.0).
                """)
            with gr.Tab("RIEMPIMENTO E  SVUOTAMENTO"):
                gr.Markdown("""
Verificare che l’interruttore generale dell’impianto sia su "ON" per visualizzare la pressione sul display.
Se necessario, premere il tasto 'commutazione/reset'⏻
 per almeno 1 secondo per selezionare la modalità "Stand-by".
### Operazioni di Riempimento:
**Circuito sanitario:**
- Apri il rubinetto di intercettazione del circuito sanitario (se presente).
- Apri uno o più rubinetti dell'acqua calda per riempire e sfiatare il circuito.
- Richiudi i rubinetti dell'acqua calda una volta completato lo sfiato.
**Circuito riscaldamento:**
- Aprire le valvole di intercettazione e di sfogo aria nei punti più alti dell'impianto
- Allentare il tappo della valvola di sfiato automatica (3)
- Aprire il rubinetto di intercettazione del circuito di riscaldamento (se presente)
- Aprire il rubinetto di carico (4)
- Riempire fino alla fuoriuscita dell'acqua dalle valvole di sfogo aria e richiuderle
- Continuare il caricamento fino a raggiungere la pressione di 1-1,2 bar sul display
- Chiudere il rubinetto di carico (4)
- Sfiatare tutti i radiatori e il circuito per eliminare l'aria
- Ripetere il processo per una completa disaerazione
- Verificare e regolare la pressione sul display
- Chiudere il tappo della valvola di sfiato automatica (3)
- Rimontare il pannello anteriore della caldaia agganciandolo superiormente,
spingendolo in avanti e bloccandolo serrando le
viti (1) rimosse in precedenza.
                """)
                gr.Image(value="acqua.png", label="acqua", show_label=False, show_download_button=False, show_share_button=False)
                gr.Markdown("""
### Operazioni di SVUOTAMENTO
**Circuito sanitario:**
- Chiudere il rubinetto di intercettazione del circuito sanitario
- Aprire due o più rubinetti dell'acqua calda per svuotare il circuito.
**Caldaia:**
- Allentare il tappo della valvola di sfiato automatica (3)
- Chiudere i rubinetti di intercettazione del circuito di riscaldamento
- Verificare che il rubinetto di carico (4) sia chiuso
- Collegare una tubazione in gomma al rubinetto di scarico (7) della caldaia e aprirlo
- a svuotamento ultimato, chiudere il rubinetto di scarico (7)
Chiudere il tappo della valvola di sfiato automatica  (3).
                """)

    demo.launch()
