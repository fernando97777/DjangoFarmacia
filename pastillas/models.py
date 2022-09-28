from django.db import models


class medicine(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre del medicamento",
        unique=True
    )
    description = models.CharField(
        max_length=250,
        verbose_name="Descripcion del medicamento"
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Precio"
    )
    stock = models.PositiveIntegerField(
        verbose_name="Cantidad"
    )

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        unique_together = [["name", "description","price","stock"]]

    def __str__(self):
        _list = [
            str(self.name),
            str(self.description),
        ]
        return " - ".join(list(_list))