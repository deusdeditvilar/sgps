from django.db import models

class Funcionario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=80)
    tipo_pessoa = models.TextField()  # This field type is a guess.
    nome_da_mae = models.CharField(max_length=80, blank=True, null=True)
    nome_do_pai = models.CharField(max_length=80, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=11)
    situacao_moradia = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateTimeField()
    escola = models.CharField(max_length=30, blank=True, null=True)
    ano_escolar = models.CharField(max_length=15, blank=True, null=True)
    turno_escolar = models.TextField(blank=True, null=True)  # This field type is a guess.
    escolaridade = models.CharField(max_length=30, blank=True, null=True)
    bolsa_familia = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'funcionario'


class Pessoa(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=80)
    tipo_pessoa = models.TextField()  # This field type is a guess.
    nome_da_mae = models.CharField(max_length=80, blank=True, null=True)
    nome_do_pai = models.CharField(max_length=80, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(unique=True, max_length=11)
    situacao_moradia = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateTimeField()
    escola = models.CharField(max_length=30, blank=True, null=True)
    ano_escolar = models.CharField(max_length=15, blank=True, null=True)
    turno_escolar = models.TextField(blank=True, null=True)  # This field type is a guess.
    escolaridade = models.CharField(max_length=30, blank=True, null=True)
    bolsa_familia = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pessoa'