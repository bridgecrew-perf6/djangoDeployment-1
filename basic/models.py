from django.db import models

# Create your models here.
# hem fiziksel veri (db) hem de arayüzde kullanılacak veriyi modelleyen nesneler
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    discount = models.FloatField(blank=True, default=0)
    

    class Meta:
        ordering =('-name',)
    
    def __str__(self) -> str:
        return self.name + " " + self.description