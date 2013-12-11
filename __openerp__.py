# -*- coding: utf-8 -*-



######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################

{
    "name" : "Payment Release",
    "version" : "0.1",
    "author" : "Novak Conversions",
    "summary": "Various Customizations",
    'description':
        """
        """,
    'maintainer': 'Ursa Information Systems',
    'website': 'http://www.ursainfosystems.com',
    "category" : "User Experience",
    "images" : [],
    "depends" : ["base","sale","account"],
    "data" : [
		"account_invoice.xml",
		"stock_picking.xml"
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
