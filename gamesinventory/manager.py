from django.core.paginator import Paginator

from gamesinventory.models import Game


def get_page(title, players, year, limit):
    res = Game.objects.all()
    if title:
        res.filter(title__contains=title)
    if players:
        res.filter(players__contains=players)
    if year:
        res.filter(year__exact=year)
    pg = Paginator(res, limit)
    return pg


def get_game(game_id):
    return Game.objects.get(id=game_id)


def update_game(game_id, title, players, year, description):
    g = Game.objects.filter(id__exact=game_id)
    if title:
        g.update(title=title)
    if players:
        g.update(players=players)
    if year:
        g.update(year=year)
    if description:
        g.update(description=description)


def create_game(title, players, year, description):
    g = Game.objects.create(title=title, players=players, year=year, description=description)
    return g.id

def delete_game(game_id):
    Game.objects.filter(id=game_id).delete()