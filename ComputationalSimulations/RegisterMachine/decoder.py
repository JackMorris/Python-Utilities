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

    @staticmethod
    def decode_program_instructions(numeric_representation):
        """ Inverse operation of Encoder.encode_program_instructions(). (Documentation in encoder.py) """
        coded_instructions = Decoder.decode_list(numeric_representation)
        return [Decoder._decode_instruction_code(coded_instruction) for coded_instruction in coded_instructions]

    @staticmethod
    def _decode_instruction_code(numeric_representation):
        """ Inverse operation of Encoder.encode_instruction_string(). (Documentation in decoder.py) """
        if not isinstance(numeric_representation, int) or numeric_representation < 0:
            raise ValueError("Numeric representation must be a natural number")
        if numeric_representation == 0:
            return "HALT"
        x, y = Decoder.decode_pair(numeric_representation)
        if x % 2 == 0:
            # x even, Instruction is Rx/2+ -> Ly
            return "R" + str(x/2) + "+ -> L" + str(y)
        else:
            # x odd. y = <j, k>. Instruction is R(x-1)/2- -> Lj, Lk
            j, k = Decoder.decode_pair(y, fat=False)
            return "R" + str((x-1)/2) + "- -> L" + str(j) + ", L" + str(k)