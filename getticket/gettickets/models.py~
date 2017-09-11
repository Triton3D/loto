from django.db import models
import django.core.validators as vls

class Ticket(models.Model):
	number=models.IntegerField(primary_key=True,default=0)
	content=models.CharField(max_length=90,validators=[vls.validate_comma_separated_integer_list])
	circ=models.SmallIntegerField(default=1196)
