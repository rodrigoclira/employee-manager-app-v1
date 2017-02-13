from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from .models import EmployeeList

"""Esta classe irá definir o conjunto de testes para o modelo da classe: 'EmployeeList':"""
class ModelTestCase(TestCase):

    """Essa função aqui será responsável por testar o cliente e as variáveis:"""
    def setUp(self):
        self.employeelist_name = "Write world class code"
        self.employeelist = EmployeeList(name=self.employeelist_name)

    """Essa função irá testar o modelo da classe:"""
    def test_model_can_create_a_employeelist(self):
        old_count = EmployeeList.objects.count()
        self.employeelist.save()
        new_count = EmployeeList.objects.count()
        self.assertNotEqual(old_count, new_count)

""" Aqui irei testar a parte lógica da aplicação: 'views.py':"""
class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.employeelist_data = {'name': 'Glaucia Lemos'}
        self.response = self.client.post(
            reverse('create'),
            self.employeelist_data,
            format="json")

    """ Aqui iremos testar se realmente criará de maneira satisfatória o empregado: METHOD: GET (ALL) """
    def test_api_can_create_a_employeelist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    """ Aqui iremos testar se está retornando todos os valores dados do employee: METHOD: GET (By Id) """
    def test_api_can_get_a_employeelist(self):
        employeelist = EmployeeList.objects.get(id=1)
        response = self.client.get(
            '/employee/',
            kwargs={'pk': employeelist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, employeelist)
    
    """# Aqui iremos testar se estará atualizando os valores para employee: METHOD: PUT"""
    def test_api_can_update_employeelist(self):
        employeelist = EmployeeList.objects.get()
        change_employeelist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': employeelist.id}),
            change_employeelist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    """Aqui iremos testar se estará deletando o valor pelo Id: METHOD: DELETE:"""
    def test_api_can_delete_employeelist(self):
        employeelist = EmployeeList.objects.get()
        response = self.client.delete(
            reserve('details', kwargs={'pk': employeelist.id}),
            format='json',
            follow=True)

    self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
