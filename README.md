# Audio-streaming-using-socket-programming
Secure Audio Streaming Application:
  The Secure Audio Streaming Application is a Python-based client-server application that enables users to stream and transfer audio files securely over a network. 
  The project utilizes TCP/IP sockets for communication and implements SSL/TLS encryption to ensure data privacy and integrity during transmission.

Key Features:
  Secure Communication: 
    Utilizes SSL/TLS encryption to establish a secure channel between the server and clients, protecting audio data from eavesdropping and tampering.

  Client-Server Architecture: 
    Follows a client-server architecture where the server hosts audio files, and clients can connect to the server to stream and download these files securely.

  Audio Streaming: 
    Clients can stream audio files from the server in real-time, allowing for seamless playback without the need for complete file downloads.

  File Transfer: 
    Supports the transfer of audio files from the server to clients securely, ensuring that the transferred files remain confidential and unaltered during transit.

  User Interface (Client): 
    Provides a graphical user interface (GUI) for clients to interact with the application, including options for selecting and playing audio files, pausing/resuming playback, and setting sleep timers.

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
