import requests


def get_cords(adddres):
    toponim = geo_request(adddres)
    toponym_coodrinates = toponim["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = map(float, toponym_coodrinates.split(' '))
    return toponym_longitude, toponym_lattitude


def geo_request(aaaaaaaaa: str) -> dict:
    res = requests.get('http://geocode-maps.yandex.ru/1.x/', params={
        'apikey': "40d1649f-0493-4b70-98ba-98533de7710b",
        'geocode': aaaaaaaaa,
        'format': 'json',
    })

    try:
        data = res.json()
    except RuntimeError:
        print("неа")

    # Получаем первый топоним из ответа геокодера.
    toponym = data["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]

    return toponym
