from django.db import models

class Dentrix(models.Model):
    Month = models.CharField(
        max_length=20,
        null=False,
        blank=False
        )
    Production = models.DecimalField(
        decimal_places=2,
        default=0
        )
    Hygienist_Production = models.DecimalField(
        decimal_places=2,
        default=0
        )
    Collections_Percentage = models.DecimalField(
        decimal_places=2,
        default=0
        )
    Overthe_Counter = models.SmallIntegerField(
        default=0
        )
    AR_31_60 = models.DecimalField(
        decimal_places=2,
        default=0
    )
    AR_61_90 = models.DecimalField(
        decimal_places=2,
        default=0
    )
    AR_Over_90 = models.DecimalField(
        decimal_places=2,
        default=0
    )
    AR_Ins_31_60 = models.DecimalField(
        decimal_places=2,
        default=0
    )
    AR_Ins_61_90 = models.DecimalField(
        decimal_places=2,
        default=0
    )
    AR_Ins_Over_90 = models.DecimalField(
        decimal_places=2,
        default=0
    )
    New_Patients = models.SmallIntegerField(
        default=0
        )
    Total_Patients_Seen =models.SmallIntegerField(
        default=0
    )
    Broken_Apointments = models.SmallIntegerField(
        default=0
    )
    Broken_Appt_Pct = models.DecimalField(
        default = 0
    )
    Hygiene_Pct = models.DecimalField(
        default=0
    )
