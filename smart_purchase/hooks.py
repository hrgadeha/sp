# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "smart_purchase"
app_title = "Smart Purchase"
app_publisher = "Hardik Gadesha"
app_description = "App to Create Auto Purchase"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developer"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/smart_purchase/css/smart_purchase.css"
# app_include_js = "/assets/smart_purchase/js/smart_purchase.js"

# include js, css files in header of web template
# web_include_css = "/assets/smart_purchase/css/smart_purchase.css"
# web_include_js = "/assets/smart_purchase/js/smart_purchase.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "smart_purchase.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "smart_purchase.install.before_install"
# after_install = "smart_purchase.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "smart_purchase.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"smart_purchase.tasks.all"
# 	],
# 	"daily": [
# 		"smart_purchase.tasks.daily"
# 	],
# 	"hourly": [
# 		"smart_purchase.tasks.hourly"
# 	],
# 	"weekly": [
# 		"smart_purchase.tasks.weekly"
# 	]
# 	"monthly": [
# 		"smart_purchase.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "smart_purchase.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "smart_purchase.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "smart_purchase.task.get_dashboard_data"
# }
