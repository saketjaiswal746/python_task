from django.db import models
#create a models

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    access_count = models.PositiveIntegerField(default=0)
    retrieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title