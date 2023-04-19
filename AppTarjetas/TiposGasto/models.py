from django.db import models
from uuid import uuid4

# Create your models here.
class TipoGasto(models.Model):
    TipoGastoID = models.UUIDField(primary_key=True, default=uuid4, editable=False, auto_created=True)
    Descripcion = models.CharField(max_length=100)