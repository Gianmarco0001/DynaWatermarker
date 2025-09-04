import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os
import math

# =======================
# Funzioni Watermark
# =======================

def scegli_video():
    global video_path
    video_path = filedialog.askopenfilename(
        title="Seleziona un video",
        filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
    )
    if video_path:
        label_video.config(text=f"Video selezionato: {os.path.basename(video_path)}")

def crea_watermark_piccolo(text):
    """Crea un'immagine piccola con il testo del watermark"""
    img = Image.new("RGBA", (300, 50), (0,0,0,0))  # dimensione fissa
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()
    draw.text((0,0), text, font=font, fill=(255,255,255,180))
    return np.array(img)

def watermark_dinamico(clip, text):
    w, h = clip.w, clip.h
    wm_img = crea_watermark_piccolo(text)

    # posizione in movimento sinusoidale
    def posizione(t):
        x = int((w - 300) * 0.1 + (w - 300) * 0.8 * abs(math.sin(t*0.5)))
        y = int((h - 50) * 0.1 + (h - 50) * 0.8 * abs(math.cos(t*0.7)))
        return (x, y)

    wm_clip = (ImageClip(wm_img, transparent=True)
               .set_duration(clip.duration)
               .set_position(posizione))

    return CompositeVideoClip([clip, wm_clip])

# =======================
# Funzioni GUI
# =======================

def anteprima_watermark():
    if not video_path:
        messagebox.showerror("Errore", "Seleziona prima un video.")
        return

    text = entry_testo.get()
    if not text:
        messagebox.showerror("Errore", "Inserisci un testo per il watermark.")
        return

    clip = VideoFileClip(video_path).subclip(0, min(5, VideoFileClip(video_path).duration))
    final = watermark_dinamico(clip, text)

    # preview senza audio per evitare crash
    final.preview(audio=False)

def applica_watermark():
    if not video_path:
        messagebox.showerror("Errore", "Seleziona prima un video.")
        return

    text = entry_testo.get()
    if not text:
        messagebox.showerror("Errore", "Inserisci un testo per il watermark.")
        return

    clip = VideoFileClip(video_path)
    final = watermark_dinamico(clip, text)

    output_path = filedialog.asksaveasfilename(
        defaultextension=".mp4",
        filetypes=[("MP4 files", "*.mp4")],
        title="Salva il video con watermark"
    )

    if output_path:
        final.write_videofile(output_path, codec="libx264", audio_codec="aac")
        messagebox.showinfo("Completato", f"Video salvato come:\n{output_path}")

# =======================
# GUI Tkinter
# =======================

root = tk.Tk()
root.title("Video Watermarker Dinamico")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

btn_video = tk.Button(frame, text="Scegli Video", command=scegli_video)
btn_video.pack(pady=5)

label_video = tk.Label(frame, text="Nessun video selezionato")
label_video.pack(pady=5)

entry_testo = tk.Entry(frame, width=40)
entry_testo.pack(pady=5)
entry_testo.insert(0, "Watermark di prova")

btn_preview = tk.Button(frame, text="Anteprima", command=anteprima_watermark)
btn_preview.pack(pady=5)

btn_apply = tk.Button(frame, text="Applica e Salva", command=applica_watermark)
btn_apply.pack(pady=5)

root.mainloop()
