import argparse
from pprint import pprint as pp
from tabulate import tabulate

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
===============================================================================
BFSR: 0x{bfsr["_raw"]:02X}
-------------------------------------------------------------------------------

         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │{bfsr_bitfield_template}│
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
BFARVALID─┘ │ │ │ │ │ │ └─IBUSERR
 reserved───┘ │ │ │ │ └───PRECISERR
   LSPERR─────┘ │ │ └─────IMPRECISERR
   STKERR───────┘ └───────UNSTKERR

-------------------------------------------------------------------------------
"""

    bfsr_desc = list()

    if bfsr["BFARVALID"]:
        bfsr_desc.append(["BFARVALID", "BFAR has valid contents"])
    else:
        bfsr_desc.append(["BFARVALID", "BFAR does not have valid contents"])
    
    if bfsr["LSPERR"]:
        bfsr_desc.append(["LSPERR", "A bus fault occurred during FP lazy state preservation"])

    if bfsr["STKERR"]:
        bfsr_desc.append(["STKERR", "A derived bus fault has occurred on exception entry"])

    if bfsr["UNSTKERR"]:
        bfsr_desc.append(["UNSTKERR", "A derived bus fault has occurred on exception return"])

    if bfsr["IMPRECISERR"]:
        bfsr_desc.append(["IMPRECISERR", "An imprecise data access error has occured"])

    if bfsr["PRECISERR"]:
        bfsr_desc.append(["PRECISERR", "A precise data access error has occurred, and the processor has written the faulting address to the BFAR"])

    if bfsr["IBUSERR"]:
        bfsr_desc.append(["IBUSERR", "A bus fault on an instruction prefetch has occurred. The fault is signlaed only if the instruction is issued"])

    bfsr_bitfield_str += tabulate(bfsr_desc, tablefmt="simple_grid", maxcolwidths=[None, 65])

    bfsr_bitfield_str += "\n==============================================================================="

    return bfsr_bitfield_str

def ufsr_report(ufsr: dict) -> str:

    ufsr_bitfield_template = f"""  reserved  │{ufsr["DIVBYZERO"]}│{ufsr["UNALIGNED"]}│  res. │{ufsr["NOCP"]}│{ufsr["INVPC"]}│{ufsr["INVSTATE"]}│{ufsr["UNDEFINSTR"]}"""

    ufsr_bitfield_str = f"""
===============================================================================
UFSR: 0x{ufsr["_raw"]:02X}
-------------------------------------------------------------------------------

│15      │ 10 9 8│7     4│3 2 1 0│
├────────┴───┬─┬─┼───────┼─┬─┬─┬─┤
│{ufsr_bitfield_template}│
└────────────┴▲┴▲┴───────┴▲┴▲┴▲┴▲┘
    DIVBYZERO─┘ │    NOCP─┘ │ │ │
    UNALIGNED───┘   INVPC───┘ │ │
                 INVSTATE─────┘ │
               UNDEFINSTR───────┘

-------------------------------------------------------------------------------
"""

    ufsr_desc = list()

    if ufsr["DIVBYZERO"]:
        ufsr_desc.append(["DIVBYZERO", "Divide by zero error has occurred"])

    if ufsr["UNALIGNED"]:
        ufsr_desc.append(["UNALIGNED", "Unaligned access error has occurred"])

    if ufsr["NOCP"]:
        ufsr_desc.append(["NOCP", "A coprocessor access error has occurred. This shows that the coprocessor is disabled or not present"])

    if ufsr["INVPC"]:
        ufsr_desc.append(["INVPC", "An integrity check error has occurred on EXC_RETURN"])

    if ufsr["INVSTATE"]:
        ufsr_desc.append(["INVSTATE", "Instruction executed with invalid EPSR.T or EPSR.IT field"])
    
    if ufsr["UNDEFINSTR"]:
        ufsr_desc.append(["UNDEFINSTR", "The processor has attempted to execute an undefined instruction. This might be an undefined instruction associated with an enabled coprocessor"])

    ufsr_bitfield_str += tabulate(ufsr_desc, tablefmt="simple_grid", maxcolwidths=[None, 65])

    ufsr_bitfield_str += "\n==============================================================================="

    return ufsr_bitfield_str

def mmfsr_report(mmfsr: dict) -> str:

    mmfsr_bitfield_template = f"""{mmfsr["MMARVALID"]}│ │{mmfsr["MLSPERR"]}│{mmfsr["MSTKERR"]}│{mmfsr["MUNSTKERR"]}│ │{mmfsr["DACCVIOL"]}│{mmfsr["IACCVIOL"]}"""

    mmfsr_bitfield_str = f"""
===============================================================================
MMFSR: 0x{mmfsr["_raw"]:02X}
-------------------------------------------------------------------------------

         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │{mmfsr_bitfield_template}│
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
MMARVALID─┘ │ │ │ │ │ │ └─IACCVIOL
 Reserved───┘ │ │ │ │ └───DACCVIOL
  MLSPERR─────┘ │ │ └─────Reserved
  MSTKERR───────┘ └───────MUNSTKERR

-------------------------------------------------------------------------------
"""

    mmfsr_desc = list()

    if mmfsr["MMARVALID"]:
        mmfsr_desc.append(["MMARVALID", "MMFAR has valid contents"])
    else:
        mmfsr_desc.append(["MMARVALID", "MMFAR does not have valid contents"])
    
    if mmfsr["MLSPERR"]:
        mmfsr_desc.append(["MLSPERR", "A MemManage fault occurred during FP lazy state preservation"])

    if mmfsr["MSTKERR"]:
        mmfsr_desc.append(["MSTKERR", "A derived MemManage fault has occurred on exception entry"])

    if mmfsr["MUNSTKERR"]:
        mmfsr_desc.append(["MUNSTKERR", "A derived MemManage fault has occurred on exception return"])

    if mmfsr["DACCVIOL"]:
        mmfsr_desc.append(["DACCVIOL", "Data access violation. The MMFAR shows the data address that the load or store tried to access"])

    if mmfsr["IACCVIOL"]:
        mmfsr_desc.append(["IACCVIOL", "MPU or Execute Never (XN) default memory map access violation on an instruction fetch has occurred. The fault is signaled only if the instruction is issued"])

    mmfsr_bitfield_str += tabulate(mmfsr_desc, tablefmt="simple_grid", maxcolwidths=[None, 65])

    mmfsr_bitfield_str += "\n==============================================================================="

    return mmfsr_bitfield_str

def hfsr_decode(hfsr: int) -> dict:

    hfsr_dict = dict()

    HFSR_DEBUGEVT_MASK      = 0x80000000
    HFSR_DEBUGEVT_SHIFT     = 31
    HFSR_FORCED_MASK        = 0x40000000
    HFSR_FORCED_SHIFT       = 30
    HFSR_VECTTBL_MASK       = 0x00000002
    HFSR_VECTTBL_SHIFT      = 1

    hfsr_bitfields = {
        "DEBUGEVT": {
            "mask": HFSR_DEBUGEVT_MASK,
            "shift": HFSR_DEBUGEVT_SHIFT
        },
        "FORCED": {
            "mask": HFSR_FORCED_MASK,
            "shift": HFSR_FORCED_SHIFT
        },
        "VECTTBL": {
            "mask": HFSR_VECTTBL_MASK,
            "shift": HFSR_VECTTBL_SHIFT
        }
    }

    for bitfield in hfsr_bitfields.keys():
        hfsr_dict[bitfield] = (hfsr & hfsr_bitfields[bitfield]["mask"]) >> hfsr_bitfields[bitfield]["shift"]

    hfsr_dict["_raw"] = hfsr

    return hfsr_dict
    
def hfsr_report(hfsr: dict) -> str:
    
    hfsr_bitfield_template = f"""{hfsr["DEBUGEVT"]}│{hfsr["FORCED"]}│          RESERVED          │{hfsr["VECTTBL"]}│ """

    hfsr_bitfield_str = f"""
===============================================================================
HFSR: 0x{hfsr["_raw"]:02X}
-------------------------------------------------------------------------------

│31 │29                          │1│0│
├─┬─┼────────────────────────────┼─┼─┤
│{hfsr_bitfield_template}│
└▲┴▲┴────────────────────────────┴▲┴▲┘
 │ └─FORCED               VECTTBL─┘ │
 └───DEBUGEVT            RESERVED───┘

-------------------------------------------------------------------------------
"""

    hfsr_desc = list()

    if hfsr["DEBUGEVT"]:
        hfsr_desc.append(["DEBUGEVT", "Reserved for Debug Use. When writing to the register you must write 1 to this bit, otherwise behaviour is unpredictable"])

    if hfsr["FORCED"]:
        hfsr_desc.append(["FORCED", "Indicates a forced HardFault, generated by escalation of a fault with configurable priority that cannot be handled, either because of priority or because it is disabled. When this bit is set to 1, the HardFault handler must read the other fault status registers to find the cause of the fault"])

    if hfsr["VECTTBL"]:
        hfsr_desc.append(["VECTTBL", "Indicates a HardFault on a vector table read during exception processing. This error is always handled by the HardFault handler. When this bit is set to 1, the PC value stacked for hte exception return points to the instruction that was pre-empted by the exception"])

    hfsr_bitfield_str += tabulate(hfsr_desc, tablefmt="simple_grid", maxcolwidths=[None, 65])

    hfsr_bitfield_str += "\n==============================================================================="

    return hfsr_bitfield_str

def shcsr_decode(shcsr: int) -> dict:

    shcsr_dict = dict()

    SHCSR_USGFAULTENA_MASK      = 0x00040000
    SHCSR_USGFAULTENA_SHIFT     = 18
    SHCSR_BUSFAULTENA_MASK      = 0x00020000
    SHCSR_BUSFAULTENA_SHIFT     = 17
    SHCSR_MEMFAULTENA_MASK      = 0x00010000
    SHCSR_MEMFAULTENA_SHIFT     = 16
    SHCSR_SVCALLPENDED_MASK     = 0x00008000
    SHCSR_SVCALLPENDED_SHIFT    = 15
    SHCSR_BUSFAULTPENDED_MASK   = 0x00004000
    SHCSR_BUSFAULTPENDED_SHIFT  = 14
    SHCSR_MEMFAULTPENDED_MASK   = 0x00002000
    SHCSR_MEMFAULTPENDED_SHIFT  = 13
    SHCSR_USGFAULTPENDED_MASK   = 0x00001000
    SHCSR_USGFAULTPENDED_SHIFT  = 12
    SHCSR_SYSTICKACT_MASK       = 0x00000800
    SHCSR_SYSTICKACT_SHIFT      = 11
    SHCSR_PENDSVACT_MASK        = 0x00000400
    SHCSR_PENDSVACT_SHIFT       = 10
    SHCSR_MONITORACT_MASK       = 0x00000100
    SHCSR_MONITORACT_SHIFT      = 8
    SHCSR_SVCALLACT_MASK        = 0x00000080
    SHCSR_SVCALLACT_SHIFT       = 7
    SHCSR_USGFAULTACT_MASK      = 0x00000008
    SHCSR_USGFAULTACT_SHIFT     = 3
    SHCSR_BUSFAULTACT_MASK      = 0x00000002
    SHCSR_BUSFAULTACT_SHIFT     = 1
    SHCSR_MEMFAULTACT_MASK      = 0x00000001
    SHCSR_MEMFAULTACT_SHIFT     = 0

    shcsr_bitfields = {
        "USGFAULTENA": {
            "mask": SHCSR_USGFAULTENA_MASK,
            "shift": SHCSR_USGFAULTENA_SHIFT
        },
        "BUSFAULTENA": {
            "mask": SHCSR_BUSFAULTENA_MASK,
            "shift": SHCSR_BUSFAULTENA_SHIFT
        },
        "MEMFAULTENA": {
            "mask": SHCSR_MEMFAULTENA_MASK,
            "shift": SHCSR_MEMFAULTENA_SHIFT
        },
        "SVCALLPENDED": {
            "mask": SHCSR_SVCALLPENDED_MASK,
            "shift": SHCSR_SVCALLPENDED_SHIFT
        },
        "BUSFAULTPENDED": {
            "mask": SHCSR_BUSFAULTPENDED_MASK,
            "shift": SHCSR_BUSFAULTPENDED_SHIFT
        },
        "MEMFAULTPENDED": {
            "mask": SHCSR_MEMFAULTPENDED_MASK,
            "shift": SHCSR_MEMFAULTPENDED_SHIFT
        },
        "USGFAULTPENDED": {
            "mask": SHCSR_USGFAULTPENDED_MASK,
            "shift": SHCSR_USGFAULTPENDED_SHIFT
        },
        "SYSTICKACT": {
            "mask": SHCSR_SYSTICKACT_MASK,
            "shift": SHCSR_SYSTICKACT_SHIFT
        },
        "PENDSVACT": {
            "mask": SHCSR_PENDSVACT_MASK,
            "shift": SHCSR_PENDSVACT_SHIFT
        },
        "MONITORACT": {
            "mask": SHCSR_MONITORACT_MASK,
            "shift": SHCSR_MONITORACT_SHIFT
        },
        "SVCALLACT": {
            "mask": SHCSR_SVCALLACT_MASK,
            "shift": SHCSR_SVCALLACT_SHIFT
        },
        "USGFAULTACT": {
            "mask": SHCSR_USGFAULTACT_MASK,
            "shift": SHCSR_USGFAULTACT_SHIFT
        },
        "BUSFAULTACT": {
            "mask": SHCSR_BUSFAULTACT_MASK,
            "shift": SHCSR_BUSFAULTACT_SHIFT
        },
        "MEMFAULTACT": {
            "mask": SHCSR_MEMFAULTACT_MASK,
            "shift": SHCSR_MEMFAULTACT_SHIFT
        }
    }

    for bitfield in shcsr_bitfields.keys():
        shcsr_dict[bitfield] = (shcsr & shcsr_bitfields[bitfield]["mask"]) >> shcsr_bitfields[bitfield]["shift"]

    shcsr_dict["_raw"] = shcsr

    return shcsr_dict

def shcsr_report(shcsr: dict) -> str:

    shcsr_bitfield_template = f"""        RESERVED         │{shcsr["USGFAULTENA"]}│{shcsr["BUSFAULTENA"]}│{shcsr["MEMFAULTENA"]}│{shcsr["SVCALLPENDED"]}│{shcsr["BUSFAULTPENDED"]}│{shcsr["MEMFAULTPENDED"]}│{shcsr["USGFAULTPENDED"]}│{shcsr["SYSTICKACT"]}│{shcsr["PENDSVACT"]}│ │{shcsr["MONITORACT"]}│{shcsr["SVCALLACT"]}│ RES │{shcsr["USGFAULTACT"]}│ │{shcsr["BUSFAULTACT"]}│{shcsr["MEMFAULTACT"]}"""

    shcsr_bitfield_str = f"""
===============================================================================
SHCSR: 0x{shcsr["_raw"]:02X}
-------------------------------------------------------------------------------

                         1 1 1 1 1 1 1 1 1 1
│31                     │9 8 7 6│5 4 3 2│1 0 9 8│7 6   4│3 2 1 0│
├───────────────────────┴─┬─┬─┬─┼─┬─┬─┬─┼─┬─┬─┬─┼─┬─────┼─┬─┬─┬─┤
│{shcsr_bitfield_template}│
└─────────────────────────┴▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┴─────┴▲┴▲┴▲┴▲┘
               USGFAULTENA─┘ │ │ │ │ │ │ │ │ │ │ │       │ │ │ └─MEMFAULTACT
               BUSFAULTENA───┘ │ │ │ │ │ │ │ │ │ │       │ │ └───BUSFAULTACT
               MEMFAULTENA─────┘ │ │ │ │ │ │ │ │ │       │ └─────RESERVED
                    SVCALLPENDED─┘ │ │ │ │ │ │ │ │       └───────USGFAULTACT
                  BUSFAULTPENDED───┘ │ │ │ │ │ │ │
                  MEMFAULTPENDED─────┘ │ │ │ │ │ └─SVCALLACT
                  USGFAULTPENDED───────┘ │ │ │ └───MONITORACT
                              SYSTICKACT─┘ │ └─────RESERVED
                               PENDSVACT───┘

-------------------------------------------------------------------------------
"""

    shcsr_desc = list()

    if shcsr["USGFAULTENA"]:
        shcsr_desc.append(["USGFAULTENA", "UsageFault enabled"])

    if shcsr["BUSFAULTENA"]:
        shcsr_desc.append(["BUSFAULTENA", "BusFault enabled"])

    if shcsr["MEMFAULTENA"]:
        shcsr_desc.append(["MEMFAULTENA", "MemManage fault enabled"])

    if shcsr["SVCALLPENDED"]:
        shcsr_desc.append(["SVCALLPENDED", "SVCall is pending"])

    if shcsr["BUSFAULTPENDED"]:
        shcsr_desc.append(["BUSFAULTPENDED", "BusFault is pending"])

    if shcsr["MEMFAULTPENDED"]:
        shcsr_desc.append(["MEMFAULTPENDED", "MemManage fault is pending"])

    if shcsr["USGFAULTPENDED"]:
        shcsr_desc.append(["USGFAULTPENDED", "UsageFault is pending"])

    if shcsr["SYSTICKACT"]:
        shcsr_desc.append(["SYSTICKACT", "SysTick is active"])

    if shcsr["PENDSVACT"]:
        shcsr_desc.append(["PENDSVACT", "PendSV is active"])

    if shcsr["MONITORACT"]:
        shcsr_desc.append(["MONITORACT", "Monitor is active"])

    if shcsr["SVCALLACT"]:
        shcsr_desc.append(["SVCALLACT", "SVCall is active"])

    if shcsr["USGFAULTACT"]:
        shcsr_desc.append(["USGFAULTACT", "UsageFault is active"])

    if shcsr["BUSFAULTACT"]:
        shcsr_desc.append(["BUSFAULTACT", "BusFault is active"])

    if shcsr["MEMFAULTACT"]:
        shcsr_desc.append(["MEMFAULTACT", "MemManage fault is active"])

    shcsr_bitfield_str += tabulate(shcsr_desc, tablefmt="simple_grid", maxcolwidths=[None, 65])

    shcsr_bitfield_str += "\n==============================================================================="

    return shcsr_bitfield_str

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Analyze Fault causes on arm M-33 devices")
    parser.add_argument('--cfsr', dest="cfsr", type=lambda x: int(x, 0), required=False, help="the CFSR value from the ARM device")
    parser.add_argument('--hfsr', dest="hfsr", type=lambda x: int(x, 0), required=False, help="the HFSR value from the ARM device")
    parser.add_argument('--shcsr', dest="shcsr", type=lambda x: int(x, 0), required=False, help="the SHCSR value from the ARM device")

    args = parser.parse_args()

    report = ""

    if args.cfsr is not None:
        cfsr = cfsr_decode(args.cfsr)

        report += ufsr_report(cfsr["UFSR"])
        report += bfsr_report(cfsr["BFSR"])
        report += mmfsr_report(cfsr["MMFSR"])

    if args.hfsr is not None:
        hfsr = hfsr_decode(args.hfsr)

        report += hfsr_report(hfsr)

    if args.shcsr is not None:
        shcsr = shcsr_decode(args.shcsr)

        report += shcsr_report(shcsr)

    print(report)