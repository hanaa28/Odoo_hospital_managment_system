{
    'name': 'hospital system',
    'author': 'hanaa',
    'depends': ['crm'],
    'data': [
        'views/patient.xml',
        'views/hms_doctors.xml',
        'views/hms_departments.xml',
        'views/customer_inherit.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hms/static/src/css/custom_styles.css',
        ],
    },
}

