from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255) # [cite: 27]

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Product(models.Model):
    name = models.CharField(max_length=255) # [cite: 20]
    price = models.FloatField(default=0) # [cite: 21]
    description = models.TextField(default='') # [cite: 22]
    count = models.IntegerField(default=0) # [cite: 23]
    is_active = models.BooleanField(default=True) # [cite: 24]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products') # [cite: 25]

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count,
            'is_active': self.is_active
        }