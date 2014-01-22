class Decoder:
    """ Class to decode numbers to Register Machine Descriptions """

    def __init__(self):
        """ Class only contains static methods """
        pass

    @staticmethod
    def decode_pair(numeric_representation, fat=True):
        """ Inverse operation of Encoder.encode_pair(). (Documentation in encoder.py) """
        if not isinstance(numeric_representation, int) or numeric_representation < 0:
            raise ValueError("Numeric representation must be a natural number.")
        if fat and numeric_representation == 0:
            raise ValueError("Fat decoding cannot decode 0.")
        if not fat:
            numeric_representation += 1  # Convert to fat representation

        # Find position of first 1
        first_one_position = 0
        while (numeric_representation >> first_one_position) & 1 == 0:
            first_one_position += 1
        x = first_one_position

        y = numeric_representation >> (first_one_position + 1)
        return x, y

    @staticmethod
    def decode_list(numeric_representation):
        """ Inverse operation of Encoder.encode_list(). (Documentation in encoder.py) """
        if not isinstance(numeric_representation, int) or numeric_representation < 0:
            raise ValueError("Numeric representation must be a natural number")
        if numeric_representation == 0:
            return []
        head, tail_representation = Decoder.decode_pair(numeric_representation)
        return [head] + Decoder.decode_list(tail_representation)