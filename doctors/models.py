from django.db import models


class Doctors(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Nombre",
        unique=True
    )
    cedule = models.CharField(
        max_length=10,
        verbose_name="Cedula",
        unique=True
    )
    phone = models.CharField(
        max_length=10,
        verbose_name="Telefono",
        unique=True
    )
    direction = models.CharField(
        max_length=250,
        verbose_name="Direccion"
    )

    class Meta:
        verbose_name = "Doctor",
        verbose_name_plural = "Doctores",

    def __str__(self):
        _list = [str(self.name),
                 ]
        return " - ".join(list(_list))


class ReportDoctor(models.Model):
    doctor = models.ForeignKey(
        "doctors.Doctors",
        verbose_name="Medico",
        on_delete=models.PROTECT
    )
    medicament = models.ForeignKey(
        "pastillas.medicine",
        verbose_name="Pastillas",
        on_delete=models.PROTECT
    )
    patient_name = models.CharField(
        max_length=250,
        verbose_name="Nombre Paciente"
    )
    patient_Cedule = models.CharField(
        max_length=10,
        verbose_name="Cedula"
    )
    patient_phone = models.CharField(
        max_length=10,
        verbose_name="Telefono"
    )

    class Meta:
        verbose_name = "Reporte",
        verbose_name_plural = "Reportes",

    def __str__(self):
        _list = [str(self.doctor),
                 str(self.medicament),
                 str(self.patient_name),
                 str(self.patient_Cedule),
                 str(self.patient_phone),
                 ]
        return " - ".join(list(_list))

