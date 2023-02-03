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
    for i in range(0, len(GRADIENT_COLORS), skip+1):
        yield GRADIENT_COLORS[i]