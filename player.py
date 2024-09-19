import pygame
import socket
import pickle

class Player:
    def __init__(self, x, y, width=50, height=50, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = 5
        self.server = None  # Add a socket for communication with the server

    def draw(self, screen):
        """Draws the player (square) on the screen."""
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def handle_movement(self, keys):
        """Handles player movement using arrow keys."""
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def connect_to_server(self, server_ip, port):
        """Connects to the game server."""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((server_ip, port))

    def send_position(self):
        """Sends the current position to the server."""
        if self.server:
            data = pickle.dumps((self.x, self.y))
            self.server.sendall(data)

    def receive_positions(self):
        """Receives updated positions of all players from the server."""
        if self.server:
            data = self.server.recv(1024)
            positions = pickle.loads(data)
            print(positions)
            return positions
        return {}
