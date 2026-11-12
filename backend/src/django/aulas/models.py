from django.db import models

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False, blank=False)

    class Meta:
        db_table = 'carrera'

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False, blank=False)
    apellido = models.CharField(max_length=128, null=False, blank=False)
    mostrar = models.CharField(max_length=256, null=False, blank=False)

    class Meta:
        db_table = 'profesor'

    def __str__(self):
        return self.mostrar


class Materia(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128, null=False, blank=False)
    cant_alumnos = models.IntegerField(null=False, default=5)
    id_carrera = models.ForeignKey(
        Carrera,
        on_delete=models.CASCADE,
        db_column='id_carrera'
    )
    
    id_profesor = models.ForeignKey(
        Profesor,
        on_delete=models.CASCADE,
        db_column='id_profesor'
    )

    class Meta:
        db_table = 'materia'

    def __str__(self):
        return self.nombre


class Aula(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=128, null=False, blank=False)
    ubicacion = models.CharField(max_length=128, null=False, blank=False)
    cant_proyector = models.IntegerField(default=0)
    aforo = models.IntegerField(default=0)
    es_climatizada = models.BooleanField(default=False)

    class Meta:
        db_table = 'aula'

    def __str__(self):
        return f"{self.descripcion} ({self.ubicacion})"



class ReservaAula(models.Model):
    id = models.AutoField(primary_key=True)
    id_aula = models.ForeignKey(
        Aula,
        on_delete=models.CASCADE,
        db_column='id_aula'
    )
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()
    observacion = models.CharField(max_length=256, blank=True, default='')

    class Meta:
        db_table = 'reserva_aula'

    def __str__(self):
        return f"Reserva {self.id} - Aula {self.id_aula}"


class HorarioMateria(models.Model):
    id = models.AutoField(primary_key=True)
    id_materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        db_column='id_materia'
    )
    id_reserva = models.ForeignKey(
        ReservaAula,
        on_delete=models.CASCADE,
        db_column='id_reserva'
    )
    fh_desde = models.DateTimeField()
    fh_hasta = models.DateTimeField()


    class Meta:
        db_table = 'horario_materia'

    def __str__(self):
        return f"{self.id_materia} ({self.fh_desde} - {self.fh_hasta})"
