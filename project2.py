class CPU:
    def __init__(self):
        self.registers = [0] * 8  # 8 general-purpose registers
        self.memory = [0] * 1024  # 1024 words of memory
        self.pc = 0  # Program Counter

    def load_program(self, program):
        for i, value in enumerate(program):
            self.memory[i] = value

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def decode_execute(self, instruction):
        opcode = (instruction >> 24) & 0xFF
        src_reg = (instruction >> 16) & 0xFF
        dest_reg = (instruction >> 8) & 0xFF
        immediate = instruction & 0xFF

        if opcode == 0:  # Halt
            return False
        elif opcode == 1:  # Move
            self.registers[dest_reg] = immediate
        elif opcode == 2:  # Add
            self.registers[dest_reg] = self.registers[src_reg] + immediate
        elif opcode == 3:  # Subtract
            self.registers[dest_reg] = self.registers[src_reg] - immediate
        elif opcode == 4:  # Multiply
            self.registers[dest_reg] = self.registers[src_reg] * immediate
        elif opcode == 5:  # Divide
            if immediate == 0:
                print("Division by zero error!")
            else:
                self.registers[dest_reg] = self.registers[src_reg] / immediate

        return True

    def run(self):
        while True:
            instruction = self.fetch()
            if not self.decode_execute(instruction):
                break

    def dump_registers(self):
        for i, value in enumerate(self.registers):
            print(f"r{i}: {value}")


# # Example program
# program = [
#     0x01020304,  # mov r1, 4
#     0x02010302,  # add r3, r1, 2
#     0x03030405,  # sub r4, r4, 5
#     0x04020700,  # mul r7, r0, 0
#     0x05030100,  # div r3, r1, 0 (division by zero)
#     0x00000000,  # halt
# ]

# cpu = CPU()
# cpu.load_program(program)
# cpu.run()
# cpu.dump_registers()

# Example program without division by zero
program = [
    0x01020304,  # mov r1, 4
    0x02010302,  # add r3, r1, 2
    0x03030405,  # sub r4, r4, 5
    0x04020600,  # mul r6, r0, 0
    0x05030302,  # div r3, r3, 2 (division by 2)
    0x00000000,  # halt
]

cpu = CPU()
cpu.load_program(program)
cpu.run()
cpu.dump_registers()
