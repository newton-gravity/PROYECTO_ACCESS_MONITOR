from django.contrib import admin
from .models import (Provincia,Municipio, Client,ClientAddress, Suscription, SuscriptionType, Game, GameCategory)

# Register your models here.
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Client)
admin.site.register(ClientAddress)
admin.site.register(Suscription)
admin.site.register(SuscriptionType)
admin.site.register(GameCategory)
admin.site.register(Game)
