from django.db import models
import numpy as np

# create your models here
def get_default_array():
  default_arr = np.random.rand(1536)  # Adjust this to your desired default array
  return default_arr.tobytes()


class Movie(models.Model): 
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250) 
    image = models.ImageField(upload_to='movie/images/', default = 'movie/images/default.jpg') 
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)
    year = models.IntegerField(blank=True, null=True)
    emb = models.BinaryField(null=True, blank=True)  # Añade esta línea

    def __str__(self): 
        return self.title