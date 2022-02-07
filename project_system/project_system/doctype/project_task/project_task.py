# Copyright (c) 2022, Pradyot Raina and contributors
# For license information, please see license.txt

import frappe
import datetime
from frappe.model.document import Document

class ProjectTask(Document):
	
	def before_save(self):
		self.task_id = self.name
		'''project = frappe.get_doc("Project", self.project_id)
		if self.task_start_date:
			tsd = datetime.datetime.strptime(self.task_start_date, '%Y-%m-%d').date()
			if tsd < project.start_date:
				frappe.throw("Task start date is before Project Start Date")
		if self.task_end_date:
			ted = datetime.datetime.strptime(self.task_end_date, '%Y-%m-%d').date()
			if ted > project.expected_end_date:
				frappe.throw("Task end date after project end date")
		
	'''	
