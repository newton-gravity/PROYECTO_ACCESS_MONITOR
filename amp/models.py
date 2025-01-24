from django.db import models

# Create your models here.

class Provincia(models.Model):
    name_provincia = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.name_provincia
    


class Municipio(models.Model):
    name_municipio = models.CharField(max_length=30)
    id_provincia =models.ForeignKey(Provincia, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return self.name_municipio



class ClientAddress(models.Model):
    house_number = models.CharField(max_length=10)
    house_street1 = models.CharField( max_length=30)
    house_street2 = models.CharField( max_length=30)
    house_street3 = models.CharField( max_length=30)
    municipio = models.ForeignKey( Municipio, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "ClientAddress"
        verbose_name_plural = "ClientAddresss"

    def __str__(self):
        number= str(self.house_number)
        street1=str(self.house_street1)
        street2 = str(self.house_street2)
        street3 = str(self.house_street3)
        municipio = self.municipio.name_municipio
        return (number + " , " + street1 +" - "+ street2+" and "+street3+" - "+municipio)



class Client(models.Model):
    
    first_name = models.CharField( blank=False, max_length=30)
    last_name = models.CharField( blank=False, max_length=30)
    alias_name = models.CharField( blank=False, max_length=30)
    client_email = models.EmailField(default=("default@defaul.org"), max_length=254)
    client_age = models.IntegerField( blank=False)
    address = models.ForeignKey(ClientAddress, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now=True)
    updateAt = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.first_name



class SuscriptionType(models.Model):

    suscription_name = models.CharField( blank = False,max_length = 50)
    suscription_cost = models.PositiveIntegerField(blank = False)
    createdAt = models.DateTimeField( auto_now=True)
    updatedAT = models.DateTimeField( auto_now_add=True)    

    class Meta:
        verbose_name = ("SuscriptionType")
        verbose_name_plural = ("SuscriptionTypes")

    def __str__(self):
        return self.suscription_name

   

class Suscription(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    suscription_status = models.BooleanField( blank = False, default = False) 
    suscription_type = models.ForeignKey(SuscriptionType, on_delete=models.CASCADE)
    start_date = models.DateTimeField( auto_now_add=True)  
    end_date = models.DateTimeField( auto_now_add=False) 
    

    class Meta:
        verbose_name = ("Suscription")
        verbose_name_plural = ("Suscriptions")

    def __str__(self):
        client = str(self.client_id)
        suscription = str(self.suscription_type)
        date = str(self.start_date)+ " " + str(self.end_date)
        return (client +" "+ suscription +" "+ date)


class GameCategory(models.Model):
    name = models.CharField(blank=False, max_length=30)
    

    class Meta:
        verbose_name = ("GameCategory")
        verbose_name_plural =("GameCategorys")

    def __str__(self):
        return self.name

    

class Game(models.Model):
    game_name = models.CharField(blank=False, max_length=50)
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    description = models.TextField((""))
    image = models.ImageField( default="static/cardgb.jpeg")
    launch_date = models.DateField( auto_now=False)
    developer = models.CharField( max_length=50)

    class Meta:
        verbose_name = ("Game")
        verbose_name_plural =  ("Games")
   
    def __str__(self):
        return self.game_name

    
    

      


    

