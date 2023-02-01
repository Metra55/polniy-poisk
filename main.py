from sys import argv
import os
import pygame
import requests

from geo_api import get_cords

top = " ".join(argv[1:])
if not top:
    print("Чё-то надо ввести -_-")
    exit()
lat, lon = get_cords(top)


def show_map(ll: tuple[float, float], spn: [float, float], map_type: str):
    res = requests.get('http://geocode-maps.yandex.ru/1.x/', params={
        'll': ','.join(map(str, ll)),
        'spn': ','.join(map(str, spn)),
        'l': map_type,
    })

    with open('map.png', 'wb') as file:
        file.write(res.content)

    pygame.init()
    screen=pygame.display.set_mode((400,400))
    screen.blit(pygame.image.load('map.png'))
    pygame.display.flip()
    while pygame.event.wait().type !=pygame.QUIT:
        pass

    pygame.quit()
    os.remove('map.png')


show_map((lat, lon), (0.005, 0.005), "map")
