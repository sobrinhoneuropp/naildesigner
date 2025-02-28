from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    contato = models.CharField(max_length=15)
    historico_agendamento = models.TextField(blank=True, null=True)
    preferencia_designer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=15)
    disponibilidade_horario = models.TextField()
    servicos_oferecidos = models.TextField()

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tempo_estimado = models.DurationField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_horario = models.DateTimeField()

    def __str__(self):
        return f"{self.cliente} - {self.servico} - {self.data_horario}"


class Pagamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    agendamento = models.OneToOneField(Agendamento, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pagamento = models.CharField(max_length=50)
    status_pagamento = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado')
    ])

    def __str__(self):
        return f"{self.cliente} - {self.status_pagamento}"
