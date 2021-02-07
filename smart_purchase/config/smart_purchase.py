from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Tool"),
			"items": [
				{
					"type": "doctype",
					"name": "Smart Purchase",
					"label": "Smart Purchase",
					"description": _("Smart Purchase"),
					"onboard": 1
				}
			]
		}
]

