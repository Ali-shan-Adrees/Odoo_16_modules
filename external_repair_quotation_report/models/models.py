# -*- coding: utf-8 -*-

from odoo import models, fields, api


class external_repair_quotation_report(models.AbstractModel):
	_name = 'external_repair_quotation_report'
	_description = 'Report'

	@api.model
	def _get_report_values(self, docids, data=None):
		record = self.env['repair.order'].browse(docids)

		return {
			'doc_ids': docids,
			'doc_model': 'repair.order',
			'docs': record,
			'data': data,
			}