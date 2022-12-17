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
                            max_length=500, )
    type = models.IntegerField(choices=EVENTS_TYPE,
                               verbose_name="Тип мероприятия",
                               default=2,
                               null=False,
                               blank=False, )
    description = models.TextField(verbose_name="Описание",
                                   blank=True,
                                   null=True, )
    link = models.CharField(verbose_name="Ссылка регистрации",
                            blank=True,
                            null=True,
                            max_length=500, )

    class Meta:
        verbose_name = "Мероприятия"
        verbose_name_plural = "Мероприятии"

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(verbose_name="Имя студента",
                            null=False,
                            blank=False,
                            max_length=100, )
    email = models.EmailField(verbose_name="Email",
                              null=False,
                              blank=False)

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    def __str__(self):
        return self.name


class Feedback(models.Model):
    student = models.ForeignKey(Student,
                                verbose_name="Студент",
                                on_delete=models.CASCADE,
                                null=False, )
    event = models.ForeignKey(Event,
                              verbose_name="Мероприятие",
                              on_delete=models.CASCADE,
                              null=False, )
    feedback = models.IntegerField(verbose_name="Оценка",
                                   null=False,
                                   blank=False, )
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.student} - {self.event} - {self.feedback}"


class Register(models.Model):
    student = models.ForeignKey(Student,
                                verbose_name="Студент",
                                on_delete=models.CASCADE,
                                null=False, )
    event = models.ForeignKey(Event,
                              verbose_name="Мероприятие",
                              on_delete=models.CASCADE,
                              null=False, )
    event_check = models.BooleanField(default=False,
                                      verbose_name="Посетил?")
    link = models.CharField(max_length=500,
                            verbose_name="Уникальная ссылка для отзыва",
                            null=True,
                            blank=True, )

    class Meta:
        verbose_name = "Регистрация на мероприятие"
        verbose_name_plural = "Регистрации на мероприятия"

    def __str__(self):
        return f"{self.student} - {self.event}"

