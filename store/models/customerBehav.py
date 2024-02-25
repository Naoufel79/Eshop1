from django.db import models
from . import Customer
from . import Products

class customerBehav(models.Model):
    idcustomer=models.ForeignKey(Customer, on_delete=models.CASCADE)  
    idproduct=models.ForeignKey(Products, on_delete=models.CASCADE)

    
    #to save the data
    def register(self):
        self.save()

