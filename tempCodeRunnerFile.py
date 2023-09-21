class CPU:
    def __init__(self):
        self.registers = [0] * 8  # 8 general-purpose registers
        self.memory = [0] * 1024  # Main memory with 1024 words
        self.pc = 0  # Program counter
        self.cycles = 0  # Total clock cycles
        self.register_mapping = {'r0': 0, 'r1': 1, 'r2': 2,
                                 'r3': 3, 'r4': 4, 'r5': 5, 'r6': 6, 'r7': 7}
        self.encoded_instructions = []  # List to store encoded instructions

    def execute(self, program):
        self.pc = 0
        while self.pc < len(program):
            instruction = program[self.pc]
            opcode = instruction[0]

            if opcode == "mov":
                dest_reg = self.register_mapping[instruction[1]]
                src_reg_or_value = instruction[2]
                if isinstance(src_reg_or_value, int):
                    self.registers[dest_reg] = src_reg_or_value
                else:
                    src_reg = self.register_mapping[src_reg_or_value]
                    self.registers[dest_reg] = self.registers[src_reg]

                # Encoding for "mov" instruction
                encoded_instruction = "0000{:03}{:03}".format(
                    self.register_mapping[src_reg_or_value], dest_reg)
                self.encoded_instructions.append(encoded_instruction)

            elif opcode == "add":
                dest_reg = self.register_mapping[instruction[1]]
                src_reg1 = self.register_mapping[instruction[2]]
                src_reg_or_value = instruction[3]
                if isinstance(src_reg_or_value, int):
                    src_reg2 = 0  # Use r0 as a placeholder for immediate values
                    src_val2 = src_reg_or_value
                else:
                    src_reg2 = self.register_mapping[src_reg_or_value]
                    src_val2 = 0  # Placeholder for the source register value

                self.registers[dest_reg] = self.registers[src_reg1] + \
                    src_val2

                # Encoding for "add" instruction
                encoded_instruction = "0001{:03}{:03}{:03}".format(
                    src_reg1, src_reg2, dest_reg)
                self.encoded_instructions.append(encoded_instruction)

            elif opcode == "sub":
                dest_reg = self.register_mapping[instruction[1]]
                src_reg1 = self.register_mapping[instruction[2]]
                src_reg_or_value = instruction[3]
                if isinstance(src_reg_or_value, int):
                    src_reg2 = 0  # Use r0 as a placeholder for immediate values
                    src_val2 = src_reg_or_value
                else:
                    src_reg2 = self.register_mapping[src_reg_or_value]
                    src_val2 = 0  # Placeholder for the source register value

                self.registers[dest_reg] = self.registers[src_reg1] - \
                    src_val2

                # Encoding for "sub" instruction
                encoded_instruction = "0010{:03}{:03}{:03}".format(
                    src_reg1, src_reg2, dest_reg)
                self.encoded_instructions.append(encoded_instruction)

            elif opcode == "mul":
                dest_reg = self.register_mapping[instruction[1]]
                src_reg1 = self.register_mapping[instruction[2]]
                src_reg_or_value = instruction[3]
                if isinstance(src_reg_or_value, int):
                    src_reg2 = 0  # Use r0 as a placeholder for immediate values
                    src_val2 = src_reg_or_value
                else:
                    src_reg2 = self.register_mapping[src_reg_or_value]
                    src_val2 = 0  # Placeholder for the source register value

                self.registers[dest_reg] = self.registers[src_reg1] * \
                    src_val2

                # Encoding for "mul" instruction
                encoded_instruction = "0011{:03}{:03}{:03}".format(
                    src_reg1, src_reg2, dest_reg)
                self.encoded_instructions.append(encoded_instruction)

            elif opcode == "div":
                dest_reg = self.register_mapping[instruction[1]]
                src_reg1 = self.register_mapping[instruction[2]]
                src_reg_or_value = instruction[3]
                if isinstance(src_reg_or_value, int):
                    src_reg2 = 0  # Use r0 as a placeholder for immediate values
                    src_val2 = src_reg_or_value
                else:
                    src_reg2 = self.register_mapping[src_reg_or_value]
                    src_val2 = 0  # Placeholder for the source register value

                self.registers[dest_reg] = self.registers[src_reg1] // self.registers[src_reg2]

                # Encoding for "div" instruction
                encoded_instruction = "0100{:03}{:03}{:03}".format(
                    src_reg1, src_reg2, dest_reg)
                self.encoded_instructions.append(encoded_instruction)

            elif opcode == "end":
                break  # Exit the program

            self.pc += 1
            self.cycles += 1

    def run(self, program):
        self.execute(program)
        cpi = self.cycles / len(program)
        print("Encoded Instructions:")
        for i, encoded_instruction in enumerate(self.encoded_instructions):
            print(f"{i}: {encoded_instruction}")
        print("Registers:", self.registers)
        print("CPI:", cpi)


# Example program
program = [
    ["mov", "r1", 3],
    ["add", "r1", "r1", 3],
    ["sub", "r2", "r1", 2],
    ["mul", "r3", "r2", 4],
    ["div", "r4", "r3", 2],
    ["end", 0, 0],
]

cpu = CPU()
cpu.run(program)
