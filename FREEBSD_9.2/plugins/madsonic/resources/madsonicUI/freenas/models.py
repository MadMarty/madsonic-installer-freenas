import platform

from django.db import models


class Madsonic(models.Model):
    """
    Django model describing every tunable setting for madsonic
    """

    enable = models.BooleanField(default=False)
    madsonic_max_memory = models.IntegerField(
        verbose_name="Max Memory (MB)",
        default=150,
        )
    madsonic_ssl = models.BooleanField(
        verbose_name="Enable SSL",
        default=False,
        )
    madsonic_port = models.IntegerField(
        verbose_name="WebUI Port",
        default=4040,
        )
    madsonic_context_path = models.CharField(
        verbose_name="Context Path",
        max_length=120,
        default="/",
        )
