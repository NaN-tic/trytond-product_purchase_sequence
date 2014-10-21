# This file is part product_purchase_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Configuration']
__metaclass__ = PoolMeta


class Configuration:
    __name__ = 'product.configuration'
    purchasable_sequence = fields.Property(fields.Many2One('ir.sequence',
        'Purchasable Sequence', domain=[
            ('code', '=', 'product.product'),
        ], required=True))
