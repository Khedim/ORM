# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# from django.db import models

# # Create your models here.

# # Abstract model inheritence
# # an abstract model does not get created in the db


# class BaseItem(models.Model):
#     title = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
#         ordering = ["title"]


# class ItemA(BaseItem):
#     content = models.TextField()

#     class Meta:
#         ordering = ['-created']
#         verbose_name_plural = 'Item A'

# # multi table model inheritence


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)


# class ISBN(Book):
#     ISBN = models.TextField()

#     class Meta:
#         verbose_name_plural = 'ISBN'

# # proxy model inheritence
# # didnt understand quitly it destenited to manager in the ORM and some others

# # this about to make ForeignKey without declaring the inherited from class ahead
# class Product(models.Model):
#     content_type = models.ForeignKey(
#         ContentType, on_delete=models.CASCADE, limit_choices_to={"model__in": ('book', 'cupboard')})
#     object_id = models.PositiveIntegerField()
#     item = GenericForeignKey('content_type', 'object_id')

# # using polymorphic pakage
# from polymorphic.models import PolymorphicModel

# class Product(PolymorphicModel):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

# class Book(Product):
#     author = models.CharField(max_length=100)
#     pages = models.IntegerField()

# class Furniture(Product):
#     material = models.CharField(max_length=100)
#     dimensions = models.CharField(max_length=100)
