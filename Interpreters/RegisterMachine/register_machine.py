import re
import time


class RegisterMachine:
    """ Class to simulate the operation of the RM computing model. """

    @staticmethod
    def _increment_instruction_arguments(instruction):
        """ If instruction is an increment, return its numerical arguments. Otherwise, return None. """
        # We don't care about case or whitespace
        instruction = instruction.lower().replace(" ", "")
        increment_match = re.match(r"^r(\d+)\+->l(\d+)$", instruction)
        if increment_match is None:
            return None
        else:
            return [int(arg) for arg in increment_match.groups()]

    @staticmethod
    def _decrement_instruction_arguments(instruction):
        """ If instruction is a decrement, return its numerical arguments. Otherwise, return None. """
        # We don't care about case or whitespace
        instruction = instruction.lower().replace(" ", "")
        decrement_match = re.match(r"^r(\d+)-->l(\d+),l(\d+)$", instruction)
        if decrement_match is None:
            return None
        else:
            return [int(arg) for arg in decrement_match.groups()]

    @staticmethod
    def _instruction_is_halt(instruction):
        """ Return true if this is a halt instruction """
        return instruction.lower().replace(" ", "") == "halt"

    @staticmethod
    def _ensure_sufficient_registers(configuration, register_index):
        """ Increase the number of registers in configuration (default val 0) if required """
        top_register_index = len(configuration) - 2
        if top_register_index < register_index:
            for i in range(top_register_index, register_index):
                configuration.append(0)

    @staticmethod
    def _handle_increment(configuration, register_index, jump_index):
        """ Increment register at register_index and jump to instruction in jump_index, reflecting both as a change to
        configuration.
        """
        RegisterMachine._ensure_sufficient_registers(configuration, register_index)
        configuration[register_index+1] += 1
        configuration[0] = jump_index

    @staticmethod
    def _handle_decrement(configuration, register_index, jump_index_g0, jump_index_0):
        """ If register at register_index greater than zero, decrement and jump to jump_index_g0. Else jump to
        jump_index_0 Reflect changes as changes to configuration.
        """
        RegisterMachine._ensure_sufficient_registers(configuration, register_index)
        if configuration[register_index+1] > 0:
            configuration[register_index+1] -= 1
            configuration[0] = jump_index_g0
        else:
            configuration[0] = jump_index_0

    @staticmethod
    def _print_configuration(configuration):
        """ Print configuration to console """
        print("PC: " + str(configuration[0]) + "\t" + str(configuration[1:]))

    @staticmethod
    def compute(instructions, registers, print_steps=True, delay=0.5):
        """ Simulates a Register Machine instance.
        instructions    -- list of instructions for the machine. In form:
                            - Rn+ -> Lj         Increment register n, jump to instruction j.
                            - Rn- -> Lj, Lk     If register n>0, decrement and jump to instruction j. Else jump to k.
                            - HALT              Halt operation.
                           Instructions are implicitly labeled by their list index (0 indexed).
        registers       -- Initial contents of registers. Register number specified by list index (0 indexed), must all
                           be natural numbers (integers >= 0).
        print_steps     -- If print_steps is true, configuration at each step will be printed (see below).
        delay           -- Delay between each operation.

        Returns the contents of the registers following the computation. If the machine doesn't halt, this process will
        continue indefinitely.
        Attempting to jump to a non-existing instruction will cause the machine to halt.
        At each step, the 'configuration' is modified. This is of form [PC, R0, R1, R2...].
        """
        if len(instructions) == 0:
            return registers

        configuration = [0] + registers
        while True:
            time.sleep(delay)
            if print_steps:
                RegisterMachine._print_configuration(configuration)

            if configuration[0] > len(instructions):
                # Halt by out of range instruction
                break

            instruction = instructions[configuration[0]]  # Get PC from configuration
            arguments = RegisterMachine._increment_instruction_arguments(instruction)
            if arguments is not None:
                RegisterMachine._handle_increment(configuration, arguments[0], arguments[1])
                continue
            arguments = RegisterMachine._decrement_instruction_arguments(instruction)
            if arguments is not None:
                RegisterMachine._handle_decrement(configuration, arguments[0], arguments[1], arguments[2])
                continue
            if RegisterMachine._instruction_is_halt(instruction):
                # Halt
                break
            # If we get here, instruction is not of valid type
            raise ValueError("Instruction " + instruction + " has invalid format.")

        return configuration[1:]