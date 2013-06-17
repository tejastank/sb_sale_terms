# -*- coding: utf-8 -*-
##############################################################################
#
#    SnippetBucket.com, Open Source Management Solution
#    Copyright (C) 2012-2013 (<http://snippetbucket.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv,fields

class company(osv.osv):
    _inherit = 'res.company'
    _columns = {
        'sale_notes': fields.text('Sales Terms', translate=True),
    }
company()

class sale_order(osv.osv):
    _inherit = 'sale.order'

    def _get_default_note(self, cr, uid, context=None):
        language = self.pool.get('res.users').browse(cr, uid, uid, context=context).lang
        print context, language
        company_id = self.pool.get('res.users').browse(cr, uid, uid, context=context).company_id.sale_notes
        return company_id

    _defaults = {
        'note': _get_default_note,
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
