import os
import unittest

from main import *

def getDirectory(rel_dir):
    script_dir = os.path.dirname(__file__)
    complete_dir = script_dir + rel_dir
    return complete_dir

agendar_1 = getDirectory("/audio/agendar_1.wav")
cortes_1 = getDirectory("/audio/cortes_1.wav")
disponibilidade_1 = getDirectory("/audio/disponibilidade_1.wav")
errado_1 = getDirectory("/audio/errado_1.wav")
errado_2 = getDirectory("/audio/errado_2.wav")
fila_1 = getDirectory("/audio/fila_1.wav")
horario_1 = getDirectory("/audio/horario_1.wav")
pagamento_1 = getDirectory("/audio/pagamento_1.wav")
produtos_1 = getDirectory("/audio/produtos_1.wav")
saudacao_1 = getDirectory("/audio/saudacao_1.wav")
        
class TesteNome(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_sem_nome(self):
        phrase = hear_audio(errado_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "")

    def testar_nome_errado(self):
        phrase = hear_audio(errado_2)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "")


class TesteAgendamento(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_atendimento(self):
        phrase = hear_audio(agendar_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "Para agendar, basta dizer por exemplo: 'Barber, agendar com josias'. Para saber quais são os nomes dos nossos barbeiros, diga: 'barber, lista de barbeiros'.")

        
class TesteCortes(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_cortes(self):
        phrase = hear_audio(cortes_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "Fazemos todos os tipos de cortes de cabelo. Dá uma olhada no nosso instagram e você poderá ter um catálogo completo de nossos serviços.")
        
class TesteDisponibilidade(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_disponibilidade(self):
        phrase = hear_audio(disponibilidade_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "sim! temos cortes disponiveis para hoje. Pedro atende das 7h às 19h, Carlos atende das 14h às 17h e josias das 16h às 20h.")

        
class TesteFila(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_fila(self):
        phrase = hear_audio(fila_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "Para saber quantos clientes faltam para determinado barbeiro, como por exemplo josias, diga: 'barber, josias fila'. Para saber quais são os nomes dos nossos barbeiros, diga: 'barber, barbeiros lista'")
        
class TesteHorario(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_horario(self):
        phrase = hear_audio(horario_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "Atendemos de segunda à sexta das 7h à 20h. Pedro atende das 7h às 19h, Carlos atende das 14h às 17h e josias das 16h às 20h.")
        
class TestePagamento(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_pagamento(self):
        phrase = hear_audio(pagamento_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "Aceitamos débito, crédito, dinheiro e pix.")
        
class TesteProduto(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_produtos(self):
        phrase = hear_audio(produtos_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "Temos um freezer com refigerantes e água. Basta escolher um e pegar, o valor será debitado ao pagamento do corte.")

class TesteSaudacao(unittest.TestCase):

    def setUp(self):
        get_data_settings()

    def testar_saudacao(self):
        phrase = hear_audio(saudacao_1)
        print(f"comando reconhecido: {phrase}")

        action, target = get_tokenized_command(phrase)
        is_valid,response = run_command(action, target)

        self.assertTrue(response == "Oi, sou a Barber. Deseja fazer algum atendimento? Basta dizer o meu nome e em seguida o comando.")


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteNome))
    testes.addTest(carregador.loadTestsFromTestCase(TesteAgendamento))
    testes.addTest(carregador.loadTestsFromTestCase(TesteCortes))
    testes.addTest(carregador.loadTestsFromTestCase(TesteDisponibilidade))
    testes.addTest(carregador.loadTestsFromTestCase(TesteFila))
    testes.addTest(carregador.loadTestsFromTestCase(TesteHorario))
    testes.addTest(carregador.loadTestsFromTestCase(TestePagamento))
    testes.addTest(carregador.loadTestsFromTestCase(TesteProduto))
    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacao))

    executor = unittest.TextTestRunner()
    executor.run(testes)