# -*- coding: utf-8 -*-


######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################

from openerp.osv import fields, osv

class stock_picking(osv.osv):
    _inherit = "stock.picking"			
			
    def _get_releasable(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        inv_obj = self.pool.get('account.invoice')

        if context is None:
            context = {}
        for val in self.browse(cr,uid,ids,context=context):
            if val.sale_id:
                if val.sale_id.bs_releasable or val.sale_id.invoiced: # if the product has been invoiced
                    res[val.id] = "HOLD" # hold
                    for inv in inv_obj.browse(cr, uid, val.sale_id.invoice_ids, context=context): #then search the object to try and find objects with that source document
                        if inv.id: # if the id is valid
                            if inv.id.bs_releasable: # and if this field is checked.
                                res[val.id] = 'RELEASE' # release.
				
            else:
                res[val.id] = ''
                                
        return res
		
    def _get_payment_type(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        if context is None:
            context = {}
        for session in self.browse(cr,uid,ids,context=context):
            if session.sale_id:
                #res[session.id] = session.sale_id.payment_type.name or False
				foo="foo"
        return res
		
    _columns = {
        "bs_releasable": fields.function(_get_releasable, type='char', size = 5,readonly=False,
            method=True, string="Release",store=False,
            help="Can this order be delivered.  If not checked, then this customer is either over their credit limit or must pay for the order before it can be delivered."),
        "bs_payment_type": fields.function(_get_payment_type, type='char',size=50,
            method=True, string="Pay By",
            store=True),			
    }

class stock_picking_out(osv.osv):
    _inherit = "stock.picking.out"

    def _get_releasable(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        inv_obj = self.pool.get('account.invoice')
        
        if context is None:
            context = {}
        for val in self.browse(cr,uid,ids,context=context):
            if val.sale_id:
                if val.sale_id.bs_releasable and val.sale_id.invoiced:
                    res[val.id] = "RELEASE"
                else:
                    res[val.id] = "HOLD"
                    for inv in inv_obj.browse(cr, uid, val.sale_id.invoice_ids, context=context):
                        if inv.id:
                            if inv.id.bs_cc_check:
                                res[val.id] = 'RELEASE'
				
            else:
                res[val.id] = ''
            
        return res

    def _get_payment_type(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        if context is None:
            context = {}
        for session in self.browse(cr,uid,ids,context=context):
            if session.sale_id:
                #res[session.id] = session.sale_id.payment_type.name or False
				foo="foo"
        return res

    _columns = {
        "bs_releasable": fields.function(_get_releasable, type='char', size = 5,readonly=False,
            method=True, string="Release",store=False,
            help="Can this order be delivered.  If not checked, then this customer is either over their credit limit or must pay for the order before it can be delivered."),
#        "bs_payment_type": fields.function(_get_payment_type, type='char',size=50,
#            method=True, string="Pay By",
#            store=True),
    }

