from django.db import models
#
from django.db.models import Count


class ReunionManager(models.Manager):

    #cuenta cantidad de veces que sale el personaje en reuniones
    def cantidad_reuniones_job(self):
        resultado = self.values('persona__job').annotate(
            cantidad = Count('id')
        )
        print("asdasdas")
        print(resultado)
        return resultado