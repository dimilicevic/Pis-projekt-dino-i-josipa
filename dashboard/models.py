from django.db import models
from datetime import datetime  
 
class Firma(models.Model):
    """
    Reprezentacija modela 'Firma' i prikaz atributa.

    Attributes:
        - naziv_firme (CharField): Naziv firme koji je objavio oglas.
        - opis (str): Opis firme.
        - industrija (str): Industrija.
    """

    naziv_firme = models.CharField(max_length=50)
    opis = models.CharField(max_length=200)
    industrija = models.CharField(max_length=50)
    image = models.ImageField(default = "images/default.png",upload_to="./images")

    class Meta:
        ordering = ("naziv_firme",)
        verbose_name = "Firma"
        verbose_name_plural = "Firme"

    def __str__(self):
        return self.naziv_firme

class Posao(models.Model):
    """
    Model koji reprezentira model Posao.
    Atributi:
        - naziv_posla (str): Ime Posla.
        - opis_posla (str): Opis posla.
        - placa (int): Placa posla.
        - lokacija (str): Gdje se posao radi.
        - kontakt (emal): Email kontakt firme
    """

    naziv_posla = models.CharField(max_length=50)
    opis_posla = models.TextField()
    placa = models.PositiveBigIntegerField()
    lokacija = models.CharField(max_length=50)
    kontakt_osobe = models.EmailField(max_length=50)
    firma = models.ForeignKey(Firma, on_delete=models.CASCADE)
    datum_izrade= models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(default = "images/default.png",upload_to="images")
    
    class Meta:
        ordering = ("naziv_posla",)
        verbose_name = "Posao"
        verbose_name_plural = "Poslovi"

    def __str__(self):
        return self.naziv_posla

