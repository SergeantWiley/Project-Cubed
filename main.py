import pygame
from player import Player
import pickle

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multiplayer Game")

clock = pygame.time.Clock()

# Create the player instance with an image
player_image_path = 'assets/stand1.png'  # Path to your player image
player = Player(x=300, y=300, image_path=player_image_path)

# Connect to the server
server_ip = '192.168.0.235'
port = 5555
player.connect_to_server(server_ip, port)

# Dictionary to hold other players' positions
other_players = {}

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_movement(keys)

    player.send_position()  # Send player's current position to the server
    other_players = player.receive_positions()  # Receive positions of other players

    screen.fill((0, 0, 0))
    player.draw(screen)  # Draw the player image

    # Draw other players using their positions
    for other_id, pos in other_players.items():
        if pos != (player.x, player.y):  # Avoid drawing the local player
            # Create another player instance for drawing
            other_player = Player(pos[0], pos[1], image_path=player_image_path)  # Use the same image
            other_player.draw(screen)  # Draw the other player's image

    pygame.display.flip()

pygame.quit()
