# ARM Cortex-M33 Fault Analyzer

A simple utility that takes a user provided coredump and lists potential areas of investigation for debugging faults on a Cortex-M33 based embedded systems device

*really i think this is any arm m profile v7 arch. system*

## How to Use

```
usage: system_control_registers.py [-h] CFSR

positional arguments:
  CFSR        the CFSR value from the ARM device
```

example:
```
> python system_control_registers.py 0xEF205AB5
```

## Background

- [Configurable Fault Status Register (CFSR)](#configurable-fault-status-register-cfsr)
    - [UsageFault Status Register (UFSR)](#usagefault-status-register-ufsr)
    - [BusFault Status Register (BFSR)](#busfault-status-register-bfsr)
    - [MemManage Status Register (MMFSR)](#memmanage-fault-status-register-mmfsr)
- [BusFault Address Register (BFAR)](#busfault-address-register-bfar)
- [MemManage Fault Address Register (MMFAR)](#memmanage-fault-address-register-mmfar)
- [Hardfault Status Register (HFSR)](#hardfault-status-register-hfsr)
- [System Handler Control and State Register (SHCSR)](#system-handler-control-and-state-register-shcsr)
- Core Registers

### Configurable Fault Status Register (CFSR)

The CFSR is states the cause of a UsageFault, BusFault, or MemManage Fault.

Cortex-M33 location: `0xE000ED28`

The CFSR bit fields:
```
│32              │16      │8       │0
├────────────────┼────────┼────────┤
│      UFSR      │  BFSR  │  MMFSR │
└────────────────┴────────┴────────┘
▲                                  ▲
└Configurable Fault Status Register┘
```

#### UsageFault Status Register (UFSR)

The UFSR is a subregister of CFSR. It indicates the cause of a UsageFault.

Cortex-M33 location: `0xE000ED2A` (halfword access)

The UFSR bit fields:
```
│15      │ 10 9 8│7     4│3 2 1 0│
├────────┴───┬─┬─┼───────┼─┬─┬─┬─┤
│  reserved  │ │ │  res. │ │ │ │ │
└────────────┴▲┴▲┴───────┴▲┴▲┴▲┴▲┘
    DIVBYZERO─┘ │    NOCP─┘ │ │ │
    UNALIGNED───┘   INVPC───┘ │ │
                 INVSTATE─────┘ │
               UNDEFINSTR───────┘
```

|                   |           |   |
|---                |---        |---|
| Bits[15:10]       | Reserved  | |
| DIVBYZERO, bit[9] | 0         | No divide by zero error has occured       |
|                   | 1         | Divide by zero error has occurred[^1]     |
| UNALIGNED, bit[8] | 0         | No unaligned access error has occurred    |
|                   | 1         | Unaligned access error has occurred[^2]   |
| Bits[7:4]         | Reserved  | |
| NOCP, bit[3]      | 0         | No coprocessor access error has occurred  |
|                   | 1         | A coprocessor access error has occurred. This shows that the coprocessor is disabled or not present |
| INVPC, bit[2]     | 0         | No integrity check error has occurred     |
|                   | 1         | An integrity check error has occurred on EXC_RETURN |
| INVSTATE, bit[1]  | 0         | EPSR.T bit and EPSR.IT bits are valid for instruction execution |
|                   | 1         | Instruction executed with invalid EPSR.T or EPSR.IT field |
| UNDEFINSTR, bit[0]| 0         | No undefined instruction usage fault has occured |
|                   | 1         | The processor has attempted to execute an undefined instruction. This might be an undefined instruction associated with an enabled coprocessor |

[^1]: When SDIV or UDIV instruction is used with a divisor of 0, this failt occurs if DIV_0_TRP is enabled in the CCR.
[^2]: Multi-word accesses always fault if not word aligned. Software can configure unaligned word and halfword accesses to fault, by enabling UNALIGN_TRP in the CCR.

#### BusFault Status Register (BFSR)

Shows the status of bus errors resulting from instruction prefetches and data accesses.

Cortex-M33 location: `0xE000ED29` (byte access)

The BFSR bit fields:
```
         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │ │ │ │ │ │ │ │ │
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
BFARVALID─┘ │ │ │ │ │ │ └─IBUSERR
 reserved───┘ │ │ │ │ └───PRECISERR
   LSPERR─────┘ │ │ └─────IMPRECISERR
   STKERR───────┘ └───────UNSTKERR
```

|                     |           |   |
|---                  |---        |---|
| BFARVALID, bit[7]   | 0         | BFAR does not have valid contents |
|                     | 1         | BFAR has valid contents |
| Bit[6]              | reserved  |   |
| LSPERR, bit[5]      | 0         | no bus fault occurred during FP lazy state preservation |
|                     | 1         | A bus fault occurred during FP lazy state preservation |
| STKERR, bit[4]      | 0         | No derived bus fault has occurred |
|                     | 1         | A derived bus fault has occurred on exception entry  |
| UNSTKERR, bit[3]    | 0         | No derived bus fault has occurred on exception return  |
|                     | 1         | A derived bus fault has occurred on exception return |
| IMPRECISERR, bit[2] | 0         | No imprecise data access error has occured |
|                     | 1         | Imprecise data access error has occured |
| PRECISERR, bit[1]   | 0         | No precise data access error has occurred |
|                     | 1         | A precise data access error has occurred, and the processor has written the faulting address ot the BFAR |
| IBUSERR, bit[0]     | 0         | No bus fault on an instruction prefetch has occurred |
|                     | 1         | A bus fault on an instruction prefetch has occurred. The fault is signlaed only if the instruction is issued |

#### MemManage Fault Status Register (MMFSR)

Shows the status of MPU faults.

Cortex-M33 location: `0xE000ED28` (byte access)

The MMFSR bit fields:
```
         │7 6 5 4│3 2 1 0│
         ├─┬─┬─┬─┼─┬─┬─┬─┤
         │ │ │ │ │ │ │ │ │
         └▲┴▲┴▲┴▲┴▲┴▲┴▲┴▲┘
MMARVALID─┘ │ │ │ │ │ │ └─IACCVIOL
 Reserved───┘ │ │ │ │ └───DACCVIOL
  MLSPERR─────┘ │ │ └─────Reserved
  MSTKERR───────┘ └───────MUNSTKERR
```

|                     |           |   |
|---                  |---        |---|
| MMARVALID, bit[7]   | 0         | MMFAR does not have valid contents |
|                     | 1         | MMFAR has valid contents |
| Bit[6]              | reserved  |   |
| MLSPERR, bit[5]     | 0         | no MemManage fault occurred during FP lazy state preservation |
|                     | 1         | A MemManage fault occurred during FP lazy state preservation |
| MSTKERR, bit[4]     | 0         | No derived MemManage fault has occurred |
|                     | 1         | A derived MemManage fault has occurred on exception entry  |
| MUNSTKERR, bit[3]   | 0         | No derived MemManage fault has occurred on exception return  |
|                     | 1         | A derived MemManage fault has occurred on exception return |
| Bit[2]              | reserved  |  |
| DACCVIOL, bit[1]    | 0         | No data access violation has occurred |
|                     | 1         | Data access violation. The MMFAR shows the data address that the load or store tried to access |
| IACCVIOL, bit[0]    | 0         | No MPU or Execute Never (XN) default memory map access violation has occurred |
|                     | 1         | MPU or Execute Never (XN) default memory map access violation on an instruction fetch has occurred. The fault is signaled only if the instruction is issued |

### BusFault Address Register (BFAR)

The BFAR contains the address of the location that generated a BusFault.
When an unaligned access faults the address in the BFAR is the one requested by the instruction, even if it is not the address of the fault.
*Flags in BFSR indicate the cause of the fault, and whether the value in the BFAR is valid.*

Cortex-M33 location: `0xE000ED38` (word access)

The BFAR bit fields:
```
│32                              │0
├────────────────────────────────┤
│            ADDRESS             │
└────────────────────────────────┘
▲                                ▲
└───BusFault Address Register────┘
```

|                     |           |   |
|---                  |---        |---|
| ADDRESS, Bits[31:0] |           | When the BFARVALID bit of the BFSR is set to 1, this field holds the address of the location that generated the BusFault |

### MemManage Fault Address Register (MMFAR)

The MMFAR contains the address of hte location that generated a MemManage fault.
When an unaligned access faults, the address is the actual address that faulted. Because a single read or write instruction can be split in to multiple aligned accesses, the fault address can be any address in the range of the requested access size.
*Flags in the MMFAR indicate the cause of the fault, and whether the value in the MMFAR is valid.*

Cortex-M33 location: `0xE000ED34` (word access)

The MMFAR bit fields:
```
│32                              │0
├────────────────────────────────┤
│            ADDRESS             │
└────────────────────────────────┘
▲                                ▲
└MemManage Fault Address Register┘
```

|                     |           |   |
|---                  |---        |---|
| ADDRESS, Bits[31:0] |           | When the MMARVALID bit of the MMFSR is set to 1, this field holds the address of the location that generated the MemManage Fault |

### HardFault Status Register (HFSR)

The HFSR gives information about events that activate the HardFault handler. The HFSR register is read, write to clear. This means that bits in the register read normally, but writing 1 to any bit clears that bit to 0.

Cortex-M33 location: `0xE000ED2C` (word access)

The HFSR bit fields:
```
│31 │29                          │1│0│
├─┬─┼────────────────────────────┼─┼─┤
│ │ │          RESERVED          │ │ │
└▲┴▲┴────────────────────────────┴▲┴▲┘
 │ └─FORCED               VECTTBL─┘ │
 └───DEBUGEVT            RESERVED───┘
```

|                     |           |   |
|---                  |---        |---|
| DEBUGEVT, Bit[31]   |           | Reserved for Debug Use. When writing to the register you must write 1 to this bit, otherwise behaviour is unpredictable |
| FORCED, Bit[30]     | 0         | No Forced HardFault |
|                     | 1         | Forced HardFault[^3]    |
| Bits[29:2]          | Reserved  |   |
| VECTTBL, Bit[1]     | 0         | No HardFault on vector table read |
|                     | 1         | HardFault on vector table read[^4] |
| Bit[0]              | Reserved  |   |

[^3]: Indicates a forced HardFault, generated by escalation of a fault with configurable priority that cannot be handled, either because of priority or because it is disabled. When this bit is set to 1, the HardFault handler must read the other fault status registers to find the cause of the fault.

[^4]: Indicates a HardFault on a vector table read during exception processing. This error is always handled by the HardFault handler. When this bit is set to 1, the PC value stacked for hte exception return points to the instruction that was pre-empted by the exception.

### System Handler Control and State Register (SHCSR)

The SHCSR enables the system handlers. It indicates the pending status of the BusFault, MemManage fault, and SVC exceptions, and indicates the active status of the system handlers.

Cortex-M33 location: `0xE000ED24` (word access)

The SHCSR bit field:
```
                         1 1 1 1 1 1 1 1 1 1
│31                     │9 8 7 6│5 4 3 2│1 0 9 8│7 6   4│3 2 1 0│
├───────────────────────┴─┬─┬─┬─┼─┬─┬─┬─┼─┬─┬─┬─┼─┬─────┼─┬─┬─┬─┤
│        RESERVED         │ │ │ │ │ │ │ │ │ │ │ │ │ RES │ │ │ │ │
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
```
|                           |           |   |
|---                        |---        |---|
| Bits[31:19]               | Reserved  |   |
| USGFAULTENA, Bit[18]      | 0         | Disable UsageFault |
|                           | 1         | Enable UsageFault  |
| BUSFAULTENA, Bit[17]      | 0         | Disable BusFault |
|                           | 1         | Enable BusFault  |
| MEMFAULTENA, Bit[16]      | 0         | Disable MemManageFault |
|                           | 1         | Enable MemManageFault  |
| SVCALLPENDED, Bit[15]     | 0         | SVCall is not pending |
|                           | 1         | SVCall is pending  |
| BUSFAULTPENDED, Bit[14]   | 0         | BusFault is not pending |
|                           | 1         | BusFault is pending  |
| MEMFAULTPENDED, Bit[13]   | 0         | MemManage fault is not pending |
|                           | 1         | MemManage fault is pending  |
| USGFAULTPENDED, Bit[12]   | 0         | UsageFault is not pending |
|                           | 1         | UsageFault is pending  |
| SYSTICKACT, Bit[11]       | 0         | SysTick is not active  |
|                           | 1         | SysTick is active      |
| PENDSVACT, Bit[10]        | 0         | PendSV is not active  |
|                           | 1         | PendSV is active      |
| Bit[9]                    | Reserved  |   |
| MONITORACT, Bit[8]        | 0         | Monitor is not active  |
|                           | 1         | Monitor is active      |
| SVCALLACT, Bit[7]         | 0         | SVCall is not active  |
|                           | 1         | SVCall is active      |
| Bits[6:4]                 | Reserved  |   |
| USGFAULTACT, Bit[3]       | 0         | UsageFault is not active  |
|                           | 1         | UsageFault is active      |
| Bit[2]                    | Reserved  |   |
| BUSFAULTACT, Bit[1]       | 0         | BusFault is not active  |
|                           | 1         | BusFault is active      |
| MEMFAULTACT, Bit[0]       | 0         | MemManage fault is not active  |
|                           | 1         | MemManage fault is active      |

> Pending state bits[15:12] are set to 1 when an exception occurs, and are cleared to 0 when the exception becomes active.
> Active state bits[11:10, 8:7, 3, 1:0] are set to 1 if the associated exception is the current exception or an exception that is nested because of preemption.

