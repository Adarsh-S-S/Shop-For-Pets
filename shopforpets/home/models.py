from django.db import models

class PetProduct(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    qty=models.IntegerField()
    img=models.ImageField(upload_to="pic")
    desc=models.TextField()
    discount=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)
