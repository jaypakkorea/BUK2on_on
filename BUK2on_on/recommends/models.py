from django.db import models
from django.template.defaultfilters import slugify

class Restaurant(models.Model):
    province = (('1','Seoul'),('2','Busan'),('3','etc.'))
    region = models.CharField(max_length=20, choices=province)
    adress = models.CharField(max_length=1000)
    name = models.CharField(max_length = 200)
    stars = models.IntegerField()
    bestMenu = models.CharField(max_length=200)
    reason = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name
    
def get_image_filename(instance, filename):
    name = instance.restaurant.name
    slug = slugify(name)
    return "restaurant_images/%s-%s" % (slug, filename)  



class Images(models.Model):
    restaurant = models.ForeignKey(Restaurant, default=None,on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to=get_image_filename, null=False, blank=False)

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    def __str__(self):
       return str(self.restaurant)