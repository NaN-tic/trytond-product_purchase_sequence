# This file is part of the product_purchase_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ProductPurchaseSequenceTestCase(ModuleTestCase):
    'Test Product Purchase Sequence module'
    module = 'product_purchase_sequence'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ProductPurchaseSequenceTestCase))
    return suite