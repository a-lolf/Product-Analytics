from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, db_index=True)
    price = models.FloatField(db_index=True)
    stock = models.IntegerField()
    created_at = models.DateTimeField()
    
