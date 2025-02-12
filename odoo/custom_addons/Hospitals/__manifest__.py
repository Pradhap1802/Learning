{
    "name" : "Hospital Management System" ,
    "author" : "Pradhap" ,
    "license" : "LGPL-3" ,
    "version" : "18.0.1.0" ,
    "depends": ["mail","product"],
    "data": [
        "views/patient_views.xml",
        "views/patient_readonly_views.xml",
        "views/appointment_views.xml",
        "views/appointment_lines_views.xml",
        "data/sequence.xml",
        "views/patient_tag_views.xml",
        "views/menu.xml",
        "security/ir.model.access.csv",
    ]
}