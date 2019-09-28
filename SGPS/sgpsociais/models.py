from django.db import models
from django.contrib.auth.models import User

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
    turno_escolar = models.TextField(blank=True, null=True)
    escolaridade = models.CharField(max_length=30, blank=True, null=True)
    bolsa_familia = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'funcionario'


class Jovem(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=80)
    data_nascimento = models.DateTimeField()
    sexo = models.CharField(max_length=2)
    nome_da_mae = models.CharField(max_length=80, blank=True, null=True)
    nome_do_pai = models.CharField(max_length=80, blank=True, null=True)
    naturalidade = models.CharField(max_length=20)
    cep = models.CharField(max_length=11,null=False)
    cidade = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)
    situacao_escolar = models.CharField(max_length=30)
    escola = models.CharField(max_length=30, blank=True, null=True)
    ano_escolar = models.IntegerField(blank=True, null=True)
    turno_escolar = models.IntegerField(blank=True, null=True)
    telefone = models.IntegerField(max_length=12, null=True)
    parentesco = models.CharField(max_length=20, null=True)
    diabetes = models.BooleanField(null=False)
    uso_med = models.BooleanField()
    desc_uso_med = models.CharField(max_length=30)
    dep_quim = models.BooleanField()
    desc_dep_quim = models.CharField(max_length=30)
    pressao_alta = models.BooleanField()
    sofre_doenca = models.BooleanField()
    alergia_med = models.BooleanField()
    med_controlado = models.BooleanField()
    desc_med_controlado = models.CharField(max_length=30)
    prioritario = models.BooleanField()
    obs = models.TextField(max_length=200)

    class Meta:
        managed = False
        db_table = 'pessoa'
    
    def __str__(self):
        return self.nome

class Crianca(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=80)
    data_nascimento = models.DateTimeField()
    sexo = models.CharField(max_length=2)
    nome_da_mae = models.CharField(max_length=80, blank=True, null=True)
    nome_do_pai = models.CharField(max_length=80, blank=True, null=True)
    naturalidade = models.CharField(max_length=20)
    cep = models.CharField(max_length=11,null=False)
    cidade = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    endereco = models.CharField(max_length=100)
    situacao_escolar = models.CharField(max_length=30)
    escola = models.CharField(max_length=30, blank=True, null=True)
    ano_escolar = models.IntegerField(blank=True, null=True)
    turno_escolar = models.IntegerField(blank=True, null=True)
    telefone = models.IntegerField(max_length=12, null=True)
    parentesco = models.CharField(max_length=20, null=True)
    diabetes = models.BooleanField(null=False)
    uso_med = models.BooleanField()
    desc_uso_med = models.CharField(max_length=30)
    dep_quim = models.BooleanField()
    desc_dep_quim = models.CharField(max_length=30)
    pressao_alta = models.BooleanField()
    sofre_doenca = models.BooleanField()
    alergia_med = models.BooleanField()
    med_controlado = models.BooleanField()
    desc_med_controlado = models.CharField(max_length=30)
    prioritario = models.BooleanField()
    obs = models.TextField(max_length=200)

    class Meta:
        managed = False
        db_table = 'crianca'
    
    def __str__(self):
        return self.nome

class Usuario(User):
   # id = models.IntegerField(primary_key=True)
    #pessoa = models.ForeignKey(Pessoa, models.DO_NOTHING, blank=True, null=True)
    funcionario = models.ForeignKey(Funcionario, models.DO_NOTHING, blank=True, null=True)
   # nome_usuario = models.CharField(max_length=20)
   # senha = models.CharField(max_length=20)
    cpf = models.CharField(unique=True, max_length=11)
    nivel_permissao = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

