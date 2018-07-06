from ckeditor.fields import RichTextField
from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=255)
    description = RichTextField(config_name='description_ckeditor', blank=True)
    solve = RichTextField(config_name='solve_ckeditor')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ('created_on',)