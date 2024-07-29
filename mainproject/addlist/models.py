from django.db import models

class Products(models.Model):
    productname = models.CharField(max_length=300)
    productprice = models.IntegerField()
    productdescription = models.TextField()
    productimage = models.ImageField(upload_to="product_images/",default="none")