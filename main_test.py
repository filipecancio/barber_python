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

class TesteAgendamento(unittest.TestCase):

    def setUp(self):
        get_data_settings()
        
class TesteCortes(unittest.TestCase):

    def setUp(self):
        get_data_settings()
        
class TesteDisponibilidade(unittest.TestCase):

    def setUp(self):
        get_data_settings()
        
class TesteNome(unittest.TestCase):

    def setUp(self):
        get_data_settings()
        
class TesteFila(unittest.TestCase):

    def setUp(self):
        get_data_settings()
        
class TesteHorario(unittest.TestCase):

    def setUp(self):
        get_data_settings()
        
class TestePagamento(unittest.TestCase):

    def setUp(self):
        get_data_settings()
        
class TesteProduto(unittest.TestCase):

    def setUp(self):
        get_data_settings()

class TesteSaudacao(unittest.TestCase):

    def setUp(self):
        get_data_settings()


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteAgendamento))
    testes.addTest(carregador.loadTestsFromTestCase(TesteCortes))
    testes.addTest(carregador.loadTestsFromTestCase(TesteDisponibilidade))
    testes.addTest(carregador.loadTestsFromTestCase(TesteErradoNome))
    testes.addTest(carregador.loadTestsFromTestCase(TesteErradoSemNome))
    testes.addTest(carregador.loadTestsFromTestCase(TesteFila))
    testes.addTest(carregador.loadTestsFromTestCase(TesteHorario))
    testes.addTest(carregador.loadTestsFromTestCase(TestePagamento))
    testes.addTest(carregador.loadTestsFromTestCase(TesteProduto))
    testes.addTest(carregador.loadTestsFromTestCase(TesteSaudacao))

    executor = unittest.TextTestRunner()
    executor.run(testes)