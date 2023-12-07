from .color import colorize_dict
from .main import dictionary
from .util import cleanup
from .hanzi import split_hanzi, remove_empty


def _get_bolded(hanzi):
    return ''

def get_rths(hanzi):
    '''Return RTH for a sentence'''
    chars = list(hanzi)

    rths = []
    for c in chars:
        rth = dictionary.get_rth(hanzi)
        if rth:
            rths += rth
    return ' | '.join(rths)


