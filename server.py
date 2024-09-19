import socket
import threading
import pickle

# Server setup
HOST = '127.0.0.1'
PORT = 5555

players = {}

def handle_client(conn, addr, player_id):
    global players
    print(f"Player {player_id} connected from {addr}")
    
    conn.send(pickle.dumps(players))

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            position = pickle.loads(data)
            players[player_id] = position
            print(f"Updated Player {player_id} position: {position}")

            for player_conn in clients:
                player_conn.sendall(pickle.dumps(players))

        except Exception as e:
            print(f"Error handling client {player_id}: {e}")
            break

    print(f"Player {player_id} disconnected")
    conn.close()

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server started, listening on {HOST}:{PORT}")

    clients = []

    while True:
        conn, addr = server.accept()
        player_id = len(players) + 1
        players[player_id] = (0, 0)

        clients.append(conn)

        thread = threading.Thread(target=handle_client, args=(conn, addr, player_id))
        thread.start()

except Exception as e:
    print(f"Server error: {e}")
finally:
    server.close()
