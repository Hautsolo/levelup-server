from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event,Game,Gamer

class EventView(ViewSet):
    
    def retrieve(self, request , pk):
        event= Event.objects.get(pk=pk)
        serializer= EventSerializer(event)
        return Response(serializer.data)
    
    def list(self, request ):
        event = Event.objects.all()
        serializer= EventSerializer(event, many=True)
        return Response(serializer.data)
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized event instance
        """
        game = Game.objects.get(pk=request.data["game"])
        gamer = Gamer.objects.get(uid=request.data["organizer"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            game=game,
            organizer=gamer,
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)
    def update(self,request,pk):
        
        event=Event.objects.get(pk=pk)
        event.description=request.data["description"]
        event.date=request.data["date"]
        event.time=request.data["time"]
        
        game=Game.objects.get(pk=request.data["game"])
        event.game=game
        
        gamer=Gamer.objects.get(pk=request.data["organizer"])
        event.organizer=gamer
        
        event.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self,request,pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)


        
        
        
        
        
        
    
    
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model =Event
        fields=('id','game','description','date','time','organizer')