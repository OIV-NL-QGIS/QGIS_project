"""predifened constant for Kaartblad and Grid"""
DEFAULTSCALE = 25000

PROJECTCRS = 'EPSG:28992'

SINGLEGRIDSIZE = 1000

PAPERSIZES = ['A4', 'A3', 'A2', 'A1', 'A0']

"""Standarised sizes based on A3 format and 40cm x 28cm map print size"""
PAPERTOPOLYGONRD = {
    'A4': {
        'landscape': {
            'x_width': 7000,
            'y_width': 5000
        },
        'portrait': {
            'x_width': 5000,
            'y_width': 7000
        }
    },
    'A3': {
        'landscape': {
            'x_width': 10000,
            'y_width': 7000
        },
        'portrait': {
            'x_width': 7000,
            'y_width': 10000
        }
    },
    'A2': {
        'landscape': {
            'x_width': 14000,
            'y_width': 10000
        },
        'portrait': {
            'x_width': 10000,
            'y_width': 14000
        }
    },
    'A1': {
        'landscape': {
            'x_width': 20000,
            'y_width': 14000
        },
        'portrait': {
            'x_width': 14000,
            'y_width': 20000
        }
    },
    'A0': {
        'landscape': {
            'x_width': 28000,
            'y_width': 20000
        },
        'portrait': {
            'x_width': 20000,
            'y_width': 28000
        }
    }
}