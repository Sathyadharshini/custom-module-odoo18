{
    "name": "Leave Request System",
    "version": "1.0",
    "summary": "Custom Leave Request and Approval Workflow",
    "author": "Sathya Dharshini",
    "category": "Human Resources",
    "depends": ["base", "hr", "mail"],
"data": [
    "security/leave_groups.xml",
    "security/ir.model.access.csv",
    "views/leave_request_views.xml",
    "views/leave_request_actions.xml",
    "views/leave_request_menus.xml"
],

    "application": True,
    "installable": True
}
