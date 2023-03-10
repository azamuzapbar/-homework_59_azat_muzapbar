from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='название', null=False, blank=False)
    description = models.TextField(max_length=2000, verbose_name='полное_описание')
    task = models.ForeignKey('webapp.Task', related_name='Projects', on_delete=models.PROTECT, verbose_name='задача')
    created_at = models.DateField(verbose_name='время_создания', auto_now_add=True)
    updated_at = models.DateField(verbose_name='время_обновления', auto_now=True)

    def __str__(self):
        return self.title