import unittest
from flask_testing import TestCase
from application import application, gastos, agregar_gasto_logic

class TestApp(TestCase):

    def create_app(self):
        application.config['TESTING'] = True
        return application

    def setUp(self):
        gastos.clear()

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)  

    def test_agregar_gasto_route(self):
        data = {'descripcion': 'Comida', 'monto': 20.0}
        self.client.post('/agregar_gasto', data=data)

        self.assertEqual(len(gastos), 1)
        self.assertEqual(gastos[0]['descripcion'], 'Comida')
        self.assertEqual(gastos[0]['monto'], 20.0)

    def test_eliminar_gasto_route(self):
        agregar_gasto_logic(gastos, 'Comida', 20.0)

        data = {'gasto_index': 0}
        self.client.post('/eliminar_gasto', data=data)

        self.assertEqual(len(gastos), 0)

if __name__ == '__main__':
    unittest.main()
