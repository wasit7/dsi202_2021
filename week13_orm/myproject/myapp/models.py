from django.db import models

class Bike(models.Model):
    start=models.DateField(auto_now=False, auto_now_add=True)
    type=models.CharField(max_length=20)
    price=models.DecimalField( max_digits=8, decimal_places=2)

    def __str__(self):
        return "Bike id:%s, start:%s type:%s price:%s"\
            %(self.id,self.start,self.type,self.price)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bike', args=[str(self.id)])