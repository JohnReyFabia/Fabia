from django.db import models

class BaseModel (models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
class Position(BaseModel):
    description = models.CharField (max_length=100)
# Create your models here.
