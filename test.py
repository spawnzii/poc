import socket

HOST = '0.0.0.ddddd'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Listening on port {PORT}...")
    conn, addr = server.accept()
    print(f"Connected by {addr}")

    with conn:
        while True:
            cmd = input("Shell> ")
            if cmd.lower() in ['exit', 'quit']:
                conn.sendall(b'exit\n')
                break
            conn.sendall((cmd + '\n').encode('utf-8'))  # <<< envoie aussi \n
            data = b""
            while True:
                chunk = conn.recv(1024)
                data += chunk
                if len(chunk) < 1024:
                    break
            print(data.decode('utf-8'))
