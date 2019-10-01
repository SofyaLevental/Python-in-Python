import paho.mqtt.publish as publish
import pygame

from samples.utils import HOSTNAME


class Publisher:
    @staticmethod
    def __send_key(key):
        publish.single("commands", key, hostname=HOSTNAME, client_id="commandsPub")

    @staticmethod
    def listen_to_keyboard_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Publisher.__send_key('Q')

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                Publisher.__send_key('L')
            if keys[pygame.K_RIGHT]:
                Publisher.__send_key('R')
            if keys[pygame.K_UP]:
                Publisher.__send_key('U')
            if keys[pygame.K_DOWN]:
                Publisher.__send_key('D')
