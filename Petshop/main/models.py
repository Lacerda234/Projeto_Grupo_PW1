from django.db import models


SEXO_CHOICES=[
    ('M', 'Masculino'),
    ('F', 'Feminino')
]

TIPO_CHOICES=[
    ('G', 'Gato'),
    ('C', 'Cachorro')
]


ATENDIMENTO_CHOICES=[
    ('M', 'Medico'),
    ('BT', 'Banho e Tosa')
]

class Funcionario(models.Model):
    nome = models.CharField(max_length=30)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    idade = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    cargo = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Funcionários"

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Clientes"


class Animal(models.Model):
    nome = models.CharField(max_length=50)
    tutor  = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    raca = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Animais"


class Atendimento(models.Model):
    tipo = models.CharField(max_length=2, choices=ATENDIMENTO_CHOICES)
    data = models.DateTimeField()
    Descricao = models.CharField(max_length=200)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    responsavel  = models.ForeignKey(Funcionario, on_delete=models.CASCADE)


    def __str__(self):
        return self.Descricao

    class Meta:
        verbose_name_plural = "Atendimentos"



