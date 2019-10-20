from django.db import models
from django.utils import timezone


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class SoftDeleteMixin(models.Model):
    deleted_at = models.DateTimeField(default=None, null=True)
    actives = ActiveManager()
    objects = models.Manager()

    @property
    def deleted(self):
        return self.deleted_at is not None

    class Meta:
        abstract = True
