from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game,Gamer,GameType


class GameView(ViewSet):
    
    def retrieve(self, request , pk):
        game= Game.objects.get(pk=pk)
        serializer= GameSerializer(game)
        return Response(serializer.data)
    
    def list (self, request ):
        game= Game.objects.all()
        serializer= GameSerializer(game, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        gamer = Gamer.objects.get(uid=request.data["userId"])
        game_type = GameType.objects.get(pk=request.data["gameType"])

        game = Game.objects.create(
            title=request.data["title"],
            maker=request.data["maker"],
            number_of_players=request.data["numberOfPlayers"],
            skill_level=request.data["skillLevel"],
            game_type=game_type,
            gamer=gamer,
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)
    def update(self, request, pk):
   

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.skill_level = request.data["skillLevel"]

        game_type = GameType.objects.get(pk=request.data["gameType"])
        game.game_type = game_type
        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

    
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model =Game
        fields=('id','game_type','title','maker','gamer','number_of_players','skill_level')