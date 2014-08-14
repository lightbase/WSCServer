#!/usr/env python
# -*- coding: utf-8 -*
import unittest
import requests
import json
#import hashlib
#from pyramid_restler.view import RESTfulView
#from collections import defaultdict

class TestConect(unittest.TestCase):
    """
        Testando WSCserver 
    """
    def setUp(self):
        self.rest_url = 'http://10.1.0.121/wscserver'
        pass


    def test_carrega_classe(self):
        """
        Testa carregar instanciar classe do REST
        """
        url = self.rest_url + '/rest/coleta'
        r = requests.get(url)
        coleta = r.json()
        coleta_str = r.text
        fd = open('/tmp/coleta.json', 'w+')
        fd.write(coleta_str)
        fd.close()

        assert(coleta)

    def test_carrega_resultados(self):
        """
        Carrega resultados em uma variavel
        """
        url = self.rest_url + '/rest/coleta'
        r = requests.get(url)
        coleta = r.json()
        results = coleta.get('results')

        assert(results)


    def test_carrega_computador(self):
        """
        Carrega resultados para um computador
        """
        url = self.rest_url + '/rest/coleta'
        r = requests.get(url)
        coleta = r.json()
        results = coleta.get('results')
        computador = results[0]

        assert(computador)


    def test_carrega_elemento(self):
        """
        Carrega um elemento de um computador
        """
        url = self.rest_url + '/rest/coleta'
        r = requests.get(url)
        coleta = r.json()
        results = coleta.get('results')
        computador = results[0]
        software = computador.get('SoftwareList')

        assert(software)

    def test_url_rest(self):
        """
        Testa URL do rest
        """
        url = self.rest_url +'/rest/coleta'
        get_url = requests.get(url)
        assert(get_url)

    def test_url_zip(self):
        """
        Testa URL do zip
        """
        url = self.rest_url +'/zip/coleta'
        get_url = requests.get(url)
        assert(get_url)

    def tearDown(self):
       pass

