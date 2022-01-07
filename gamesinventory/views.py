import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import gamesinventory.manager as gm
from gamesinventory.utils import success_response, simplified_game_list, game_detail
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def get_game_list(request):
    params = request.GET
    title = params.get('title', '')
    players = [int(x) for x in params.get('players', [])]
    year = int(params.get('year', 0))
    page = int(params.get('page', 1))
    limit = int(params.get('limit', 20))
    intermediate = gm.get_page(title, players, year, limit).page(page).object_list
    res = simplified_game_list(intermediate)
    return success_response(res)

@require_http_methods(["GET"])
def get_game_detail(request, game_id):
    game = gm.get_game(game_id)
    return success_response(game_detail(game))

@require_http_methods(["POST"])
def update_game(request, game_id):
    params = json.loads(request.body)
    title = params.get('title', '')
    players = [int(x) for x in params.get('players', [])]
    year = int(params.get('year', 0))
    description = params.get('description', '')
    gm.update_game(game_id, title, players, year, description)
    return success_response({})

@require_http_methods(["POST"])
def delete_game(request, game_id):
    gm.delete_game(game_id)
    return success_response({})

@require_http_methods(["POST"])
def create_game(request):
    params = json.loads(request.body)
    title = params.get('title', '')
    players = [int(x) for x in params.get('players', [])]
    year = int(params.get('year', 0))
    description = params.get('description', '')
    game_id = gm.create_game(title, players, year, description)
    return success_response({"id": game_id})

def autocomplete(request):
    return success_response({})

def autocomplete_detail(request):
    return success_response({})