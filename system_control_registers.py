import argparse
from pprint import pprint as pp

def bfsr_decode(bfsr: int) -> dict:

    bfsr_dict = dict()

    BFSR_BFARVALID_MASK     = 0b10000000
    BFSR_BFARVALID_SHIFT    = 7
    BFSR_LSPERR_MASK        = 0b00100000
    BFSR_LSPERR_SHIFT       = 5
    BFSR_STKERR_MASK        = 0b00010000
    BFSR_STKERR_SHIFT       = 4
    BFSR_UNSTKERR_MASK      = 0b00001000
    BFSR_UNSTKERR_SHIFT     = 3
    BFSR_IMPRECISERR_MASK   = 0b00000100
    BFSR_IMPRECISERR_SHIFT  = 2
    BFSR_PRECISERR_MASK     = 0b00000010
    BFSR_PRECISERR_SHIFT    = 1
    BFSR_IBUSERR_MASK       = 0b00000001
    BFSR_IBUSERR_SHIFT      = 0

    bfsr_bitfields = {
        "BFARVALID": {
            "mask":     BFSR_BFARVALID_MASK,
            "shift":    BFSR_BFARVALID_SHIFT
        },
        "LSPERR": {
            "mask":     BFSR_LSPERR_MASK,
            "shift":    BFSR_LSPERR_SHIFT
        },
        "STKERR": {
            "mask":     BFSR_STKERR_MASK,
            "shift":    BFSR_STKERR_SHIFT
        },
        "UNSTKERR": {
            "mask":     BFSR_UNSTKERR_MASK,
            "shift":    BFSR_UNSTKERR_SHIFT
        },
        "IMPRECISERR": {
            "mask":     BFSR_IMPRECISERR_MASK,
            "shift":    BFSR_IMPRECISERR_SHIFT
        },
        "PRECISERR": {
            "mask":     BFSR_PRECISERR_MASK,
            "shift":    BFSR_PRECISERR_SHIFT
        },
        "IBUSERR": {
            "mask":     BFSR_IBUSERR_MASK,
            "shift":    BFSR_IBUSERR_SHIFT
        }
    }

    for bitfield in bfsr_bitfields.keys():
        bfsr_dict[bitfield] = (bfsr & bfsr_bitfields[bitfield]["mask"]) >> bfsr_bitfields[bitfield]["shift"]

    bfsr_dict["_raw"] = bfsr

    return bfsr_dict

def ufsr_decode(ufsr: int) -> dict:

    ufsr_dict = dict()

    UFSR_DIVBYZERO_MASK     = 0b0000001000000000
    UFSR_DIVBYZERO_SHIFT    = 9
    UFSR_UNALIGNED_MASK     = 0b0000000100000000
    UFSR_UNALIGNED_SHIFT    = 8
    UFSR_NOCP_MASK          = 0b0000000000001000
    UFSR_NOCP_SHIFT         = 3
    UFSR_INVPC_MASK         = 0b0000000000000100
    UFSR_INVPC_SHIFT        = 2
    UFSR_INVSTATE_MASK      = 0b0000000000000010
    UFSR_INVSTATE_SHIFT     = 1
    UFSR_UNDEFINSTR_MASK    = 0b0000000000000001
    UFSR_UNDEFINSTR_SHIFT   = 0

    ufsr_bitfields = {
        "DIVBYZERO": {
            "mask": UFSR_DIVBYZERO_MASK,
            "shift": UFSR_DIVBYZERO_SHIFT
        },
        "UNALIGNED": {
            "mask": UFSR_UNALIGNED_MASK,
            "shift": UFSR_UNALIGNED_SHIFT
        },
        "NOCP": {
            "mask": UFSR_NOCP_MASK,
            "shift": UFSR_NOCP_SHIFT
        },
        "INVPC": {
            "mask": UFSR_INVPC_MASK,
            "shift": UFSR_INVPC_SHIFT
        },
        "INVSTATE": {
            "mask": UFSR_INVSTATE_MASK,
            "shift": UFSR_INVSTATE_SHIFT
        },
        "UNDEFINSTR": {
            "mask": UFSR_UNDEFINSTR_MASK,
            "shift": UFSR_UNDEFINSTR_SHIFT
        }
    }

    for bitfield in ufsr_bitfields.keys():
        ufsr_dict[bitfield] = (ufsr & ufsr_bitfields[bitfield]["mask"]) >> ufsr_bitfields[bitfield]["shift"]

    ufsr_dict["_raw"] = ufsr

    return ufsr_dict

def mmfsr_decode(mmfsr: int) -> dict:
    
    mmfsr_dict = dict()

    MMFSR_MMARVALID_MASK    = 0b10000000
    MMFSR_MMARVALID_SHIFT   = 7
    MMFSR_MLSPERR_MASK      = 0b00100000
    MMFSR_MLSPERR_SHIFT     = 5
    MMFSR_MSTKERR_MASK      = 0b00010000
    MMFSR_MSTKERR_SHIFT     = 4
    MMFSR_MUNSTKERR_MASK    = 0b00001000
    MMFSR_MUNSTKERR_SHIFT   = 3
    MMFSR_DACCVIOL_MASK     = 0b00000010
    MMFSR_DACCVIOL_SHIFT    = 1
    MMFSR_IACCVIOL_MASK     = 0b00000001
    MMFSR_IACCVIOL_SHIFT    = 0

    mmfsr_bitfields = {
       "MMARVALID": {
            "mask": MMFSR_MMARVALID_MASK,
            "shift": MMFSR_MMARVALID_SHIFT
       },
        "MLSPERR": {
            "mask": MMFSR_MLSPERR_MASK,
            "shift": MMFSR_MLSPERR_SHIFT
        },
        "MSTKERR": {
            "mask": MMFSR_MSTKERR_MASK,
            "shift": MMFSR_MSTKERR_SHIFT
        },
        "MUNSTKERR": {
            "mask": MMFSR_MUNSTKERR_MASK,
            "shift": MMFSR_MUNSTKERR_SHIFT
        },
        "DACCVIOL": {
            "mask": MMFSR_DACCVIOL_MASK,
            "shift": MMFSR_DACCVIOL_SHIFT
        },
        "IACCVIOL": {
            "mask": MMFSR_IACCVIOL_MASK,
            "shift": MMFSR_IACCVIOL_SHIFT
        }
    }

    for bitfield in mmfsr_bitfields.keys():
        mmfsr_dict[bitfield] = (mmfsr & mmfsr_bitfields[bitfield]["mask"]) >> mmfsr_bitfields[bitfield]["shift"]

    mmfsr_dict["_raw"] = mmfsr

    return mmfsr_dict

def cfsr_decode(cfsr: int) -> dict:
    """parse cfsr for bfsr, ufsr, and mmfsr"""

    CFSR_MMFSR_MASK     = 0x000000FF
    CFSR_MMFSR_SHIFT    = 0
    CFSR_BFSR_MASK      = 0x0000FF00
    CFSR_BFSR_SHIFT     = 8
    CFSR_UFSR_MASK      = 0xFFFF0000
    CFSR_UFSR_SHIFT     = 16

    bfsr    = bfsr_decode((cfsr & CFSR_BFSR_MASK) >> CFSR_BFSR_SHIFT)
    ufsr    = ufsr_decode((cfsr & CFSR_UFSR_MASK) >> CFSR_UFSR_SHIFT)
    mmfsr   = mmfsr_decode((cfsr & CFSR_MMFSR_MASK) >> CFSR_MMFSR_SHIFT)

    return {
        "BFSR": bfsr,
        "UFSR": ufsr,
        "MMFSR": mmfsr
    }

def bfsr_report(bfsr: dict) -> str:

    bfsr_bitfield_template = f"""{bfsr["BFARVALID"]}│ │{bfsr["LSPERR"]}│{bfsr["STKERR"]}│{bfsr["UNSTKERR"]}│{bfsr["IMPRECISERR"]}│{bfsr["PRECISERR"]}│{bfsr["IBUSERR"]}"""

    bfsr_bitfield_str = f"""
=======================================
BFSR: 0x{bfsr["_raw"]:02X}
---------------------------------------

         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │{bfsr_bitfield_template}│
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
BFARVALID─┘ │ │ │ │ │ │ └─IBUSERR
 reserved───┘ │ │ │ │ └───PRECISERR
   LSPERR─────┘ │ │ └─────IMPRECISERR
   STKERR───────┘ └───────UNSTKERR

=======================================
"""
    if bfsr["BFARVALID"]:
        bfsr_bitfield_str += "BFARVALID: BFAR has valid contents\n"
    else:
        bfsr_bitfield_str += "BFARVALID: BFAR does not have valid contents\n"
    
    if bfsr["LSPERR"]:
        bfsr_bitfield_str += "LSPERR: A bus fault occurred during FP lazy state preservation\n"

    if bfsr["STKERR"]:
        bfsr_bitfield_str += "STKERR: A derived bus fault has occurred on exception entry\n"

    if bfsr["UNSTKERR"]:
        bfsr_bitfield_str += "UNSTKERR: A derived bus fault has occurred on exception return\n"

    if bfsr["IMPRECISERR"]:
        bfsr_bitfield_str += "IMPRECISERR: An imprecise data access error has occured\n"

    if bfsr["PRECISERR"]:
        bfsr_bitfield_str += "PRECISERR: A precise data access error has occurred, and the processor has written the faulting address to the BFAR\n"

    if bfsr["IBUSERR"]:
        bfsr_bitfield_str += "A bus fault on an instruction prefetch has occurred. The fault is signlaed only if the instruction is issued\n"

    return bfsr_bitfield_str

def ufsr_report(ufsr: dict) -> str:

    ufsr_bitfield_template = f"""  reserved  │{ufsr["DIVBYZERO"]}│{ufsr["UNALIGNED"]}│  res. │{ufsr["NOCP"]}│{ufsr["INVPC"]}│{ufsr["INVSTATE"]}│{ufsr["UNDEFINSTR"]}"""

    ufsr_bitfield_str = f"""
=======================================
UFSR: 0x{ufsr["_raw"]:02X}
---------------------------------------

│15      │ 10 9 8│7     4│3 2 1 0│
├────────┴───┬─┬─┼───────┼─┬─┬─┬─┤
│{ufsr_bitfield_template}│
└────────────┴▲┴▲┴───────┴▲┴▲┴▲┴▲┘
    DIVBYZERO─┘ │    NOCP─┘ │ │ │
    UNALIGNED───┘   INVPC───┘ │ │
                 INVSTATE─────┘ │
               UNDEFINSTR───────┘

========================================
"""

    if ufsr["DIVBYZERO"]:
        ufsr_bitfield_str += "DIVBYZERO: Divide by zero error has occurred\n"

    if ufsr["UNALIGNED"]:
        ufsr_bitfield_str += "UNALIGNED: Unaligned access error has occurred\n"

    if ufsr["NOCP"]:
        ufsr_bitfield_str += "NOCP: A coprocessor access error has occurred. This shows that the coprocessor is disabled or not present\n"

    if ufsr["INVPC"]:
        ufsr_bitfield_str += "INVPC: An integrity check error has occurred on EXC_RETURN\n"

    if ufsr["INVSTATE"]:
        ufsr_bitfield_str += "INVSTATE: Instruction executed with invalid EPSR.T or EPSR.IT field\n"
    
    if ufsr["UNDEFINSTR"]:
        ufsr_bitfield_str += "UNDEFINSTR: The processor has attempted to execute an undefined instruction. This might be an undefined instruction associated with an enabled coprocessor\n"

    return ufsr_bitfield_str

def mmfsr_report(mmfsr: dict) -> str:

    mmfsr_bitfield_template = f"""{mmfsr["MMARVALID"]}│ │{mmfsr["MLSPERR"]}│{mmfsr["MSTKERR"]}│{mmfsr["MUNSTKERR"]}│ │{mmfsr["DACCVIOL"]}│{mmfsr["IACCVIOL"]}"""

    mmfsr_bitfield_str = f"""
========================================
MMFSR: 0x{mmfsr["_raw"]:02X}
----------------------------------------

         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │{mmfsr_bitfield_template}│
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
MMARVALID─┘ │ │ │ │ │ │ └─IACCVIOL
 Reserved───┘ │ │ │ │ └───DACCVIOL
  MLSPERR─────┘ │ │ └─────Reserved
  MSTKERR───────┘ └───────MUNSTKERR

========================================
"""

    if mmfsr["MMARVALID"]:
        mmfsr_bitfield_str += "MMARVALID: MMFAR has valid contents\n"
    else:
        mmfsr_bitfield_str += "MMARVALID: MMFAR does not have valid contents\n"
    
    if mmfsr["MLSPERR"]:
        mmfsr_bitfield_str += "MLSPERR: A MemManage fault occurred during FP lazy state preservation\n"

    if mmfsr["MSTKERR"]:
        mmfsr_bitfield_str += "MSTKERR: A derived MemManage fault has occurred on exception entry\n"

    if mmfsr["MUNSTKERR"]:
        mmfsr_bitfield_str += "MUNSTKERR: A derived MemManage fault has occurred on exception return\n"

    if mmfsr["DACCVIOL"]:
        mmfsr_bitfield_str += "DACCVIOL: Data access violation. The MMFAR shows the data address that the load or store tried to access\n"

    if mmfsr["IACCVIOL"]:
        mmfsr_bitfield_str += "IACCVIOL: MPU or Execute Never (XN) default memory map access violation on an instruction fetch has occurred. The fault is signaled only if the instruction is issued\n"


    return mmfsr_bitfield_str

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Decode Configurable Fault Status Register (CFSR)")
    parser.add_argument('CFSR', type=lambda x: int(x, 0), help="the CFSR value from the ARM device")

    args = parser.parse_args()
    cfsr = cfsr_decode(args.CFSR)

    print(ufsr_report(cfsr["UFSR"]))
    print(bfsr_report(cfsr["BFSR"]))
    print(mmfsr_report(cfsr["MMFSR"]))