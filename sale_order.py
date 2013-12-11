# -*- coding: utf-8 -*-


######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################

from openerp.osv import fields, osv
import pdb

class sale_order(osv.osv):
    _inherit = "sale.order"

    _columns = {
		"bs_releasable": fields.boolean('Releasable', readonly=False, 
		help="Can this order be delivered.  If not checked, then this customer is either over their credit limit or must pay for the order before it can be delivered."),
    }
	
#	def action_invoice_create(self, cr, uid, ids, grouped=False, states=None, date_invoice = False, context=None)
#		result = super(sale_order,self).action_invoice_create(cr,uid,ids,grouped=False,states=None,date_invoice=False,context=None)
#		
#		total = float( self.pool.get('sale.order').read(cr,uid,ids,['amount_total'],context['active_id'])[0]['amount_total'] )
#		if total > 1000.0 :
#			self.pool.get('sale.order').write(cr,uid,context['active_id'],{'bs_releaseable' : False})
#		return result
	
	
    def onchange_partner_id(self, cr, uid, ids, part, context=None):
        result = super(sale_order, self).onchange_partner_id(cr, uid, ids, part, context=context)
	
        if not part:
            return result
        partner = self.pool.get('res.partner').browse(cr, uid, part, context=context)	
        if partner.parent_id and not partner.is_company:
            partner = partner.parent_id
        if partner.property_payment_term and partner.property_payment_term.id:
            result['value']['bs_releasable'] = True
        else:
            result['value']['bs_releasable'] = False
        return result

    def onchange_payment_term(self, cr, uid, ids, term, context=None):
        result = {'value': {'bs_releasable': False,}}

        if not term:
            return result

        payment_term = self.pool.get('account.payment.term').browse(cr, uid, term, context=context)
        if payment_term:
            result['value']['bs_releasable'] = True

        return result

