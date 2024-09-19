import pygame
from player import Player
import pickle

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multiplayer Game")

clock = pygame.time.Clock()
player = Player(x=100, y=100)

server_ip = '127.0.0.1'
port = 5555
player.connect_to_server(server_ip, port)
other_players = {}

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.handle_movement(keys)

    player.send_position()
    other_players = player.receive_positions()
    screen.fill((0, 0, 0))
    player.draw(screen)

    for other_id, pos in other_players.items():
        if pos != (player.x, player.y):
            pygame.draw.rect(screen, (0, 255, 0), (pos[0], pos[1], 50, 50))

    pygame.display.flip()

pygame.quit()
