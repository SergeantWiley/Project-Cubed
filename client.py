import socket
import pygame

player_name = input("Enter your username: ")
password = input("Enter your password: ")

player_x, player_y = 100, 100

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

# Step 1: Send login details
login_data = f"{player_name},{password}".encode('utf-8')
client.sendall(login_data)

# Step 2: Receive login response
response = client.recv(1024).decode('utf-8')
if response == "SUCCESS":
    print("Logged in successfully!")
else:
    print("Login failed.")
    client.close()
    exit()

def send_player_data():
    """Send player position to server."""
    client.sendall(f"{player_name},{player_x},{player_y}".encode('utf-8'))

def receive_data():
    """Receive other players' data from server."""
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            print(f"Received: {data}")
        except:
            print("Connection closed.")
            break

import threading
receive_thread = threading.Thread(target=receive_data)
receive_thread.start()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Send player position to server
    send_player_data()

    # Update display
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, 50, 50))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
client.close()
