import socket  # Import the socket module for network communication
import ssl  # Import the SSL module for secure communication
import os  # Import the OS module for interacting with the operating system
import threading  # Import threading for handling concurrency
import pygame  # Import pygame for audio playback
import tkinter as tk  # Import tkinter for GUI creation

# Server configuration
HOST = '127.0.0.1'  # Change this to the hostname or IP address of your server
PORT = 8080  # Specify the port number for communication
CERTFILE = 'server.crt'  # Path to the server's SSL certificate file

def send_file(conn, filename):
    """
    Function to send a file over the connection.
    
    Parameters:
        conn (socket.socket): The socket connection.
        filename (str): The name of the file to be sent.
    """
    with conn.makefile('wb') as file:
        file.write(filename.encode() + b'\n')  # Write the filename to the connection
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)  # Read data from the file in chunks
                if not data:
                    break
                file.write(data)  # Write the data to the connection
        print(f"File '{filename}' sent.")  # Print a message indicating the file has been sent

def list_files():
    """
    Function to list all files in the current directory.
    
    Returns:
        list: A list of filenames.
    """
    files = os.listdir('.')  # Get a list of files in the current directory
    return files

def start_audio(filename):
    """
    Function to start playing an audio file.
    
    Parameters:
        filename (str): The name of the audio file to play.
    """
    pygame.init()  # Initialize the Pygame library
    pygame.mixer.init()  # Initialize the mixer module for audio playback
    pygame.mixer.music.load(filename)  # Load the specified audio file
    pygame.mixer.music.play()  # Start playing the audio

def pause_audio():
    """Function to pause the currently playing audio."""
    pygame.mixer.music.pause()  # Pause the audio playback

def resume_audio():
    """Function to resume the paused audio playback."""
    pygame.mixer.music.unpause()  # Resume the paused audio playback

def set_timer_to_pause_audio(filename, delay):
    """
    Function to set a timer to pause audio playback after a specified delay.
    
    Parameters:
        filename (str): The name of the audio file.
        delay (float): The delay in seconds before pausing the audio.
    """
    threading.Timer(delay, pause_audio).start()  # Create a timer to pause audio playback after the delay

def handle_send_button(filename_entry, client_socket):
    """
    Function to handle sending a file when the 'Send File' button is clicked.
    
    Parameters:
        filename_entry (tk.Entry): The entry field containing the filename.
        client_socket (socket.socket): The client socket for communication.
    """
    filename = filename_entry.get()  # Get the filename from the entry field
    send_file(client_socket, filename)  # Send the file to the client

def handle_play_button(filename_entry):
    """
    Function to handle playing an audio file when the 'Play' button is clicked.
    
    Parameters:
        filename_entry (tk.Entry): The entry field containing the filename.
    """
    filename = filename_entry.get()  # Get the filename from the entry field
    start_audio(filename)  # Start playing the audio file

def handle_pause_button():
    """Function to handle pausing audio playback when the 'Pause' button is clicked."""
    pause_audio()  # Pause the audio playback

def handle_resume_button():
    """Function to handle resuming audio playback when the 'Resume' button is clicked."""
    resume_audio()  # Resume the paused audio playback

def handle_timer_button(filename_entry, delay_entry):
    """
    Function to handle setting a timer for pausing audio playback when the 'Pause Audio (as per timer)' button is clicked.
    
    Parameters:
        filename_entry (tk.Entry): The entry field containing the filename.
        delay_entry (tk.Entry): The entry field containing the delay time.
    """
    filename = filename_entry.get()  # Get the filename from the entry field
    delay = float(delay_entry.get())  # Get the delay from the entry field
    set_timer_to_pause_audio(filename, delay)  # Set a timer to pause audio playback

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket with SSL/TLS
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)  # Create SSL context for server authentication
context.load_verify_locations(CERTFILE)  # Load the server's SSL certificate
client_socket = context.wrap_socket(client_socket, server_hostname=HOST)  # Wrap the socket with SSL/TLS

# Create GUI
root = tk.Tk()  # Create the main Tkinter window
root.title("Audio Player")  # Set the title of the window

# List of files in directory
files_frame = tk.Frame(root)  # Create a frame for file list display
files_frame.grid(row=2, column=2, rowspan=6, padx=10)  # Set the position and size of the frame
files_label = tk.Label(files_frame, text="Files in Server directory:")  # Label for file list
files_label.pack(side=tk.TOP)  # Position the label at the top of the frame
files_scrollbar = tk.Scrollbar(files_frame)  # Create a scrollbar for file list
files_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Position the scrollbar on the right side of the frame
files_listbox = tk.Listbox(files_frame, height=20, width=70, yscrollcommand=files_scrollbar.set)  # Create a listbox for file display
files_listbox.pack(side=tk.LEFT)  # Position the listbox on the left side of the frame
for file in list_files():
    files_listbox.insert(tk.END, file)  # Insert each file into the listbox
files_scrollbar.config(command=files_listbox.yview)  # Configure the scrollbar to scroll the listbox

# Filename entry
filename_label = tk.Label(root, text="Enter filename:")  # Label for filename entry
filename_label.grid(row=2, column=4, sticky="e")  # Set the position of the label
filename_entry = tk.Entry(root)  # Create an entry field for filename input
filename_entry.grid(row=2, column=5, sticky="w")  # Set the position of the entry field

# Buttons
play_button = tk.Button(root, text="Play", command=lambda: handle_play_button(filename_entry))  # Button to play audio
play_button.grid(row=3, column=4, columnspan=2, sticky="ew")  # Set the position of the button

pause_button = tk.Button(root, text="Pause", command=handle_pause_button)  # Button to pause audio
pause_button.grid(row=4, column=4, columnspan=2, sticky="ew")  # Set the position of the button

resume_button = tk.Button(root, text="Resume", command=handle_resume_button
