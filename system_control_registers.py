import argparse
from register import Register

class BFSR(Register):

    _BFSR_BFARVALID_MASK     = 0b10000000
    _BFSR_BFARVALID_SHIFT    = 7
    _BFSR_LSPERR_MASK        = 0b00100000
    _BFSR_LSPERR_SHIFT       = 5
    _BFSR_STKERR_MASK        = 0b00010000
    _BFSR_STKERR_SHIFT       = 4
    _BFSR_UNSTKERR_MASK      = 0b00001000
    _BFSR_UNSTKERR_SHIFT     = 3
    _BFSR_IMPRECISERR_MASK   = 0b00000100
    _BFSR_IMPRECISERR_SHIFT  = 2
    _BFSR_PRECISERR_MASK     = 0b00000010
    _BFSR_PRECISERR_SHIFT    = 1
    _BFSR_IBUSERR_MASK       = 0b00000001
    _BFSR_IBUSERR_SHIFT      = 0

    _BFSR_BFARVALID_DESC     = "BFAR has valid contents"
    _BFSR_LSPERR_DESC        = "A bus fault occurred during FP lazy state preservation"
    _BFSR_STKERR_DESC        = "A derived bus fault has occurred on exception entry"
    _BFSR_UNSTKERR_DESC      = "A derived bus fault has occurred on exception return"
    _BFSR_IMPRECISERR_DESC   = "An imprecise data access error has occured"
    _BFSR_PRECISERR_DESC     = "A precise data access error has occurred, and the processor has written the faulting address to the BFAR (only valid if BFARVALID is set)"
    _BFSR_IBUSERR_DESC       = "A bus fault on an instruction prefetch has occurred. The fault is signlaed only if the instruction is issued"

    _bfsr_bitfields = {
        "BFARVALID": {
            "mask":         _BFSR_BFARVALID_MASK,
            "shift":        _BFSR_BFARVALID_SHIFT,
            "description":  _BFSR_BFARVALID_DESC
        },
        "LSPERR": {
            "mask":         _BFSR_LSPERR_MASK,
            "shift":        _BFSR_LSPERR_SHIFT,
            "description":  _BFSR_LSPERR_DESC
        },
        "STKERR": {
            "mask":         _BFSR_STKERR_MASK,
            "shift":        _BFSR_STKERR_SHIFT,
            "description":  _BFSR_STKERR_DESC
        },
        "UNSTKERR": {
            "mask":         _BFSR_UNSTKERR_MASK,
            "shift":        _BFSR_UNSTKERR_SHIFT,
            "description":  _BFSR_UNSTKERR_DESC
        },
        "IMPRECISERR": {
            "mask":         _BFSR_IMPRECISERR_MASK,
            "shift":        _BFSR_IMPRECISERR_SHIFT,
            "description":  _BFSR_IMPRECISERR_DESC
        },
        "PRECISERR": {
            "mask":         _BFSR_PRECISERR_MASK,
            "shift":        _BFSR_PRECISERR_SHIFT,
            "description":  _BFSR_PRECISERR_DESC
        },
        "IBUSERR": {
            "mask":         _BFSR_IBUSERR_MASK,
            "shift":        _BFSR_IBUSERR_SHIFT,
            "description":  _BFSR_IBUSERR_DESC
        }
    }


    def __init__(self, value = None):
        super().__init__(self._bfsr_bitfields)

        if value is not None:
            self.decode(value)

    def get_diagram(self) -> list:

        bfarvalid   = self.bitfields["BFARVALID"]["value"]
        lsperr      = self.bitfields["LSPERR"]["value"]
        stkerr      = self.bitfields["STKERR"]["value"]
        unstkerr    = self.bitfields["UNSTKERR"]["value"]
        impreciserr = self.bitfields["IMPRECISERR"]["value"]
        preciserr   = self.bitfields["PRECISERR"]["value"]
        ibuserr     = self.bitfields["IBUSERR"]["value"]

        bfsr_bitfield_template = f"""{bfarvalid}│ │{lsperr}│{stkerr}│{unstkerr}│{impreciserr}│{preciserr}│{ibuserr}"""

        bfsr_bitfield_str = f"""
         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │{bfsr_bitfield_template}│
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
BFARVALID─┘ │ │ │ │ │ │ └─IBUSERR
 reserved───┘ │ │ │ │ └───PRECISERR
   LSPERR─────┘ │ │ └─────IMPRECISERR
   STKERR───────┘ └───────UNSTKERR
"""    
        return bfsr_bitfield_str.split('\n')

class UFSR(Register):

    _UFSR_DIVBYZERO_MASK     = 0b0000001000000000
    _UFSR_DIVBYZERO_SHIFT    = 9
    _UFSR_UNALIGNED_MASK     = 0b0000000100000000
    _UFSR_UNALIGNED_SHIFT    = 8
    _UFSR_NOCP_MASK          = 0b0000000000001000
    _UFSR_NOCP_SHIFT         = 3
    _UFSR_INVPC_MASK         = 0b0000000000000100
    _UFSR_INVPC_SHIFT        = 2
    _UFSR_INVSTATE_MASK      = 0b0000000000000010
    _UFSR_INVSTATE_SHIFT     = 1
    _UFSR_UNDEFINSTR_MASK    = 0b0000000000000001
    _UFSR_UNDEFINSTR_SHIFT   = 0

    _UFSR_DIVBYZERO_DESC     = "Divide by zero error has occurred"
    _UFSR_UNALIGNED_DESC     = "Unaligned access error has occurred"
    _UFSR_NOCP_DESC          = "A coprocessor access error has occurred. This shows that the coprocessor is disabled or not present"
    _UFSR_INVPC_DESC         = "An integrity check error has occurred on EXC_RETURN"
    _UFSR_INVSTATE_DESC      = "Instruction executed with invalid EPSR.T or EPSR.IT field"
    _UFSR_UNDEFINSTR_DESC    = "The processor has attempted to execute an undefined instruction. This might be an undefined instruction associated with an enabled coprocessor"

    _ufsr_bitfields = {
        "DIVBYZERO": {
            "mask":         _UFSR_DIVBYZERO_MASK,
            "shift":        _UFSR_DIVBYZERO_SHIFT,
            "description":  _UFSR_DIVBYZERO_DESC
        },
        "UNALIGNED": {
            "mask":         _UFSR_UNALIGNED_MASK,
            "shift":        _UFSR_UNALIGNED_SHIFT,
            "description":  _UFSR_UNALIGNED_DESC
        },
        "NOCP": {
            "mask":         _UFSR_NOCP_MASK,
            "shift":        _UFSR_NOCP_SHIFT,
            "description":  _UFSR_NOCP_DESC
        },
        "INVPC": {
            "mask":         _UFSR_INVPC_MASK,
            "shift":        _UFSR_INVPC_SHIFT,
            "description":  _UFSR_INVPC_DESC
        },
        "INVSTATE": {
            "mask":         _UFSR_INVSTATE_MASK,
            "shift":        _UFSR_INVSTATE_SHIFT,
            "description":  _UFSR_INVSTATE_DESC
        },
        "UNDEFINSTR": {
            "mask":         _UFSR_UNDEFINSTR_MASK,
            "shift":        _UFSR_UNDEFINSTR_SHIFT,
            "description":  _UFSR_UNDEFINSTR_DESC
        }
    }    

    def __init__(self, value = None):
        super().__init__(self._ufsr_bitfields)

        if value is not None:
            self.decode(value)

    def get_diagram(self) -> list:

        divbyzero   = self.bitfields["DIVBYZERO"]["value"]
        unaligned   = self.bitfields["UNALIGNED"]["value"]
        nocp        = self.bitfields["NOCP"]["value"]
        invpc       = self.bitfields["INVPC"]["value"]
        invstate    = self.bitfields["INVSTATE"]["value"]
        undefinstr  = self.bitfields["UNDEFINSTR"]["value"]

        ufsr_bitfield_template = f"""  reserved  │{divbyzero}│{unaligned}│  res. │{nocp}│{invpc}│{invstate}│{undefinstr}"""

        ufsr_bitfield_str = f"""
│15      │ 10 9 8│7     4│3 2 1 0│
├────────┴───┬─┬─┼───────┼─┬─┬─┬─┤
│{ufsr_bitfield_template}│
└────────────┴▲┴▲┴───────┴▲┴▲┴▲┴▲┘
    DIVBYZERO─┘ │    NOCP─┘ │ │ │
    UNALIGNED───┘   INVPC───┘ │ │
                 INVSTATE─────┘ │
               UNDEFINSTR───────┘
"""
        return ufsr_bitfield_str.split('\n')

class MMFSR(Register):

    _MMFSR_MMARVALID_MASK    = 0b10000000
    _MMFSR_MMARVALID_SHIFT   = 7
    _MMFSR_MLSPERR_MASK      = 0b00100000
    _MMFSR_MLSPERR_SHIFT     = 5
    _MMFSR_MSTKERR_MASK      = 0b00010000
    _MMFSR_MSTKERR_SHIFT     = 4
    _MMFSR_MUNSTKERR_MASK    = 0b00001000
    _MMFSR_MUNSTKERR_SHIFT   = 3
    _MMFSR_DACCVIOL_MASK     = 0b00000010
    _MMFSR_DACCVIOL_SHIFT    = 1
    _MMFSR_IACCVIOL_MASK     = 0b00000001
    _MMFSR_IACCVIOL_SHIFT    = 0

    _MMFSR_MMARVALID_DESC    = "MMFAR has valid contents"
    _MMFSR_MLSPERR_DESC      = "A MemManage fault occurred during FP lazy state preservation"
    _MMFSR_MSTKERR_DESC      = "A derived MemManage fault has occurred on exception entry"
    _MMFSR_MUNSTKERR_DESC    = "A derived MemManage fault has occurred on exception return"
    _MMFSR_DACCVIOL_DESC     = "Data access violation. The MMFAR shows the data address that the load or store tried to access (only valid if MMARVALID is set)"
    _MMFSR_IACCVIOL_DESC     = "MPU or Execute Never (XN) default memory map access violation on an instruction fetch has occurred. The fault is signaled only if the instruction is issued"

    _mmfsr_bitfields = {
       "MMARVALID": {
            "mask":         _MMFSR_MMARVALID_MASK,
            "shift":        _MMFSR_MMARVALID_SHIFT,
            "description":  _MMFSR_MMARVALID_DESC
       },
        "MLSPERR": {
            "mask":         _MMFSR_MLSPERR_MASK,
            "shift":        _MMFSR_MLSPERR_SHIFT,
            "description":  _MMFSR_MLSPERR_DESC
        },
        "MSTKERR": {
            "mask":         _MMFSR_MSTKERR_MASK,
            "shift":        _MMFSR_MSTKERR_SHIFT,
            "description":  _MMFSR_MSTKERR_DESC
        },
        "MUNSTKERR": {
            "mask":         _MMFSR_MUNSTKERR_MASK,
            "shift":        _MMFSR_MUNSTKERR_SHIFT,
            "description":  _MMFSR_MUNSTKERR_DESC
        },
        "DACCVIOL": {
            "mask":         _MMFSR_DACCVIOL_MASK,
            "shift":        _MMFSR_DACCVIOL_SHIFT,
            "description":  _MMFSR_DACCVIOL_DESC
        },
        "IACCVIOL": {
            "mask":         _MMFSR_IACCVIOL_MASK,
            "shift":        _MMFSR_IACCVIOL_SHIFT,
            "description":  _MMFSR_IACCVIOL_DESC
        }
    }

    def __init__(self, value = None):
        super().__init__(self._mmfsr_bitfields)

        if value is not None:
            self.decode(value)
    
    def get_diagram(self) -> list:

        mmarvalid   = self.bitfields["MMARVALID"]["value"]
        mlsperr     = self.bitfields["MLSPERR"]["value"]
        mstkerr     = self.bitfields["MSTKERR"]["value"]
        munstkerr   = self.bitfields["MUNSTKERR"]["value"]
        daccviol    = self.bitfields["DACCVIOL"]["value"]
        iaccviol    = self.bitfields["IACCVIOL"]["value"]

        mmfsr_bitfield_template = f"""{mmarvalid}│ │{mlsperr}│{mstkerr}│{munstkerr}│ │{daccviol}│{iaccviol}"""

        mmfsr_bitfield_str = f"""
         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │{mmfsr_bitfield_template}│
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
MMARVALID─┘ │ │ │ │ │ │ └─IACCVIOL
 Reserved───┘ │ │ │ │ └───DACCVIOL
  MLSPERR─────┘ │ │ └─────Reserved
  MSTKERR───────┘ └───────MUNSTKERR
"""
        return mmfsr_bitfield_str.split('\n')

class CFSR():

    _CFSR_MMFSR_MASK     = 0x000000FF
    _CFSR_MMFSR_SHIFT    = 0
    _CFSR_BFSR_MASK      = 0x0000FF00
    _CFSR_BFSR_SHIFT     = 8
    _CFSR_UFSR_MASK      = 0xFFFF0000
    _CFSR_UFSR_SHIFT     = 16

    def __init__(self, value = None):

        if value is not None:
            self.decode(value)

    def decode(self, cfsr_value):
        self.bfsr   = BFSR((cfsr_value & self._CFSR_BFSR_MASK) >> self._CFSR_BFSR_SHIFT)
        self.ufsr   = UFSR((cfsr_value & self._CFSR_UFSR_MASK) >> self._CFSR_UFSR_SHIFT)
        self.mmfsr  = MMFSR((cfsr_value & self._CFSR_MMFSR_MASK) >> self._CFSR_MMFSR_SHIFT)

class HFSR(Register):

    _HFSR_DEBUGEVT_MASK      = 0x80000000
    _HFSR_DEBUGEVT_SHIFT     = 31
    _HFSR_FORCED_MASK        = 0x40000000
    _HFSR_FORCED_SHIFT       = 30
    _HFSR_VECTTBL_MASK       = 0x00000002
    _HFSR_VECTTBL_SHIFT      = 1

    _HFSR_DEBUGEVT_DESC      = "Reserved for Debug Use. When writing to the register you must write 1 to this bit, otherwise behaviour is unpredictable"
    _HFSR_FORCED_DESC        = "Indicates a forced HardFault, generated by escalation of a fault with configurable priority that cannot be handled, either because of priority or because it is disabled. When this bit is set to 1, the HardFault handler must read the other fault status registers to find the cause of the fault"
    _HFSR_VECTTBL_DESC       = "Indicates a HardFault on a vector table read during exception processing. This error is always handled by the HardFault handler. When this bit is set to 1, the PC value stacked for hte exception return points to the instruction that was pre-empted by the exception"

    _hfsr_bitfields = {
        "DEBUGEVT": {
            "mask":         _HFSR_DEBUGEVT_MASK,
            "shift":        _HFSR_DEBUGEVT_SHIFT,
            "description":  _HFSR_DEBUGEVT_DESC
        },
        "FORCED": {
            "mask":         _HFSR_FORCED_MASK,
            "shift":        _HFSR_FORCED_SHIFT,
            "description":  _HFSR_DEBUGEVT_DESC
        },
        "VECTTBL": {
            "mask":         _HFSR_VECTTBL_MASK,
            "shift":        _HFSR_VECTTBL_SHIFT,
            "description":  _HFSR_DEBUGEVT_DESC
        }
    }   

    def __init__(self, value = None):
        super().__init__(self._hfsr_bitfields)

        if value is not None:
            self.decode(value)

    def get_diagram(self) -> list:

        debugevt    = self.bitfields["DEBUGEVT"]["value"]
        forced      = self.bitfields["FORCED"]["value"]
        vecttbl     = self.bitfields["VECTTBL"]["value"]
        
        hfsr_bitfield_template = f"""{debugevt}│{forced}│          RESERVED          │{vecttbl}│ """

        hfsr_bitfield_str = f"""
│31 │29                          │1│0│
├─┬─┼────────────────────────────┼─┼─┤
│{hfsr_bitfield_template}│
└▲┴▲┴────────────────────────────┴▲┴▲┘
 │ └─FORCED               VECTTBL─┘ │
 └───DEBUGEVT            RESERVED───┘
"""
    
        return hfsr_bitfield_str.split('\n')

class SHCSR(Register):

    _SHCSR_USGFAULTENA_MASK      = 0x00040000
    _SHCSR_USGFAULTENA_SHIFT     = 18
    _SHCSR_BUSFAULTENA_MASK      = 0x00020000
    _SHCSR_BUSFAULTENA_SHIFT     = 17
    _SHCSR_MEMFAULTENA_MASK      = 0x00010000
    _SHCSR_MEMFAULTENA_SHIFT     = 16
    _SHCSR_SVCALLPENDED_MASK     = 0x00008000
    _SHCSR_SVCALLPENDED_SHIFT    = 15
    _SHCSR_BUSFAULTPENDED_MASK   = 0x00004000
    _SHCSR_BUSFAULTPENDED_SHIFT  = 14
    _SHCSR_MEMFAULTPENDED_MASK   = 0x00002000
    _SHCSR_MEMFAULTPENDED_SHIFT  = 13
    _SHCSR_USGFAULTPENDED_MASK   = 0x00001000
    _SHCSR_USGFAULTPENDED_SHIFT  = 12
    _SHCSR_SYSTICKACT_MASK       = 0x00000800
    _SHCSR_SYSTICKACT_SHIFT      = 11
    _SHCSR_PENDSVACT_MASK        = 0x00000400
    _SHCSR_PENDSVACT_SHIFT       = 10
    _SHCSR_MONITORACT_MASK       = 0x00000100
    _SHCSR_MONITORACT_SHIFT      = 8
    _SHCSR_SVCALLACT_MASK        = 0x00000080
    _SHCSR_SVCALLACT_SHIFT       = 7
    _SHCSR_USGFAULTACT_MASK      = 0x00000008
    _SHCSR_USGFAULTACT_SHIFT     = 3
    _SHCSR_BUSFAULTACT_MASK      = 0x00000002
    _SHCSR_BUSFAULTACT_SHIFT     = 1
    _SHCSR_MEMFAULTACT_MASK      = 0x00000001
    _SHCSR_MEMFAULTACT_SHIFT     = 0

    _SHCSR_USGFAULTENA_DESC      = "UsageFault enabled"
    _SHCSR_BUSFAULTENA_DESC      = "BusFault enabled"
    _SHCSR_MEMFAULTENA_DESC      = "MemManage fault enabled"
    _SHCSR_SVCALLPENDED_DESC     = "SVCall is pending"
    _SHCSR_BUSFAULTPENDED_DESC   = "BusFault is pending"
    _SHCSR_MEMFAULTPENDED_DESC   = "MemManage fault is pending"
    _SHCSR_USGFAULTPENDED_DESC   = "UsageFault is pending"
    _SHCSR_SYSTICKACT_DESC       = "SysTick is active"
    _SHCSR_PENDSVACT_DESC        = "PendSV is active"
    _SHCSR_MONITORACT_DESC       = "Monitor is active"
    _SHCSR_SVCALLACT_DESC        = "SVCall is active"
    _SHCSR_USGFAULTACT_DESC      = "UsageFault is active"
    _SHCSR_BUSFAULTACT_DESC      = "BusFault is active"
    _SHCSR_MEMFAULTACT_DESC      = "MemManage fault is active"

    _shcsr_bitfields = {
        "USGFAULTENA": {
            "mask":         _SHCSR_USGFAULTENA_MASK,
            "shift":        _SHCSR_USGFAULTENA_SHIFT,
            "description":  _SHCSR_USGFAULTENA_DESC
        },
        "BUSFAULTENA": {
            "mask":         _SHCSR_BUSFAULTENA_MASK,
            "shift":        _SHCSR_BUSFAULTENA_SHIFT,
            "description":  _SHCSR_BUSFAULTENA_DESC
        },
        "MEMFAULTENA": {
            "mask":         _SHCSR_MEMFAULTENA_MASK,
            "shift":        _SHCSR_MEMFAULTENA_SHIFT,
            "description":  _SHCSR_MEMFAULTENA_DESC
        },
        "SVCALLPENDED": {
            "mask":         _SHCSR_SVCALLPENDED_MASK,
            "shift":        _SHCSR_SVCALLPENDED_SHIFT,
            "description":  _SHCSR_SVCALLPENDED_DESC
        },
        "BUSFAULTPENDED": {
            "mask":         _SHCSR_BUSFAULTPENDED_MASK,
            "shift":        _SHCSR_BUSFAULTPENDED_SHIFT,
            "description":  _SHCSR_BUSFAULTPENDED_DESC
        },
        "MEMFAULTPENDED": {
            "mask":         _SHCSR_MEMFAULTPENDED_MASK,
            "shift":        _SHCSR_MEMFAULTPENDED_SHIFT,
            "description":  _SHCSR_MEMFAULTPENDED_DESC
        },
        "USGFAULTPENDED": {
            "mask":         _SHCSR_USGFAULTPENDED_MASK,
            "shift":        _SHCSR_USGFAULTPENDED_SHIFT,
            "description":  _SHCSR_USGFAULTPENDED_DESC
        },
        "SYSTICKACT": {
            "mask":         _SHCSR_SYSTICKACT_MASK,
            "shift":        _SHCSR_SYSTICKACT_SHIFT,
            "description":  _SHCSR_SYSTICKACT_DESC
        },
        "PENDSVACT": {
            "mask":         _SHCSR_PENDSVACT_MASK,
            "shift":        _SHCSR_PENDSVACT_SHIFT,
            "description":  _SHCSR_PENDSVACT_DESC
        },
        "MONITORACT": {
            "mask":         _SHCSR_MONITORACT_MASK,
            "shift":        _SHCSR_MONITORACT_SHIFT,
            "description":  _SHCSR_MONITORACT_DESC
        },
        "SVCALLACT": {
            "mask":         _SHCSR_SVCALLACT_MASK,
            "shift":        _SHCSR_SVCALLACT_SHIFT,
            "description":  _SHCSR_SVCALLACT_DESC
        },
        "USGFAULTACT": {
            "mask":         _SHCSR_USGFAULTACT_MASK,
            "shift":        _SHCSR_USGFAULTACT_SHIFT,
            "description":  _SHCSR_USGFAULTACT_DESC
        },
        "BUSFAULTACT": {
            "mask":         _SHCSR_BUSFAULTACT_MASK,
            "shift":        _SHCSR_BUSFAULTACT_SHIFT,
            "description":  _SHCSR_BUSFAULTACT_DESC
        },
        "MEMFAULTACT": {
            "mask":         _SHCSR_MEMFAULTACT_MASK,
            "shift":        _SHCSR_MEMFAULTACT_SHIFT,
            "description":  _SHCSR_MEMFAULTACT_DESC
        }
    }

    def __init__(self, value = None):
        super().__init__(self._shcsr_bitfields)

        if value is not None:
            self.decode(value)

    def get_diagram(self) -> list:

        usgfaultena     = self.bitfields["USGFAULTENA"]["value"]
        busfaultena     = self.bitfields["BUSFAULTENA"]["value"]
        memfaultena     = self.bitfields["MEMFAULTENA"]["value"]
        svcallpended    = self.bitfields["SVCALLPENDED"]["value"]
        busfaultpended  = self.bitfields["BUSFAULTPENDED"]["value"]
        memfaultpended  = self.bitfields["MEMFAULTPENDED"]["value"]
        usgfaultpended  = self.bitfields["USGFAULTPENDED"]["value"]
        systickact      = self.bitfields["SYSTICKACT"]["value"]
        pendsvact       = self.bitfields["PENDSVACT"]["value"]
        monitoract      = self.bitfields["MONITORACT"]["value"]
        svcallact       = self.bitfields["SVCALLACT"]["value"]
        usgfaultact     = self.bitfields["USGFAULTACT"]["value"]
        busfaultact     = self.bitfields["BUSFAULTACT"]["value"]
        memfaultact     = self.bitfields["MEMFAULTACT"]["value"]
        
        shcsr_bitfield_template = f"""        RESERVED         │{usgfaultena}│{busfaultena}│{memfaultena}│{svcallpended}│{busfaultpended}│{memfaultpended}│{usgfaultpended}│{systickact}│{pendsvact}│ │{monitoract}│{svcallact}│ RES │{usgfaultact}│ │{busfaultact}│{memfaultact}"""

        shcsr_bitfield_str = f"""
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
"""
        return shcsr_bitfield_str.split('\n')

def get_report(reg_name, value, size, diagram: list, table: list, header_char = "=", separator_char = "-", line_width = 80) -> str:

    report_str_list = list()

    # create header
    report_str_list.append(header_char * line_width)

    # print raw
    report_str_list.append(f"{reg_name}: 0x{value:0{size}X}")

    # create separator
    report_str_list.append(separator_char * line_width)

    # padding
    report_str_list.append("")

    # diagram
    report_str_list.extend(diagram)

    # padding
    report_str_list.append("")

    # separator
    report_str_list.append(separator_char * line_width)

    # padding
    report_str_list.append("")

    # table
    report_str_list.extend(table)

    # padding
    report_str_list.append("")

    # header
    report_str_list.append(header_char * line_width)

    return "\n".join(report_str_list)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Analyze Fault causes on arm M-33 devices")
    parser.add_argument('--cfsr', dest="cfsr", type=lambda x: int(x, 0), required=False, help="the CFSR value from the ARM device")
    parser.add_argument('--hfsr', dest="hfsr", type=lambda x: int(x, 0), required=False, help="the HFSR value from the ARM device")
    parser.add_argument('--shcsr', dest="shcsr", type=lambda x: int(x, 0), required=False, help="the SHCSR value from the ARM device")

    args = parser.parse_args()

    report = ""

    if args.cfsr is not None:
        cfsr = CFSR(args.cfsr)

        report += get_report("UFSR", cfsr.ufsr._raw, 2, cfsr.ufsr.get_diagram(), cfsr.ufsr.get_table()) + "\n"
        report += get_report("BFSR", cfsr.bfsr._raw, 2, cfsr.bfsr.get_diagram(), cfsr.bfsr.get_table()) + "\n"
        report += get_report("MMFSR", cfsr.mmfsr._raw, 2, cfsr.mmfsr.get_diagram(), cfsr.mmfsr.get_table()) + "\n"

    if args.hfsr is not None:
        hfsr = HFSR(args.hfsr)

        report += get_report("HFSR", hfsr._raw, 8, hfsr.get_diagram(), hfsr.get_table()) + "\n"

    if args.shcsr is not None:
        shcsr = SHCSR(args.shcsr)

        report += get_report("SHCSR", shcsr._raw, 8, shcsr.get_diagram(), shcsr.get_table()) + "\n"

    print(report)