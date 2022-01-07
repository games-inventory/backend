from django.http import JsonResponse


def success_response(content):
    return JsonResponse({'data': content})

def simplified_game_list(intermediate):
    return [{"id": game.id, "title": game.title, "year": game.year, "players": sorted(game.players)} for game in intermediate]

def game_detail(game):
    return {"id": game.id, "title": game.title, "year": game.year, "players": sorted(game.players), "description": game.description}