from unittest import TestCase
from brutils.renavam import is_valid_renavam

class TestRENAVAM(TestCase):
    def test_is_valid_renavam(self):
        
        # Testes para entradas inválidas
        self.assertFalse(is_valid_renavam(''))  # String vazia
        self.assertFalse(is_valid_renavam('12345678'))  # Menos de 11 dígitos
        self.assertFalse(is_valid_renavam('123456 8'))  # Menos de 11 dígitos com espaço
        self.assertFalse(is_valid_renavam('123456789012'))  # Mais de 11 dígitos
        self.assertFalse(is_valid_renavam('123456789 012'))  # Mais de 11 dígitos com espaço
        self.assertFalse(is_valid_renavam('1234567890a'))  # Contém letra 
        self.assertFalse(is_valid_renavam('12345678 901'))  # Contém espaço 
        self.assertFalse(is_valid_renavam('abcdefghijk'))  # Apenas letras 
        self.assertFalse(is_valid_renavam('12345678901!'))  # Contém caractere especial

        # Testes para entradas válidas
        self.assertTrue(is_valid_renavam('12345678900'))  # válido
        self.assertFalse(is_valid_renavam('12345678901'))  # inválido
