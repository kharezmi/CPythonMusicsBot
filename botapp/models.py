from django.db import models
from django.utils import timezone

STATUS_CHOICES = [
    ('s', 'Send Message'),
]


class Users(models.Model):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = verbose_name + "lar"
    u_id = models.TextField(max_length=15,)
    name = models.TextField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Musics(models.Model):
    music = models.Manager()
    class Meta:
        verbose_name = "Musiqa"
        verbose_name_plural = verbose_name + "lar"
    from_user = models.CharField(max_length=255)
    music_name = models.CharField(max_length=255)
    music_id = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.music_name} {self.music_id}"


class UnfulfilledManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            date__lt=timezone.now(),
            done=False,
        )


class TaskManager(models.Model):
    class Type(models.TextChoices):
        SEND_MESSAGE = 'Send Message All Users'
        SEND_PHOTO = 'Send Photo All Users'

    SEP = '|'

    task = models.Manager()
    unfulfilled = UnfulfilledManager()
    txt = models.CharField(max_length=30, choices=Type.choices)
    info = models.TextField(null=True, blank=True)
    photo = models.ImageField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def args_join(cls, *args):
        return cls.SEP.join(map(str, args))

    @property
    def argv(self):
        return self.info.split(TaskManager.SEP)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        if self.info:
            return f'{self.id}. {self.txt}({self.info})'

        return f'{self.id}. {self.txt}'