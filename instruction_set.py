# instruction set

# R-type Instructions

R_TYPE_FUNC = {
        "add":"100000",
        "sub":"100010",
        "and":"100100",
        "or" :"100101",
        "slt":"101010",
}


# I-type Instructions

I_TYPE_OPCODE = {
        "addi":"001000",
        "andi":"001100",
        "ori" :"001101",
        "lw"  :"100011",
        "sw"  :"101011",
        "beq" :"000100",
        "bne" : "000101"
}


# J-type instructions
J_TYPE_OPCODE = {
    "j":   "000010",
    "jal": "000011"
}


# Special case (still R-type but unique behavior)
SPECIAL_FUNCT = {
    "jr": "001000"  # jr $ra
}


# Register name to number mapping
REGISTER_MAP = {
    "$zero": 0, "$at": 1,
    "$v0": 2, "$v1": 3,
    "$a0": 4, "$a1": 5, "$a2": 6, "$a3": 7,
    "$t0": 8, "$t1": 9, "$t2": 10, "$t3": 11,
    "$t4": 12, "$t5": 13, "$t6": 14, "$t7": 15,
    "$s0": 16, "$s1": 17, "$s2": 18, "$s3": 19,
    "$s4": 20, "$s5": 21, "$s6": 22, "$s7": 23,
    "$t8": 24, "$t9": 25,
    "$sp": 29, "$ra": 31
}
