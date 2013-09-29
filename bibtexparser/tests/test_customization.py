#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from bibtexparser.customization import getnames, convert_to_unicode, homogeneize_latex_encoding, page_double_hyphen


class TestBibtexParserMethod(unittest.TestCase):

    ###########
    # getnames
    ###########
    def test_getnames(self):
        names = ['Foo Bar',
                 'F. Bar',
                 'Jean de Savigny',
                 'Jean la Tour',
                 'Jean le Tour',
                 'Mike ben Akar',
                 #'Jean de la Tour',
                 #'Johannes Diderik van der Waals',
                 ]
        result = getnames(names)
        expected = ['Bar, Foo',
                    'Bar, F',
                    'de Savigny, Jean',
                    'la Tour, Jean',
                    'le Tour, Jean',
                    'ben Akar, Mike',
                    #'de la Tour, Jean',
                    #'van der Waals, Johannes Diderik',
                    ]
        self.assertEqual(result, expected)

    ###########
    # page_double_hyphen
    ###########
    def test_page_double_hyphen_alreadyOK(self):
        record = {'pages': '12--24'}
        result = page_double_hyphen(record)
        expected = record
        self.assertEqual(result, expected)

    def test_page_double_hyphen_simple(self):
        record = {'pages': '12-24'}
        result = page_double_hyphen(record)
        expected = {'pages': '12--24'}
        self.assertEqual(result, expected)

    def test_page_double_hyphen_space(self):
        record = {'pages': '12 - 24'}
        result = page_double_hyphen(record)
        expected = {'pages': '12--24'}
        self.assertEqual(result, expected)

    def test_page_double_hyphen_nothing(self):
        record = {'pages': '12 24'}
        result = page_double_hyphen(record)
        expected = {'pages': '12 24'}
        self.assertEqual(result, expected)

    ###########
    # convert to unicode
    ###########
    def test_convert_to_unicode(self):
        record = {'toto': '{\`a} \`{a}'}
        result = convert_to_unicode(record)
        expected = {'toto': 'à à'}
        self.assertEqual(result, expected)

    ###########
    # homogeneize
    ###########
    def test_homogeneize(self):
        record = {'toto': 'à {\`a} \`{a}'}
        result = homogeneize_latex_encoding(record)
        expected = {'toto': '{\`a} {\`a} {\`a}'}
        self.assertEqual(result, expected)
