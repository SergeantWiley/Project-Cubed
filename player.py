import pygame
import socket
import pickle

class Player:
    def __init__(self, x, y, image_path, width=300, height=300):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.server = None  # Add a socket for communication with the server
        self.image = self.load_image(image_path)

    def load_image(self, image_path):
        """Loads and resizes the image to the specified width and height."""
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (self.width, self.height))

    def draw(self, screen):
        """Draws the player (image) on the screen."""
        screen.blit(self.image, (self.x, self.y))

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
