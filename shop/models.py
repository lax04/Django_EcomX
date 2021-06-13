from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    price = models.IntegerField(default=1)
    image = models.ImageField(upload_to = "media_files", default="")

    def __str__(self):
        return self.product_name

class Men(models.Model):
    iname = models.CharField(max_length=20)
    idesc = models.CharField(max_length=100)
    iprice = models.IntegerField(default=1)
    ipic = models.ImageField(upload_to = 'men_images', default=" ",blank=True)
    slug = models.CharField(max_length=100, default=" ")
    def __str__(self):
        return self.iname

class Women(models.Model):
    iname = models.CharField(max_length=20)
    idesc = models.CharField(max_length=100)
    iprice = models.IntegerField(default=1)
    ipics = models.ImageField(upload_to = 'women_images', default=" ",blank=True)
    slug = models.CharField(max_length=100, default=" ")
    def __str__(self):
        return self.iname

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    iurl = models.URLField(max_length=200, default=" ")
    iname = models.CharField(max_length=100)
    ipic = models.ImageField(upload_to = "orders", default = " ")
    email = models.EmailField(default=" ")
    password = models.CharField(max_length=100, default="")
    a1 = models.CharField(max_length=200, default="")
    a2 = models.CharField(max_length=200, default="")
    cod = models.BooleanField( default="False")
    

    def __str__(self):
        return self.iname
    

class upload(models.Model):
    img = models.ImageField(upload_to = "uploads",default="", blank=True)
    

class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    iname = models.CharField(max_length=20)
    idesc = models.CharField(max_length=100)
    iprice = models.IntegerField(default=1)
    ipic = models.ImageField(upload_to = 'cart', default=" ",blank=True)
    slug = models.CharField(max_length=100, default=" ") 

    def __str__(self):
        return self.iname

class update(models.Model):
    update_id = models.AutoField(primary_key=True)
    ord_id = models.IntegerField()
    update_desc = models.CharField(max_length=500)
    def __str__(self):
         return self.update_desc
       
