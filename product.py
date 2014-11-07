# This file is part product_purchase_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Product']
__metaclass__ = PoolMeta


class Product:
    'Product Product'
    __name__ = 'product.product'

    @classmethod
    def __setup__(cls):
        super(Product, cls).__setup__()
        cls._error_messages.update({
                'purchasable_sequence': 'Configure purchasable sequence'
                    ' in Product Configuration',
                })

    @classmethod
    def get_purchase_sequence(cls):
        Sequence = Pool().get('ir.sequence')
        Configuration = Pool().get('product.configuration')

        config = Configuration(1)
        if not config.purchasable_sequence:
            cls.raise_user_error('purchasable_sequence')
        code = Sequence.get_id(config.purchasable_sequence.id)
        return code

    @classmethod
    def create(cls, vlist):
        Template = Pool().get('product.template')

        vlist = [x.copy() for x in vlist]
        for values in vlist:
            tpl = Template.read([values.get('template')], [
                'salable', 'purchasable'])[0]
            if not values.get('code') and tpl.get('purchasable') \
                and not tpl.get('salable'):
                    values['code'] = cls.get_purchase_sequence()
        return super(Product, cls).create(vlist)

    @classmethod
    def write(cls, *args):
        super(Product, cls).write(*args)
        actions = iter(args)
        for products, values in zip(actions, actions):
            for product in products:
                if (product.template.purchasable
                        and not product.template.salable
                        and not product.code):
                    if not values.get('code'):
                        cls.write([product], {
                            'code': cls.get_purchase_sequence()
                            })
