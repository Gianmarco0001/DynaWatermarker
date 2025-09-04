# DynaWatermarker

This project allows you to add a **dynamic watermark to videos** in a style similar to Amazon Prime Preview. The watermark moves smoothly across the video and can be customized by the user.

---

## Features / Funzionalità

* User-defined watermark text / Watermark con testo scelto dall'utente
* Smooth sinusoidal movement across the video / Movimento dinamico sinusoidale sul video
* Preview the video with watermark / Anteprima del video con watermark
* Save the final video with watermark / Salvataggio del video finale con watermark
* Simple GUI with **Tkinter** / Interfaccia grafica semplice tramite Tkinter

---

## Requirements / Requisiti

* Python 3.10+
* [MoviePy](https://zulko.github.io/moviepy/)
* [Pillow](https://python-pillow.org/)
* Tkinter (included in standard Python)

Install required packages / Installazione pacchetti richiesti:

```bash
pip install moviepy pillow
```

---

## Usage / Utilizzo

1. Run the Python script / Avvia lo script Python:

```bash
python watermarker.py
```

2. Click **"Choose Video"** to select the video to watermark / Clicca su "Scegli Video" per selezionare il video.
3. Enter the watermark text in the text field / Inserisci il testo del watermark nella casella di testo.
4. Click **"Preview"** to see the watermark in action / Clicca su "Anteprima" per vedere il watermark.
5. Click **"Apply and Save"** to generate the final video / Clicca su "Applica e Salva" per generare il video finale.

---

## How it works / Come funziona

The watermark is created as a transparent image and overlaid on the video using `MoviePy`.
Its movement is calculated with sinusoidal functions to create a dynamic effect that is hard to remove.

Il watermark viene creato come immagine trasparente e sovrapposto al video usando `MoviePy`. 
Il suo movimento è calcolato con funzioni sinusoidali per creare un effetto dinamico difficile da rimuovere.

---

Disclaimer / Avvertenze

This software is provided as-is without any warranty. Use it responsibly.
Do not use this tool for illegal activities or to violate copyright laws.
The author is not responsible for any misuse.

Questo software è fornito così com'è, senza alcuna garanzia. Usalo responsabilmente.
Non utilizzare questo strumento per attività illegali o per violare leggi sul copyright.
L'autore non è responsabile per eventuali usi impropri.

---

## Notes / Note

* The preview does not play audio to avoid crashes / La preview non riproduce l’audio per evitare crash.
* Using `.mp4` videos is recommended for best compatibility / È consigliato utilizzare video in formato `.mp4`.
* The watermark uses system default font (`Arial`) and standard size / Il watermark utilizza font di default di sistema (`Arial`) e dimensione standard.

## License / Licenza

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.  
Questo progetto è rilasciato sotto la **MIT License** – vedi il file [LICENSE](LICENSE) per i dettagli.

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)

