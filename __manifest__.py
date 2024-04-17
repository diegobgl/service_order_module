{
    "name": "Service Order Module",
    "version": "1.0",
    "depends": ["base", "purchase", "stock"],
    "author": "Diego Gajardo",
    "website": "www.dgdev.cl",
    "category": "Custom",
    "summary": "Create service orders from purchase orders",
    "data": [
        "security/ir.model.access.csv",
        "views/service_order_views.xml",
        "reports/service_order_report.xml"
    ],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False
}