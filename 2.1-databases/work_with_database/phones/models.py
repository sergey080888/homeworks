from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=1, max_digits=10)
    image = models.CharField(max_length=300)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=60, null=False, unique=True)
    def __str__(self):
        return f'{self.id}, {self.name}, {self.price}, {self.image}, {self.release_date}, {self.lte_exists}, ' \
               f'{self.slug}'

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
