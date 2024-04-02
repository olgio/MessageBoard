from django.contrib.auth.models import User
from django.core import validators
from django.core.cache import cache
from django.db import models
from django.db.models import CheckConstraint, Q
from ckeditor.fields import RichTextField

class Section(models.Model):
    name = models.CharField(verbose_name="Имя раздела", max_length=255)
    number_post = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"


class Subsection(models.Model):
    name = models.CharField(
        verbose_name="Имя подраздела", max_length=255)
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        verbose_name="Раздел подраздела",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Подраздел"
        verbose_name_plural = "Подразделы"
class Aauthor(models.Model):
    name = models.CharField(verbose_name="Имя автора", max_length=255)
    reputation = models.IntegerField(validators=[validators.MinValueValidator(0)])
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name="author", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Имя автора"
        verbose_name_plural = "Имена авторов"


class Moderator(models.Model):
    name = models.CharField(verbose_name="Moderator", иmax_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, related_name="moderator", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "Имя модератора"
        verbose_name_plural = "Имена модераторов"
class Post(models.Model):
    author = models.CharField(name="Имя автора", max_length=10)
    body_text = models.TextField('Текст записи')
    subsection = models.ForeignKey(
        Subsection,
        on_delete=models.CASCADE,
        verbose_name="Подраздел",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    number_of_comments = models.IntegerField()
    number_of_like = models.IntegerField()
    number_of_dislike = models.IntegerField()
    rating =models.IntegerField(validators=[validators.MinValueValidator(0)])

    def __str__(self):
        return f'{self.author} - {self.body_text}'
