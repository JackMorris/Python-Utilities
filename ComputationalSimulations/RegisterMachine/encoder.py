import re

class Encoder:
    """ Class to encode descriptions of Register Machine programs as numbers. """

    def __init__(self):
        """ Class only contains static methods """
        pass

    @staticmethod
    def encode_pair(pair, fat=True):
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

    @staticmethod
    def encode_list(value_list):
        """ Takes in a list of any length of natural numbers. Returns a numerical representation of that list.
        This is calculated using encode_pair above.
            encode_list([]) = 0
            encode_list(x::l) = <<x, encode_list(l)>>
        where [] is the empty list, x::l is the list constructed by appending x to the front of a list l.
        encode_list is a bijection between lists of natural numbers and natural numbers.
        """
        if len(value_list) == 0:
            return 0
        head = value_list[0]
        if (not isinstance(head, int)) or head < 0:
            raise ValueError("Input list must only contains natural numbers")
        encoded_tail = Encoder.encode_list(value_list[1:])
        return Encoder.encode_pair((head, encoded_tail))

    @staticmethod
    def encode_program_instructions(program_instructions):
        """ Takes in a list of program instructions (each a string). Returns a numerical representation of the program.
        Each instruction must be in one of the three forms:
            Ri+ -> Lj           Add one to register i, jump to instruction j
            Ri- -> Lj, Lk       If register i > 0, decrement, jump to instruction j. Otherwise jump to instruction k
            HALT                Stop computation
        Note: whitespace and letter case is not important in the representations.
        Instructions are labelled in order in the list, from L(0) increasing.
        """
        coded_instructions = []
        for instruction_string in program_instructions:
            coded_instruction = Encoder._encode_instruction_string(instruction_string)
            coded_instructions.append(coded_instruction)
        return Encoder.encode_list(coded_instructions)

    @staticmethod
    def _encode_instruction_string(instruction_string):
        """ Returns the numerical representation of instruction string. Instruction string must be in the format
        described above.
        """
        if not isinstance(instruction_string, str):
            raise ValueError("Instruction string must be a string to encode.")
        instruction_string = instruction_string.lower().replace(" ", "")    # Lower case and remove all whitespace
        if instruction_string == "halt":
            return 0

        # Use regular expression to pull out instruction contents
        match = re.match(r"^r(\d+)\+->l(\d+)$", instruction_string)  # Match for r(i)+->l(j)
        if match is not None:
            register_index = int(match.group(1))
            next_instruction = int(match.group(2))
            return Encoder.encode_pair((2*register_index, next_instruction))
        match = re.match(r"^r(\d+)-->l(\d+),l(\d+)$", instruction_string)  # Match for r(i)-->l(j),l(k)
        if match is not None:
            register_index = int(match.group(1))
            positive_instruction = int(match.group(2))
            zero_instruction = int(match.group(3))
            encoded_next_instructions = Encoder.encode_pair((positive_instruction, zero_instruction), fat=False)
            return Encoder.encode_pair((2*register_index + 1, encoded_next_instructions))
        # No match, instruction string in incorrect format
        raise ValueError("Incorrect format for instruction string.")