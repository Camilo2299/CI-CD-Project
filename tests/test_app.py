import unittest
from application import agregar_gasto_logic, eliminar_gasto_logic, obtener_lista_de_gastos

class AppFunctionsTestCase(unittest.TestCase):

    def test_agregar_gasto(self):
        gastos = []
        agregar_gasto_logic(gastos, 'Comida', 20.0)
        self.assertEqual(len(gastos), 1)
        self.assertEqual(gastos[0]['descripcion'], 'Comida')
        self.assertEqual(gastos[0]['monto'], 20.0)

    def test_eliminar_gasto(self):
        gastos = [{'descripcion': 'Comida', 'monto': 20.0}, {'descripcion': 'Transporte', 'monto': 10.0}]
        eliminar_gasto_logic(gastos, 1)
        self.assertEqual(len(gastos), 1)
        self.assertEqual(gastos[0]['descripcion'], 'Comida')
        self.assertEqual(gastos[0]['monto'], 20.0)

if __name__ == '__main__':
    unittest.main()
