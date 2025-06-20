import unittest

from brutils.cpf import is_valid

class TestCPFValidation(unittest.TestCase):

    def test_CT1(self):
        cpf = "82178537464"
        self.assertTrue(is_valid(cpf))  # CT1: válido

    def test_CT2(self):
        cpf = "abc45678901"
        self.assertFalse(is_valid(cpf))  # CT2: contém letras

    def test_CT3(self):
        cpf = "1234567890"  # 10 dígitos
        self.assertFalse(is_valid(cpf))  # CT3: tamanho incorreto

    def test_CT4(self):
        cpf = "11111111111"
        self.assertFalse(is_valid(cpf))  # CT4: repetição

    def test_CT5(self):
        cpf = "86216451166"
        self.assertFalse(is_valid(cpf))  # CT5: dígito verificador inválido

    def test_CT6(self):
        cpf = "82178537464"
        self.assertTrue(is_valid(cpf))  # CT6: mesmo do CT1, válido

    def test_CT7(self):
        cpf = "86216451148"
        self.assertFalse(is_valid(cpf))  # CT7: dígito verificador inválido

if __name__ == '__main__':
    unittest.main()
