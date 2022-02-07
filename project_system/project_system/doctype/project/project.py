# Copyright (c) 2022, Pradyot Raina and contributors
# For license information, please see license.txt

import frappe
import datetime
from frappe.model.document import Document

class Project(Document):
	
	def before_save(self):
		self.project_id = self.name
		fystart = frappe.db.get_single_value("Financial Year", "finstartdate")
		fyend   = frappe.db.get_single_value("Financial Year", "finenddate")
		#startdate = datetime.datetime.strptime(self.start_date, '%Y-%m-%d').date()
		if ((frappe.utils.date_diff(self.start_date, fystart)<0) or (frappe.utils.date_diff(self.start_date, fyend)>0)):
			frappe.throw("Start Date doesnt fall within financial year")
		'''if not ((startdate>fystart) and (startdate<fyend)):
			frappe.throw("Start Date doesnt fall within financial year")
		if self.expected_end_date < self.start_date:
			frappe.throw("End Date is before Start Date")'''
	
		
