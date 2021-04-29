from __future__ import unicode_literals
import frappe
from datetime import date
from datetime import datetime, timedelta
from frappe import msgprint
from frappe.model.document import Document

class SmartPurchase(Document):
	def on_submit(self):
		if self.order_for == "All Items From Table":
			items = []
			for i in self.items:
				item_li = {"item_code": i.item_code,"qty": i.qty,"rate": i.rate,"amount":i.amount,"stock_uom":i.uom,"schedule_date":date.today(),"material_request": i.mr,"material_request_item": i.mri}
				items.append(item_li)
			purchase_order = frappe.get_doc({
			"doctype": "Purchase Order",
			"supplier": self.supplier,
			"transaction_date": date.today(),
			"schedule_date": date.today(),
			"set_warehouse": self.for_warehouse,
			"items": items
			})
			purchase_order.insert(ignore_permissions=True)
			purchase_order.save()
			msgprint("Purchase Order Created")

		if self.order_for == "Selected Items From Table":
			selected_items = []
			for i in self.items:
				if i.use_this == 1:
					item_li = {"item_code": i.item_code,"qty": i.qty,"rate": i.rate,"amount":i.amount,"stock_uom":i.uom,"schedule_date":date.today(),"material_request": i.mr,"material_request_item": i.mri}
					selected_items.append(item_li)

			purchase_order = frappe.get_doc({
			"doctype": "Purchase Order",
			"supplier": self.supplier,
			"transaction_date": date.today(),
			"schedule_date": date.today(),
			"set_warehouse": self.for_warehouse,
			"items": selected_items
			})
			purchase_order.insert(ignore_permissions=True)
			purchase_order.save()
			msgprint("Purchase Order Created")


@frappe.whitelist(allow_guest=True)
def insert_data_only_group(item_group,from_date,to_date):
        mt = frappe.db.sql("""select mri.item_code, (mri.qty - mri.ordered_qty), mri.stock_uom, mri.rate, mri.amount,
				mri.item_name,mri.description,mri.item_group,mri.brand,mri.parent, mri.name 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and mri.item_group = %s 
				and (mr.schedule_date between %s and %s);""",(item_group,from_date,to_date),as_list=1)
       	return mt

@frappe.whitelist(allow_guest=True)
def insert_data_with_brand_group(item_group,brand,from_date,to_date):
	mt = frappe.db.sql("""select mri.item_code, (mri.qty - mri.ordered_qty), mri.stock_uom, mri.rate, mri.amount,
				mri.item_name,mri.description,mri.item_group,mri.brand,mri.parent, mri.name 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and 
				mri.item_group = %s and mri.brand = %s
				and (mr.schedule_date between %s and %s);""",(item_group,brand,from_date,to_date),as_list=1)
	return mt


@frappe.whitelist(allow_guest=True)
def insert_data_all(item_group,brand,item_code,from_date,to_date):
	mt = frappe.db.sql("""select mri.item_code, (mri.qty - mri.ordered_qty), mri.stock_uom, mri.rate, mri.amount,
				mri.item_name,mri.description,mri.item_group,mri.brand,mri.parent, mri.name 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 
				and mri.item_group = %s and mri.brand = %s and mri.item_code = %s
				and (mr.schedule_date between %s and %s);""",(item_group,brand,item_code,from_date,to_date),as_list=1)
	return mt


@frappe.whitelist(allow_guest=True)
def insert_data_only_brand(brand,from_date,to_date):
        mt = frappe.db.sql("""select mri.item_code, (mri.qty - mri.ordered_qty), mri.stock_uom, mri.rate, mri.amount,
				mri.item_name,mri.description,mri.item_group,mri.brand,mri.parent, mri.name 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and mri.brand = %s
                                and (mr.schedule_date between %s and %s);""",(brand,from_date,to_date),as_list=1)
        return mt


@frappe.whitelist(allow_guest=True)
def insert_data_brand_item(brand,item_code,from_date,to_date):
        mt = frappe.db.sql("""select mri.item_code, (mri.qty - mri.ordered_qty), mri.stock_uom, mri.rate, mri.amount,
				mri.item_name,mri.description,mri.item_group,mri.brand,mri.parent, mri.name 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 
				and mri.brand = %s and mri.item_code = %s
                                ;""",(brand,item_code,from_date,to_date),as_list=1)
        return mt

@frappe.whitelist(allow_guest=True)
def insert_data_only_item(item_code,from_date,to_date):
        mt = frappe.db.sql("""select mri.item_code, (mri.qty - mri.ordered_qty), mri.stock_uom, mri.rate, mri.amount,
				mri.item_name,mri.description,mri.item_group,mri.brand, mri.parent, mri.name 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and mri.item_code = %s
                                and (mr.schedule_date between %s and %s);""",(item_code,from_date,to_date),as_list=1)
        return mt
