import paho.mqtt.publish as publish
import pygame


class Publisher:
    def __init__(self):
        pass

    @staticmethod
    def send_key(key):
        publish.single("commands", key, hostname="Marocchino", client_id="commandsPub")

    @staticmethod
    def listen_to_keyboard_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Publisher.send_key('Q')

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                Publisher.send_key('L')
            if keys[pygame.K_RIGHT]:
                Publisher.send_key('R')
            if keys[pygame.K_UP]:
                Publisher.send_key('U')
            if keys[pygame.K_DOWN]:
                Publisher.send_key('D')
