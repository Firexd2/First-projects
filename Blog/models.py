from ckeditor.fields import RichTextField
from django.db import models
from PIL import Image as Im

_MAX_SIZE = 420
_MAX_SIZE_2 = 900

class Post(models.Model):

    category_list = (('programming', 'Программирование'), ('life', 'Жизнь'), ('baby', 'Малыш'), ('ali', 'Алиэкспресс'), ('thoughts', 'Мысли'), ('recipes', 'Рецепты'))

    name = models.CharField(max_length=45)
    name_url = models.CharField(max_length=45)
    date = models.DateTimeField(auto_now_add=True)
    tittle = models.CharField(max_length=45)
    text = RichTextField()
    category = models.CharField(max_length=20, choices=category_list)
    logo = models.ImageField(upload_to='post', blank=True)
    image_resize = models.CharField(max_length=1000, blank=True)
    look = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return "%s, %s, %s" % (self.date, self.tittle, self.category)

    def save(self, *args, **kwargs):

        super(Post, self).save(*args, **kwargs)

        if self.logo:
            filename = self.logo.path
            width = self.logo.width
            height = self.logo.height

            max_size = max(width, height)

            image = Im.open(filename)

            image_small = image.resize(
                (round(width / max_size * _MAX_SIZE),
                round(height / max_size * _MAX_SIZE)),
                Im.ANTIALIAS
            )

            filename_2 = filename.split('.')
            img_resize = filename_2[0] + '-2.' + filename_2[1]
            image_small.save(img_resize)

            if max_size > _MAX_SIZE_2:

                image_big = image.resize(
                        (round(width / max_size * _MAX_SIZE_2),
                        round(height / max_size * _MAX_SIZE_2)),
                        Im.ANTIALIAS
                        )

                image_big.save(filename)


    class Meta:
        get_latest_by = "date"


class Image(models.Model):

    image = models.ImageField(upload_to='image')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.image, self.pk)


    def save(self, *args, **kwargs):

        super(Image, self).save(*args, **kwargs)


        filename = self.image.path
        width = self.image.width
        height = self.image.height

        max_size = max(width, height)

        if max_size > _MAX_SIZE_2:

            _image = Im.open(filename)
            _image = _image.resize(
                (round(width / max_size * _MAX_SIZE_2),
                round(height / max_size * _MAX_SIZE_2)),
                Im.ANTIALIAS
            )

            _image.save(filename)

class InformationsClient(models.Model):

    ip = models.CharField(max_length=15, blank=True)
    name_url = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return "%s, %s" % (self.ip, self.name_url)

