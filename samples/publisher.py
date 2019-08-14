import paho.mqtt.publish as publish
import pygame


class Publisher:
    topic = "keys"

    def __init__(self):
        pass

    def send_key(self, key):
        publish.single(self.topic, key, hostname="Marocchino")

    def listen_to_keyboard_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.send_key('Q')

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.send_key('L')
            if keys[pygame.K_RIGHT]:
                self.send_key('R')
            if keys[pygame.K_UP]:
                self.send_key('U')
            if keys[pygame.K_DOWN]:
                self.send_key('D')
