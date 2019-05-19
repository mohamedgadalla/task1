from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'List'

    def _str_(self):
        #return self.List_text
        return self.item + ' | ' + str(self.complted)

