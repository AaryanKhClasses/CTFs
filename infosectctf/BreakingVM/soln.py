#!/usr/bin/env python3
import struct

VM_MEM_FILE = "vm_mem.bin"
ROL_OFFSET = 1822

PUTCHAR = 2984
HALT = 0xE08

def rol16(x, r):
    x &= 0xFFFF
    return ((x << r) | (x >> (16 - r))) & 0xFFFF

# Load VM memory
with open(VM_MEM_FILE, "rb") as f:
    raw = f.read()

mem = list(struct.unpack("<" + "H" * (len(raw)//2), raw))
VM_WORDS = len(mem)

# VM state
R = [0] * 16
PC = 0
SP = VM_WORDS      # IMPORTANT: stack starts at end of VM RAM
Z = False
N = False

output = []

def set_flags(v):
    global Z, N
    v &= 0xFFFF
    Z = (v == 0)
    N = (v & 0x8000) != 0

MAX_STEPS = 300000

for _ in range(MAX_STEPS):
    PC %= VM_WORDS

    key = rol16(PC - ROL_OFFSET, 8)
    instr = mem[PC] ^ key
    PC += 1

    opcode = instr >> 12
    a2 = instr & 0x0FFF

    # MOV
    if opcode == 10:
        rd = (a2 >> 8) & 0xF
        if a2 & 0x80:
            imm = a2 | 0xFF80 if (a2 & 0x40) else (a2 & 0x7F)
            R[rd] = imm & 0xFFFF
        else:
            R[rd] = R[a2 & 0xF]
        set_flags(R[rd])

    # ADD
    elif opcode == 11:
        rd = (a2 >> 8) & 0xF
        if a2 & 0x80:
            val = a2 | 0xFF80 if (a2 & 0x40) else (a2 & 0x7F)
        else:
            val = R[a2 & 0xF]
        R[rd] = (R[rd] + val) & 0xFFFF
        set_flags(R[rd])

    # SUB
    elif opcode == 12:
        rd = (a2 >> 8) & 0xF
        if a2 & 0x80:
            val = a2 | 0xFF80 if (a2 & 0x40) else (a2 & 0x7F)
        else:
            val = R[a2 & 0xF]
        R[rd] = (R[rd] - val) & 0xFFFF
        set_flags(R[rd])

    # LOAD
    elif opcode == 15:  # LOAD
        rd = (instr >> 8) & 0xF
        base = (a2 >> 4) & 0xF

        off4 = a2 & 0xF
        if a2 & 0x8:
            off4 |= 0xFFF0

        addr = (R[base] + off4) % VM_WORDS
        R[rd] = mem[addr]
        set_flags(R[rd])


    # PUSH
    elif opcode == 5:
        SP = (SP - 1) % VM_WORDS
        mem[SP] = R[(a2 >> 8) & 0xF]

    # POP
    elif opcode == 6:
        R[(a2 >> 8) & 0xF] = mem[SP]
        SP = (SP + 1) % VM_WORDS
        set_flags(R[(a2 >> 8) & 0xF])

    # JMP
    elif opcode == 2:
        PC = (PC & 0xF000) | a2

    # JCC
    elif opcode == 3:
        cond = a2 >> 9
        off = a2 | 0xFE00 if a2 & 0x100 else a2 & 0x1FF
        take = (
            (cond == 0 and Z) or
            (cond == 1 and not Z) or
            (cond == 2 and N) or
            (cond == 3 and (N or Z))
        )
        if take:
            PC = (PC + off) & 0xFFFF

    # VM_INT
    elif opcode == 7:
        trap = a2 & 0xFF8
        print(f"[VM_INT] PC={PC-1:04x} trap={trap}")


# Print result
print("".join(output))
