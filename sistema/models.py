from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)  # CPF como string
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=15)  # Número de telefone como string
    historicodeagendamento = models.TextField(blank=True, null=True)
    designerdeunha = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=15)
    disponibilidadedehorario = models.TextField()
    servicosoferecidos = models.TextField()

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome


class Agendamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrigido o relacionamento com usuário
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('confirmado', 'Confirmado'), ('concluído', 'Concluído')]
    )

    def __str__(self):
        return f"{self.cliente.username} - {self.servico.nome} - {self.data_hora}"


class Pagamento(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)  # Corrigido para se referir a um usuário
    agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)  # Relacionado com agendamento
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[('pendente', 'Pendente'), ('confirmado', 'Confirmado'), ('concluído', 'Concluído')]
    )

    def __str__(self):
        return f"Pagamento de {self.cliente.username} - {self.status}"

    class Meta:
        verbose_name = "Pagamento"
