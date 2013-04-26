# This file is part product_purchase_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = [
    'ProductConfiguration',
    'ProductConfigurationCompany',
]
__metaclass__ = PoolMeta


class ProductConfiguration:
    'Product Configuration'
    __name__ = 'product.configuration'
    purchasable_sequence = fields.Function(fields.Many2One('ir.sequence', 'Purchasable Sequence',
        domain=[
            ('code', '=', 'product.product'),
        ], required=True),'get_fields', setter='set_fields')


class ProductConfigurationCompany:
    'Product Configuration Company'
    __name__ = 'product.configuration.company'
    purchasable_sequence = fields.Many2One('ir.sequence', 'Purchasable sequence', 
        domain=[
            ('code', '=', 'product.product'),
        ], required=True)
