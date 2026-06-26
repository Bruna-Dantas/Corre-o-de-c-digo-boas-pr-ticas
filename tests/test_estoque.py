import unittest
from unittest.mock import patch

import estoque


class TestEntradaDeDados(unittest.TestCase):
    def test_ler_numero_inteiro_aceita_valor_valido(self):
        with patch("builtins.input", side_effect=["7"]):
            self.assertEqual(estoque.ler_numero_inteiro("Quantidade: ", minimo=1), 7)

    def test_ler_numero_inteiro_reforca_valor_valido(self):
        with patch("builtins.input", side_effect=["abc", "3"]):
            with patch("builtins.print") as mocked_print:
                self.assertEqual(estoque.ler_numero_inteiro("Quantidade: ", minimo=1), 3)
        self.assertTrue(any("Valor inválido" in str(call.args[0]) for call in mocked_print.call_args_list))

    def test_ler_numero_real_aceita_valor_valido(self):
        with patch("builtins.input", side_effect=["12.5"]):
            self.assertEqual(estoque.ler_numero_real("Preco: ", minimo=0.01), 12.5)


if __name__ == "__main__":
    unittest.main()
