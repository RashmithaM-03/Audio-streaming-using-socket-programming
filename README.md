# Audio-streaming-using-socket-programming
Secure Audio Streaming Application:
  The Secure Audio Streaming Application is a Python-based client-server application that enables users to stream and transfer audio files securely over a network. 
  The project utilizes TCP/IP sockets for communication and implements SSL/TLS encryption to ensure data privacy and integrity during transmission.

Key Features:
  Secure Communication: 
    Utilizes SSL/TLS encryption to establish a secure channel between the server and clients, protecting audio data from eavesdropping and tampering.

Client-Server Architecture:

  Server Side: The server hosts audio files and awaits connections from clients. Upon connection, it receives audio files from clients and saves them securely.
  Client Side: Clients connect to the server using SSL/TLS-encrypted sockets and can request audio files to stream or transfer securely.

Audio Streaming:
  Clients can stream audio files from the server in real-time, enabling uninterrupted playback without the need for complete file downloads. The server facilitates     streaming by sending audio data to clients as requested.

File Transfer:
  The server supports secure file transfer of audio files to clients. Upon client request, the server sends the requested audio file securely using SSL/TLS-encrypted   sockets, ensuring confidentiality and integrity during transmission. Clients can then save the received files securely on their local systems.

User Interface (Client): 
    Provides a graphical user interface (GUI) for clients to interact with the application, including options for selecting and playing audio files, pausing/resuming   playback, and setting sleep timers.

Installation:
  To use the Secure Audio Streaming Application, follow these steps:

Clone the repository to your local machine:
  bash
  git clone https://github.com/RashmithaM-03/Audio-streaming-using-socket-programming.git

Install the required dependencies using pip:
  pip install pygame

Run the server script to start the server:
  python tcp-server1.py

Run the client script to start the client application:
  python tcp-client1.py

Usage:
  Start the server by running tcp-server1.py.
  Launch the client application by running tcp-client1.py.
  Use the graphical user interface (GUI) provided by the client to interact with the application:
  Select audio files from the server directory.
  Play, pause, or resume audio playback.
  Set sleep timers to pause audio playback after a specified duration.

Here's a step-by-step guide to creating server.key and server.crt files using OpenSSL:
Generate a Private Key (server.key):
  Run the following OpenSSL command to generate a private key:
    openssl genpkey -algorithm RSA -out server.key -aes256
You will be prompted to enter a passphrase to protect the private key.

Create a Certificate Signing Request (CSR):
  Use the private key to generate a CSR:
    openssl req -new -key server.key -out server.csr
You will be prompted to enter information about your organization and the server.

Generate a Self-Signed Certificate (server.crt):
  Now, create a self-signed certificate using the CSR:
    openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
This command creates a self-signed certificate valid for 365 days.

After running these commands, you will have the server.key and server.crt files generated and ready to use for SSL/TLS encryption in your server application. Make sure to keep the private key (server.key) secure, as it is essential for securing communications between your server and clients.


INSTRUCTIONS TO INSTALL OPENSSL:
For Windows:
Download OpenSSL:  
  Go to the OpenSSL downloads page and download the appropriate version of OpenSSL for Windows.

Install OpenSSL: 
  Run the downloaded installer and follow the installation wizard. Make sure to select the option to add OpenSSL to your system PATH during installation.

Verify Installation: 
  Open Command Prompt and type openssl version to verify that OpenSSL is installed correctly. You should see the version information if it's installed successfully.






