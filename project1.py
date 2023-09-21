class CPU:
    def __init__(self):
        self.registers = [0] * 8  # 8 general-purpose registers
        self.memory = [0] * 256  # 256 bytes of memory
        self.pc = 0  # Program Counter
        self.clock_cycles = 0  # Total clock cycles

    def mov(self, dest_reg, value):
        self.registers[dest_reg] = value
        self.clock_cycles += 1

    def add(self, dest_reg, src_reg):
        self.registers[dest_reg] += self.registers[src_reg]
        self.clock_cycles += 1

    def sub(self, dest_reg, src_reg):
        self.registers[dest_reg] -= self.registers[src_reg]
        self.clock_cycles += 1

    def execute(self, opcode, dest_reg, src_reg, immediate):
        if opcode == 1:  # MOV
            self.mov(dest_reg, immediate)
        elif opcode == 2:  # ADD
            self.add(dest_reg, src_reg)
        elif opcode == 3:  # SUB
            self.sub(dest_reg, src_reg)
        else:
            raise Exception("Invalid opcode")

    def load_program(self, program):
        self.memory[:len(program)] = program

    def run(self):
        while self.pc < len(self.memory):
            instruction = self.memory[self.pc]
            opcode = (instruction >> 24) & 0xFF  # Extract the opcode (bits 25-32)
            dest_reg = (instruction >> 16) & 0xFF  # Extract the destination register (bits 17-24)
            src_reg = (instruction >> 8) & 0xFF  # Extract the source register (bits 9-16)
            immediate = instruction & 0xFF  # Extract the immediate value (bits 1-8)
            self.execute(opcode, dest_reg, src_reg, immediate)
            self.pc += 1

    def get_cpi(self):
        if self.pc == 0:
            return 0
        return self.clock_cycles / self.pc

if __name__ == "__main__":
    cpu = CPU()
    program = [
        0x01010003,  # MOV R1, 3
        0x02020001,  # ADD R2, R1
        0x03030002,  # SUB R3, R2
    ]
    cpu.load_program(program)
    cpu.run()
    print("Registers after execution:", cpu.registers)
    print("CPI:", cpu.get_cpi())
