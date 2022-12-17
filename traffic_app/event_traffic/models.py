from django.db import models


# Create your models here.


class Event(models.Model):
    EVENTS_TYPE = [
        (1, "Хакатон"),
        (2, "Лекция"),
        (3, "Семинар"),
        (4, "Митап"),
    ]
    name = models.CharField(verbose_name="Название мероприятия",
                            null=False,
                            blank=False,
                            max_length=500,)
    type = models.IntegerField(choices=EVENTS_TYPE,
                               verbose_name="Тип мероприятия",
                               default=2,
                               null=False,
                               blank=False,)
    description = models.TextField(verbose_name="Описание",
                                   blank=True,
                                   null=True,)
    link = models.CharField(verbose_name="Ссылка регистрации",
                            blank=True,
                            null=True,
                            max_length=500,)

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятии"

    def __str__(self):
        return self.name

