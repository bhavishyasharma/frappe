import frappe


@frappe.whitelist()
def get_print_settings_to_show(doctype, docname):
	doc = frappe.get_doc(doctype, docname)
	print_settings = frappe.get_single("Print Settings")

	fields = []

	if hasattr(doc, 'get_print_settings'):
	if hasattr(doc, "get_print_settings"):
		fields = doc.get_print_settings() or []
	elif doc.doctype != "Sales Invoice":
		return []

	print_settings_fields = []

	if doc.doctype == "Sales Invoice":
		df = {
			'fieldname': 'print_copy',
			'label': 'Print Copy',
			'fieldtype': 'Select',
			'options': ['', 'Original for Recipient', 'Duplicate for Supplier', 'Duplicate for Transport', 'Triplicate for Supplier'],
			'default': ''
		}
		print_settings_fields.append(df)
	elif doc.doctype == "Quotation":
		df = {
			'fieldname': 'print_copy',
			'label': 'Print Copy',
			'fieldtype': 'Select',
			'options': ['Quotation', 'PRO FORMA INVOICE'],
			'default': ''
		}
		print_settings_fields.append(df)
	

	for fieldname in fields:
		df = print_settings.meta.get_field(fieldname)
		if not df:
			continue
		df.default = print_settings.get(fieldname)
		print_settings_fields.append(df)

	return print_settings_fields
