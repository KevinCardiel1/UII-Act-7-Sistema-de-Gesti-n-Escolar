from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    num_matricula = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=100)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    dni = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Curso(models.Model):
    nombre_curso = models.CharField(max_length=100)
    descripcion = models.TextField()
    creditos = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100)
    aula = models.CharField(max_length=50)
    nivel_educativo = models.CharField(max_length=50)
    costo_curso = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre_curso


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField()
    estado_inscripcion = models.CharField(max_length=50)
    nota_final = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    fecha_modificacion = models.DateTimeField()

    def __str__(self):
        return f"Inscripción {self.id} - {self.estudiante}"


class Asistencia(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_clase = models.DateField()
    presente = models.BooleanField()
    justificacion = models.TextField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Asistencia {self.id} - {self.estudiante}"


class Materia(models.Model):
    nombre_materia = models.CharField(max_length=100)
    descripcion = models.TextField()
    nivel_academico = models.CharField(max_length=50)
    es_obligatoria = models.BooleanField()
    horas_semanales = models.IntegerField()

    def __str__(self):
        return self.nombre_materia


class Calificacion(models.Model):
    inscripcion = models.ForeignKey(Inscripcion, on_delete=models.CASCADE)
    tipo_evaluacion = models.CharField(max_length=50)
    fecha_evaluacion = models.DateField()
    puntaje = models.DecimalField(max_digits=5, decimal_places=2)
    ponderacion = models.DecimalField(max_digits=3, decimal_places=2)
    comentarios = models.TextField()

    def __str__(self):
        return f"Calificación {self.id} - {self.inscripcion}"
