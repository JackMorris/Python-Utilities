class Encoder:
    """ Class to encode descriptions of Register Machine programs as numbers. """

    def __init__(self):
        """ Class only contains static methods """
        pass

    @staticmethod
    def encode_pair_fat(pair, fat='True'):
        """ Takes in a sequence of a pair of numbers (x,y). Returns a numerical representation of that pair.
        This can be done in two ways:
            'Fat' encoding:      <<x,y>> = 2^x(2y+1)
            'Standard' encoding:  <x,y>  = 2^x(2y+1) - 1
        Fat encoding is specified by passing the 'fat' argument as 'True' (true by default).

        The difference is that standard encoding can encode to any natural number, but 'fat' only encodes to >0.
        Both encodings form a bijection between N*N and N (but not to 0 for fat encoding).
        This distinction is important later, as we represent empty lists by 0, so don't want to map some pairs to 0.
        """
        if not len(pair) == 2:
            raise ValueError("Passed in pair must contain two values, x and y.")
        x, y = pair
        if (not isinstance(x, int)) or x < 0 or (not isinstance(y, int)) or y < 0:
            raise ValueError("Values in list must be natural numbers (integers > 0")

        encoding = (2**x) * (2*y + 1)
        if not fat:
            encoding -= 1
        return encoding
