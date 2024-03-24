import socket
import ssl
import os
import threading
import pygame
import tkinter as tk

# Server configuration
HOST = '127.0.0.1'  # Change this to the hostname or IP address of your server
PORT = 8080
CERTFILE = 'server.crt'

def send_file(conn, filename):
    with conn.makefile('wb') as file:
        file.write(filename.encode() + b'\n')
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                file.write(data)
        print(f"File '{filename}' sent.")

def list_files():
    files = os.listdir('.')
    return files

def start_audio(filename):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def pause_audio():
    pygame.mixer.music.pause()

def resume_audio():
    pygame.mixer.music.unpause()

def set_timer_to_pause_audio(filename, delay):
    threading.Timer(delay, pause_audio).start()

def handle_send_button(filename_entry, client_socket):
    filename = filename_entry.get()
    send_file(client_socket, filename)

def handle_play_button(filename_entry):
    filename = filename_entry.get()
    start_audio(filename)

def handle_pause_button():
    pause_audio()

def handle_resume_button():
    resume_audio()

def handle_timer_button(filename_entry, delay_entry):
    filename = filename_entry.get()
    delay = float(delay_entry.get())  # Get delay from the entry field
    set_timer_to_pause_audio(filename, delay)

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL/TLS
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(CERTFILE)
client_socket = context.wrap_socket(client_socket, server_hostname=HOST)

# Create GUI
root = tk.Tk()
root.title("Audio Player")

# List of files in directory
files_frame = tk.Frame(root)
files_frame.grid(row=2, column=2, rowspan=6, padx=10)
files_label = tk.Label(files_frame, text="Files in Server directory:")
files_label.pack(side=tk.TOP)
files_scrollbar = tk.Scrollbar(files_frame)
files_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
files_listbox = tk.Listbox(files_frame, height=20, width=70, yscrollcommand=files_scrollbar.set)
files_listbox.pack(side=tk.LEFT)
for file in list_files():
    files_listbox.insert(tk.END, file)
files_scrollbar.config(command=files_listbox.yview)

# Filename entry
filename_label = tk.Label(root, text="Enter filename:")
filename_label.grid(row=2, column=4, sticky="e")
filename_entry = tk.Entry(root)
filename_entry.grid(row=2, column=5, sticky="w")

# Buttons
'''send_button = tk.Button(root, text="Send File", command=lambda: handle_send_button(filename_entry, client_socket))
send_button.grid(row=2, column=1, columnspan=2, sticky="ew")'''

play_button = tk.Button(root, text="Play", command=lambda: handle_play_button(filename_entry))
play_button.grid(row=3, column=4, columnspan=2, sticky="ew")

pause_button = tk.Button(root, text="Pause", command=handle_pause_button)
pause_button.grid(row=4, column=4, columnspan=2, sticky="ew")

resume_button = tk.Button(root, text="Resume", command=handle_resume_button)
resume_button.grid(row=5, column=4, columnspan=2, sticky="ew")

# Seconds entry for timer
delay_label = tk.Label(root, text="Enter seconds for sleep timer:")
delay_label.grid(row=6, column=4, sticky="e")
delay_entry = tk.Entry(root)
delay_entry.grid(row=6, column=5, sticky="w")

timer_button = tk.Button(root, text="Pause Audio(as per timer)", command=lambda: handle_timer_button(filename_entry, delay_entry))
timer_button.grid(row=7, column=4, columnspan=2, sticky="ew")

# Run GUI
root.mainloop()

# Close the connection
client_socket.close()