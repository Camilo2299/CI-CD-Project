import unittest
from flask_testing import TestCase
from app import app, gastos, agregar_gasto_logic

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def setUp(self):
        # Lógica de negocio
        gastos.clear()

    def test_index_route(self):
        response = self.client.get('/')
        self.assert200(response)  # Verifica que la respuesta sea exitosa

    def test_agregar_gasto_route(self):
        data = {'descripcion': 'Comida', 'monto': 20.0}
        self.client.post('/agregar_gasto', data=data)
        #self.assertRedirects(response, 'http://localhost/')

        # Verifica que el gasto se haya agregado correctamente a través de la lógica de negocio
        self.assertEqual(len(gastos), 1)
        self.assertEqual(gastos[0]['descripcion'], 'Comida')
        self.assertEqual(gastos[0]['monto'], 20.0)

    def test_eliminar_gasto_route(self):
        # Agrega un gasto previo para probar la eliminación
        agregar_gasto_logic(gastos, 'Comida', 20.0)

        data = {'gasto_index': 0}
        self.client.post('/eliminar_gasto', data=data)
        #self.assertRedirects(response, '/')

        # Verifica que el gasto se haya eliminado correctamente a través de la lógica de negocio
        self.assertEqual(len(gastos), 0)

if __name__ == '__main__':
    unittest.main()
