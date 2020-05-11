from odoo import models, fields, api

class account_payment(models.Model):
    _inherit = "account.payment"
    task_ids = fields.Many2many('bts.schedule.seat', string="Task", required=True)
    schedule_id = fields.Many2one('bts.schedule', string="Schedule",readonly=True)

    @api.model
    def default_get(self, fields):
        result = super(account_payment, self).default_get(fields)
        # seat_id = self.env['bts.schedule.seat'].browse(self.env.context.get('active_ids', False))
        seat_id = self.env['bts.schedule.seat'].id
        result.update({
            'task_ids': seat_id.ids,
            'schedule_id':seat_id[0].project_id.id,
        })
        return result

    def action_validate_invoice_payment(self):
        res = super(account_payment,self).action_validate_invoice_payment()

        for line in self:
            invoice = self.env['account.invoice'].search([('id','=',self.invoice_ids.id)])
            print(invoice)
            print(invoice.state)
            invoice_line = self.env['account.invoice.line'].search([('id','=',self.invoice_ids.invoice_line_ids.id)])
            print(invoice_line.bus_state)
            print(invoice.bus_state)
            print(invoice.project_id)
            print(self.task_ids)
            if invoice.state == 'paid':
            #     seat = self.env['bts.schedule.seat'].search([('id','=',self.id)])
            #     print(seat.bus_state)
                for seat in self.task_ids:
                    seat.bus_state ='paid'

        return res