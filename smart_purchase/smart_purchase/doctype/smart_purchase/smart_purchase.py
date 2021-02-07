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
				item_li = {"item_code": i.item_code,"qty": i.qty,"rate": i.rate,"amount":i.amount,"stock_uom":i.uom,"schedule_date":date.today()}
				items.append(item_li)
			purchase_order = frappe.get_doc({
			"doctype": "Purchase Order",
			"supplier": self.supplier,
			"transaction_date": date.today(),
			"schedule_date": date.today(),
			"set_warehouse": self.for_warehouse,
			"items": items,
			"smart_purchase_mr": self.smart_purchase_mr
			})
			purchase_order.insert(ignore_permissions=True)
			purchase_order.save()
			msgprint("Purchase Order Created")

		if self.order_for == "Selected Items From Table":
			selected_items = []
			for i in self.items:
				if i.use_this == 1:
					item_li = {"item_code": i.item_code,"qty": i.qty,"rate": i.rate,"amount":i.amount,"stock_uom":i.uom,"schedule_date":date.today()}
					selected_items.append(item_li)

			purchase_order = frappe.get_doc({
			"doctype": "Purchase Order",
			"supplier": self.supplier,
			"transaction_date": date.today(),
			"schedule_date": date.today(),
			"set_warehouse": self.for_warehouse,
			"items": selected_items,
			"smart_purchase_mr": self.selected_item_mr
			})
			purchase_order.insert(ignore_permissions=True)
			purchase_order.save()
			msgprint("Purchase Order Created")


@frappe.whitelist(allow_guest=True)
def insert_data(item_group):
        mt = frappe.db.sql("""select mri.item_code, sum(mri.qty - mri.ordered_qty), mri.stock_uom, sum(mri.rate), sum(mri.amount),
				mri.item_name,mri.description,mri.item_group,mri.brand
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.per_ordered < 100 and mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and mri.item_group = %s
				group by mri.item_code;""",(item_group),as_list=1)
       	return mt

@frappe.whitelist(allow_guest=True)
def insert_data_with_brand(item_group,brand):
	mt = frappe.db.sql("""select mri.item_code, sum(mri.qty - mri.ordered_qty), mri.stock_uom, sum(mri.rate), sum(mri.amount),
				mri.item_name,mri.description,mri.item_group,mri.brand 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.per_ordered < 100 and mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and 
				mri.item_group = %s and mri.brand = %s
                                group by mri.item_code;""",(item_group,brand),as_list=1)
	return mt


@frappe.whitelist(allow_guest=True)
def insert_data_with_item(item_group,brand,item_code):
	mt = frappe.db.sql("""select mri.item_code, sum(mri.qty - mri.ordered_qty), mri.stock_uom, sum(mri.rate), sum(mri.amount),
				mri.item_name,mri.description,mri.item_group,mri.brand 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.per_ordered < 100 and mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 
				and mri.item_group = %s and mri.brand = %s
                                and mri.item_code = %s group by mri.item_code;""",(item_group,brand,item_code),as_list=1)
	return mt


@frappe.whitelist(allow_guest=True)
def insert_data_brand(brand):
        mt = frappe.db.sql("""select mri.item_code, sum(mri.qty - mri.ordered_qty), mri.stock_uom, sum(mri.rate), sum(mri.amount),
				mri.item_name,mri.description,mri.item_group,mri.brand 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.per_ordered < 100 and mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and mri.brand = %s
                                group by mri.item_code;""",(brand),as_list=1)
        return mt


@frappe.whitelist(allow_guest=True)
def insert_data_brand_item(brand,item_code):
        mt = frappe.db.sql("""select mri.item_code, sum(mri.qty - mri.ordered_qty), mri.stock_uom, sum(mri.rate), sum(mri.amount),
				mri.item_name,mri.description,mri.item_group,mri.brand 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.per_ordered < 100 and mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 
				and mri.brand = %s and mri.item_code = %s
                                group by mri.item_code;""",(brand,item_code),as_list=1)
        return mt

@frappe.whitelist(allow_guest=True)
def insert_data_item(item_code):
        mt = frappe.db.sql("""select mri.item_code, sum(mri.qty - mri.ordered_qty), mri.stock_uom, sum(mri.rate), sum(mri.amount),
				mri.item_name,mri.description,mri.item_group,mri.brand 
                                from `tabMaterial Request` mr, `tabMaterial Request Item` mri where (mri.ordered_qty != mri.qty) and
                                mr.per_ordered < 100 and mr.docstatus = 1 and mri.parent = mr.name and mri.unused = 0 and mri.item_code = %s
                                group by mri.item_code;""",(item_code),as_list=1)
        return mt


@frappe.whitelist(allow_guest=True)
def insert_mr(item_group):
        mt = frappe.db.sql("""select DISTINCT mri.parent,mri.name from `tabMaterial Request Item` mri, `tabMaterial Request` mr where 
                                mr.per_ordered < 100 and
                                mri.parent = mr.name and mri.unused = 0 and mr.docstatus = 1 and mri.item_group = %s;""",(item_group),as_list=1)
        return mt

@frappe.whitelist(allow_guest=True)
def insert_mr_with_brand(item_group,brand):
        mt = frappe.db.sql("""select DISTINCT mri.parent,mri.name from `tabMaterial Request Item` mri, `tabMaterial Request` mr where 
                                mr.per_ordered < 100 and
                                mri.parent = mr.name and mr.docstatus = 1 and mri.unused = 0 and mri.item_group = %s
				and mri.brand = %s;""",(item_group,brand),as_list=1)
        return mt

@frappe.whitelist(allow_guest=True)
def insert_mr_with_item(item_group,brand,item_code):
        mt = frappe.db.sql("""select DISTINCT mri.parent,mri.name from `tabMaterial Request Item` mri, `tabMaterial Request` mr where 
                                mr.per_ordered < 100 and
                                mri.parent = mr.name and mr.docstatus = 1 and mri.unused = 0 and mri.item_group = %s and
				mri.brand = %s and mri.item_code = %s;""",(item_group,brand,item_code),as_list=1)
        return mt


@frappe.whitelist(allow_guest=True)
def insert_mr_brand(brand):
        mt = frappe.db.sql("""select DISTINCT mri.parent,mri.name from `tabMaterial Request Item` mri, `tabMaterial Request` mr where 
                                mr.per_ordered < 100 and
                                mri.parent = mr.name and mri.unused = 0 and mr.docstatus = 1
                                and mri.brand = %s;""",(brand),as_list=1)
        return mt

@frappe.whitelist(allow_guest=True)
def insert_mr_brand_item(brand,item_code):
        mt = frappe.db.sql("""select DISTINCT mri.parent,mri.name from `tabMaterial Request Item` mri, `tabMaterial Request` mr where 
                                mr.per_ordered < 100 and
                                mri.parent = mr.name and mri.unused = 0 and mr.docstatus = 1 
                                and mri.brand = %s and mri.item_code = %s;""",(brand,item_code),as_list=1)
        return mt

@frappe.whitelist(allow_guest=True)
def insert_mr_item(item_code):
        mt = frappe.db.sql("""select DISTINCT mri.parent,mri.name from `tabMaterial Request Item` mri, `tabMaterial Request` mr where 
                                mr.per_ordered < 100 and
                                mri.parent = mr.name and mri.unused = 0 and mr.docstatus = 1
                                and mri.item_code = %s;""",(item_code),as_list=1)
        return mt

@frappe.whitelist(allow_guest=True)
def transferStock(doc,method):
	for i in doc.items:
		stock = frappe.db.sql("""select actual_qty from `tabBin` where item_code = %s and warehouse = %s""",(i.item_code,doc.stock_warehouse))
		if stock[0][0] != 0:
			items = []
			if stock[0][0] >= i.qty:
				item_li = {"item_code": i.item_code,"qty": i.qty,"uom":i.uom,"s_warehouse":doc.stock_warehouse,"t_warehouse":doc.set_warehouse,"basic_rate":i.rate}
				items.append(item_li)

			if stock[0][0] < i.qty:
				item_li = {"item_code": i.item_code,"qty": stock[0][0],"uom":i.uom,"s_warehouse":doc.stock_warehouse,"t_warehouse":doc.set_warehouse,"basic_rate":i.rate}
				items.append(item_li)
			mt = frappe.get_doc({
			"doctype": "Stock Entry",
			"company": doc.company,
			"stock_entry_type": "Material Transfer",
			"posting_date": doc.transaction_date,
			"from_warehouse": doc.stock_warehouse,
			"to_warehouse": doc.set_warehouse,
			"sales_order" : doc.name,
			"items": items
			})
			mt.insert(ignore_permissions=True)
			mt.save(ignore_permissions=True)
			mt.submit()


def closeMR(doc,method):
	if doc.smart_purchase_mr:
		for d in doc.smart_purchase_mr:
			mri = frappe.get_doc("Material Request Item",d.mri)
			mri.purchase_order = doc.name
			mri.save()

			mr = frappe.get_doc("Material Request",d.mr)
			mr.per_ordered = 100
			mr.status = "Ordered"
			mr.save()

def revertMR(doc,method):
	if doc.smart_purchase_mr:
		for d in doc.smart_purchase_mr:
			mri = frappe.get_doc("Material Request Item",d.mri)
			mri.purchase_order = ""
			mri.save()

			mr = frappe.get_doc("Material Request",d.mr)
			mr.per_ordered = 0
			mr.status = "Pending"
			mr.save()
