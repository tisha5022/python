import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pygame import mixer
import os
from mutagen.mp3 import MP3
import time
import threading
import random

# Initialize mixer
mixer.init()

root = tk.Tk()
root.title("🎶 Tkinter Music Player")
root.geometry("650x520")
root.config(bg="#0D0D0D")

current_song = None
paused = False
stopped = False
song_length = 0
visualizer_running = False


# -------- Functions -------- #
def load_music():
    global current_song
    file_path = filedialog.askopenfilename(
        title="Select Music File",
        filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav"))
    )
    if file_path:
        current_song = file_path
        song_label.config(text=f"🎵 {os.path.basename(file_path)}")
        play_music()


def play_music():
    global current_song, paused, stopped, song_length, visualizer_running
    if not current_song:
        messagebox.showwarning("No File", "Please select a music file first!")
        return

    stopped = False
    if paused:
        mixer.music.unpause()
        paused = False
        play_btn.config(text="⏸ Pause")
    else:
        mixer.music.load(current_song)
        mixer.music.play()
        play_btn.config(text="⏸ Pause")
        visualizer_running = True
        show_time_thread()
        start_visualizer()


def pause_music():
    global paused
    if paused:
        mixer.music.unpause()
        paused = False
        play_btn.config(text="⏸ Pause")
    else:
        mixer.music.pause()
        paused = True
        play_btn.config(text="▶️ Resume")


def stop_music():
    global paused, stopped, visualizer_running
    mixer.music.stop()
    paused = False
    stopped = True
    visualizer_running = False
    play_btn.config(text="▶️ Play")
    progress_bar['value'] = 0
    current_time_label.config(text="00:00")
    total_time_label.config(text="00:00")
    visualizer_canvas.delete("all")


def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)


def show_time_thread():
    threading.Thread(target=update_time, daemon=True).start()


def update_time():
    global song_length
    song = MP3(current_song)
    song_length = song.info.length
    total_time_label.config(text=time.strftime("%M:%S", time.gmtime(song_length)))

    current_time = 0
    while current_time <= song_length and not stopped:
        if paused:
            time.sleep(0.5)
            continue
        mins, secs = divmod(current_time, 60)
        current_time_label.config(text=f"{int(mins):02d}:{int(secs):02d}")
        progress = (current_time / song_length) * 100
        progress_bar['value'] = progress
        time.sleep(1)
        current_time += 1


# -------- 3D Visualizer -------- #
def start_visualizer():
    threading.Thread(target=animate_visualizer, daemon=True).start()


def animate_visualizer():
    global visualizer_running
    colors = ["#FF3CAC", "#784BA0", "#2B86C5", "#00FFC6", "#FFD700", "#FF6347"]

    while visualizer_running:
        visualizer_canvas.delete("all")
        width = visualizer_canvas.winfo_width()
        height = visualizer_canvas.winfo_height()

        bar_width = 15
        num_bars = width // (bar_width + 5)

        for i in range(num_bars):
            bar_height = random.randint(20, height)
            x0 = i * (bar_width + 5)
            y0 = height - bar_height
            x1 = x0 + bar_width
            y1 = height
            color = random.choice(colors)
            visualizer_canvas.create_rectangle(x0, y0, x1, y1, fill=color, width=0)

        root.update_idletasks()
        time.sleep(0.15)


# -------- UI Design -------- #
title_label = tk.Label(root, text="🎧 Stylish Music Player", font=("Helvetica", 22, "bold"),
                       bg="#0D0D0D", fg="#00FFD5")
title_label.pack(pady=20)

song_label = tk.Label(root, text="No music selected", font=("Helvetica", 12),
                      bg="#0D0D0D", fg="white")
song_label.pack(pady=10)

# Buttons
frame = tk.Frame(root, bg="#0D0D0D")
frame.pack(pady=20)

open_btn = tk.Button(frame, text="📂 Open", command=load_music, font=("Arial", 12, "bold"),
                     bg="#3A86FF", fg="white", width=9, relief="flat")
open_btn.grid(row=0, column=0, padx=10)

play_btn = tk.Button(frame, text="▶️ Play", command=play_music, font=("Arial", 12, "bold"),
                     bg="#00FF7F", fg="black", width=9, relief="flat")
play_btn.grid(row=0, column=1, padx=10)

pause_btn = tk.Button(frame, text="⏸ Pause", command=pause_music, font=("Arial", 12, "bold"),
                      bg="#FFD700", fg="black", width=9, relief="flat")
pause_btn.grid(row=0, column=2, padx=10)

stop_btn = tk.Button(frame, text="⏹ Stop", command=stop_music, font=("Arial", 12, "bold"),
                     bg="#FF4D6D", fg="white", width=9, relief="flat")
stop_btn.grid(row=0, column=3, padx=10)

# Progress bar
progress_frame = tk.Frame(root, bg="#0D0D0D")
progress_frame.pack(pady=10)

current_time_label = tk.Label(progress_frame, text="00:00", bg="#0D0D0D", fg="white", font=("Arial", 10))
current_time_label.grid(row=0, column=0, padx=5)

progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=350, mode="determinate")
progress_bar.grid(row=0, column=1, padx=10)

total_time_label = tk.Label(progress_frame, text="00:00", bg="#0D0D0D", fg="white", font=("Arial", 10))
total_time_label.grid(row=0, column=2, padx=5)

# Visualizer Canvas
visualizer_canvas = tk.Canvas(root, bg="#000", height=180, width=550, highlightthickness=0)
visualizer_canvas.pack(pady=20)

# Volume control
vol_label = tk.Label(root, text="🔊 Volume", font=("Helvetica", 12), bg="#0D0D0D", fg="white")
vol_label.pack()

volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal", command=set_volume,
                         length=200, bg="#0D0D0D", fg="white", highlightthickness=0)
volume_slider.set(70)
volume_slider.pack()

# Footer
tk.Label(root, text="🎶 Made with ❤️ using Tkinter & Pygame", bg="#0D0D0D",
         fg="#999", font=("Arial", 10)).pack(side="bottom", pady=10)

root.mainloop()