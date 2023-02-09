SOLID_COLORS = [
    'red',
    'green',
    'blue',
    'cyan',
]

GRADIENT_COLORS = [
    '#22e8d4',
    '#25adc4',
    '#267fa9',
    '#246093',
    '#22467e',
    '#1e2c63',
    '#17163f',
    '#361a5e',
    '#591b76',
    '#7f1a89',
    '#9b188b',
    '#ae1478',
    '#c60c51',
    '#e50000'
]

def generate_gradient_colors(skip=0):
    n = len(GRADIENT_COLORS)
    i, step = 0, skip+1
    while i<n:
        yield GRADIENT_COLORS[i]
        i += step
        i = i if i<n else 0


def generate_solid_colors(skip=0):
    n = len(SOLID_COLORS)
    i, step = 0, skip+1
    while i<n:
        yield SOLID_COLORS[i]
        i += step
        i = i if i<n else 0