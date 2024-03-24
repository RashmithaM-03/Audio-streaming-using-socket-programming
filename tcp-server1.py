import socket
import ssl
import os

# Function to receive a file from a connection
def receive_file(conn):
    # Use 'makefile' to create a file-like object from the connection
    with conn.makefile('rb') as file:
        # Read the filename from the connection
        filename = file.readline().strip().decode()
        # Extract file extension
        file_extension = os.path.splitext(filename)[1]
        # Create a directory to store received files if it doesn't exist
        directory = 'received_files'
        os.makedirs(directory, exist_ok=True)
        # Generate a new filename to avoid overwriting existing files
        new_filename = os.path.join(directory, f"received_file_{len(os.listdir(directory))}{file_extension}")
        # Open the new file and write received data to it
        with open(new_filename, 'wb') as f:
            while True:
                data = file.read(1024)
                if not data:
                    break
                f.write(data)
        # Print a message indicating the file has been received and saved
        print(f"File received: {filename} (saved as {new_filename})")
        return new_filename

if __name__ == '__main__':
    # Server configuration
    host = '127.0.0.1'
    port = 8080

    # Get the total number of clients from user input
    total_clients = int(input('Enter number of clients: '))

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    sock.bind((host, port))
    
    # Listen for incoming connections
    sock.listen(total_clients)

    # Establish SSL context for secure communication
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    # List to store connections with clients
    connections = []

    # Accept connections from clients
    print('Initiating clients')
    for i in range(total_clients):
        conn, addr = sock.accept()
        # Wrap the connection with SSL/TLS
        ssl_conn = context.wrap_socket(conn, server_side=True)
        connections.append(ssl_conn)
        print('Connected with client', i+1)

    # Receive the audio file from each client
    for conn in connections:
        filename = receive_file(conn)
        conn.close()

    # Close the server socket
    sock.close()
