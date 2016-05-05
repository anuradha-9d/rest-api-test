# -*- coding: utf-8 -*-
import requests
import unittest
import ConfigParser

class test(unittest.TestCase):

    def setUp(self):
        """
        setUp method will load the config settings and test data inputs.
        """
        self.c = ConfigParser.SafeConfigParser()
        self.c.read('config.ini')

        self.inputs = ConfigParser.SafeConfigParser()
        self.inputs.read('test_inputs.dat')

    def test_gist_count(self):
        """
        Check count of available gists
        :return:
        """
        r = requests.get(url = self.c.get('main', 'github_gist_url'))
        self.assertEqual(2, len(r.json()))
        self.assertEqual(200, r.status_code)

    def test_gist_descriptions(self):
        """
        Check gist description match the expected values from the test data file
        :return:
        """
        r = requests.get(url = self.c.get('main', 'github_gist_url'))
        expected_descriptions_list = eval(self.inputs.get('main', 'gist_descriptions'))
        actual_descriptions_list = [str(gist['description']) for gist in r.json()]
        self.assertItemsEqual(expected_descriptions_list, actual_descriptions_list)
        self.assertEqual(200, r.status_code)

    def test_gist_invalid_resource_response(self):
        """
        Check http status 404 when resource is invalid
        :return:
        """
        fake_gist_id = self.inputs.get('main', 'fake_gist_id')
        url = self.c.get('main', 'github_gist_id_url').format(fake_gist_id)
        r = requests.get(url = url)
        self.assertEqual(r.status_code, 404)

    def tearDown(self):
        del self.c
        del self.inputs