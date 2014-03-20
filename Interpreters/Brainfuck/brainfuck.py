import re

class Brainfuck:
    """ Class to interpret a Brainfuck program (http://en.wikipedia.org/wiki/Brainfuck) """

    @staticmethod
    def interpret(program):
        """ Interprets the Brainfuck instructions in the supplied program.
        program    -- string of instructions to interpret. Each item must be in {'>', '<', '+', '-', '.', ',', '[', ']'}
                        as described on http://en.wikipedia.org/wiki/Brainfuck, and all other symbols (including
                        whitespace and newlines) are ignored.
        """
        program = re.sub(r'[^><+-.,[\]]', '', program)
        data = [0]*30000
        data_pointer = 0
        instruction_pointer = 0
        instruction_count = len(program)

        while instruction_pointer < instruction_count:
            instruction = program[instruction_pointer]
            if instruction == '>':
                data_pointer += 1
                if data_pointer == len(data):
                    data += [0]*len(data)
                instruction_pointer += 1
            elif instruction == '<':
                if data_pointer > 0:
                    data_pointer -= 1
                instruction_pointer += 1
            elif instruction == '+':
                data[data_pointer] = (data[data_pointer] + 1) % 255
                instruction_pointer += 1
            elif instruction == '-':
                data[data_pointer] = (data[data_pointer] - 1) % 255
                instruction_pointer += 1
            elif instruction == '.':
                print(chr(data[data_pointer]))
                instruction_pointer += 1
            elif instruction == ',':
                data[data_pointer] = ord(input())
                instruction_pointer += 1
            elif instruction == '[':
                if data[data_pointer] == 0:
                    matching_instruction_pointer = Brainfuck.find_matching_right_bracket(program, instruction_pointer)
                    if matching_instruction_pointer == -1:
                        break
                    else:
                        instruction_pointer = matching_instruction_pointer + 1
                else:
                    instruction_pointer += 1
            elif instruction == ']':
                if data[data_pointer] == 0:
                    instruction_pointer += 1
                else:
                    matching_instruction_pointer = Brainfuck.find_matching_left_bracket(program, instruction_pointer)
                    if matching_instruction_pointer == -1:
                        break
                    else:
                        instruction_pointer = matching_instruction_pointer + 1
            else:
                break

    @staticmethod
    def find_matching_right_bracket(program, instruction_pointer):
        """ Given a program and an instruction_pointer over a [ instruction, returns the instruction pointer of the
        matching ] instruction. Returns -1 if no such instruction is in the program.
        """
        to_match = 0
        while instruction_pointer < len(program) - 1:
            instruction_pointer += 1
            if program[instruction_pointer] == '[':
                to_match += 1
            elif program[instruction_pointer] == ']':
                if to_match == 0:
                    return instruction_pointer
                else:
                    to_match -= 1
        return -1

    @staticmethod
    def find_matching_left_bracket(program, instruction_pointer):
        """ Given a program and an instruction_pointer over a ] instruction, returns the instruction pointer of the
        matching [ instruction. Returns -1 if no such instruction is in the program.
        """
        to_match = 0
        while instruction_pointer > 0:
            instruction_pointer -= 1
            if program[instruction_pointer] == ']':
                to_match += 1
            elif program[instruction_pointer] == '[':
                if to_match == 0:
                    return instruction_pointer
                else:
                    to_match -= 1
        return -1