// Copyright (c) 2022, Pradyot Raina and contributors
// For license information, please see license.txt

frappe.ui.form.on('Project', {
	refresh: function(frm) {
		frm.add_custom_button('Create Project Task', () => {
			frappe.new_doc('Project Task', {
				project_id: frm.doc.name
			})
		})
	}
});


