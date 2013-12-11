# -*- coding: utf-8 -*-


######################################################################
#
#  Note: Program metadata is available in /__init__.py
#
######################################################################

from openerp.osv import fields, osv

class account_invoice(osv.osv):
	_inherit = "account.invoice"
	_columns = {
		"bs_releasable": fields.boolean('Releasable', readonly=False, 
		help="Can this order be delivered.  If not checked, then this customer is either over their credit limit or must pay for the order before it can be delivered."),
		"bs_cc_check": fields.boolean('Release', readonly=False,help="Can this order be delivered.  If not checked, credit card information hasn't been verified")
		}

class account_voucher(osv.osv):
	_inherit = "account.voucher"
	
	def button_proforma_voucher(self, cr, uid, ids, context=None):
	
		paidAmt = self.pool.get('account.voucher').read(cr,uid,ids,['amount'],context=None)[0]['amount']
		total = self.pool.get('account.invoice').read(cr,uid,context['active_id'],['amount_total'],context=None)['amount_total']
		self.pool.get('account.invoice').write(cr,uid,context['active_id'],{'comment' : 'got here! '+str(total)+'-'+str(paidAmt)},context=None)
		if ( total - paidAmt ) <= 0 and total < 1000:
			self.pool.get('account.invoice').write(cr,uid,context['active_id'],{'bs_releasable' : True},context=None)
		return super(account_voucher, self).button_proforma_voucher(cr, uid, ids, context=context)