frappe.ui.form.on('Smart Purchase', {
	// refresh: function(frm) {

	// }
});

/*
frappe.ui.form.on("Smart Purchase", {
  item_group: function(frm){
        cur_frm.clear_table("items");
        cur_frm.refresh_fields();

	if(frm.doc.item_group){
    frappe.call({
    "method": "smart_purchase.smart_purchase.doctype.smart_purchase.smart_purchase.insert_data",
args: {
        item_group: frm.doc.item_group
},
callback:function(r){
        var len=r.message.length;
        console.log(r.message)
        for (var i=0;i<len;i++){
                var row = frm.add_child("items");
                row.item_code = r.message[i][0];
                row.qty = r.message[i][1];
                row.uom = r.message[i][2];
                row.rate = r.message[i][3];
                row.amount = r.message[i][4];
        }
		cur_frm.refresh();
        }
    });
}
}
});


frappe.ui.form.on("Smart Purchase", {
  brand: function(frm){
        cur_frm.clear_table("items");
        cur_frm.refresh_fields();

	if(frm.doc.brand){
    frappe.call({
    "method": "smart_purchase.smart_purchase.doctype.smart_purchase.smart_purchase.insert_data_brand",
args: {
        item_group: frm.doc.item_group,
        brand: frm.doc.brand
},
callback:function(r){
        var len=r.message.length;
        console.log(r.message)
        for (var i=0;i<len;i++){
                var row = frm.add_child("items");
                row.item_code = r.message[i][0];
                row.qty = r.message[i][1];
                row.uom = r.message[i][2];
                row.rate = r.message[i][3];
                row.amount = r.message[i][4];
        }
                cur_frm.refresh();
        }
    });
}
}
});

frappe.ui.form.on("Smart Purchase", {
  item_code: function(frm){
        cur_frm.clear_table("items");
        cur_frm.refresh_fields();

	if(frm.doc.item_code){
    frappe.call({
    "method": "smart_purchase.smart_purchase.doctype.smart_purchase.smart_purchase.insert_data_item",
args: {
        item_group: frm.doc.item_group,
        brand: frm.doc.brand,
        item_code: frm.doc.item_code
},
callback:function(r){
        var len=r.message.length;
        console.log(r.message)
        for (var i=0;i<len;i++){
                var row = frm.add_child("items");
                row.item_code = r.message[i][0];
                row.qty = r.message[i][1];
                row.uom = r.message[i][2];
                row.rate = r.message[i][3];
                row.amount = r.message[i][4];
        }
                cur_frm.refresh();
        }
    });
}
}
});

frappe.ui.form.on("Smart Purchase", {
  get_open_purchase_request: function(frm) {
        cur_frm.clear_table("smart_purchase_mr");
        cur_frm.refresh_fields();

	if(frm.doc.item_group){
    frappe.call({
    "method": "smart_purchase.smart_purchase.doctype.smart_purchase.smart_purchase.insert_mr",
args: {
	item_group: frm.doc.item_group
},
callback:function(r){
        var len=r.message.length;
        for (var i=0;i<len;i++){
                var row = frm.add_child("smart_purchase_mr");
                row.mr = r.message[i][0];
		row.mri = r.message[i][1];
        }
		cur_frm.refresh();
        }
    });
}
}
});
*/
