from table_printer import Table_Printer as tp

class Register:

    header_char     = '='
    separator_char  = '-'

    def __init__(self, bitfield_dict: dict):

        self.bitfields  = bitfield_dict
        self._raw       = None
        
    def decode(self, reg_val: int):
        """parses register value into bitfields"""
        
        # store register value
        self._raw = reg_val
        
        # parse value into bitfields
        for bitfield in self.bitfields.keys():
            self.bitfields[bitfield]["value"] = (reg_val & self.bitfields[bitfield]["mask"]) >> self.bitfields[bitfield]["shift"]

    def get_table(self, line_width = 80) -> list:
        """generates ascii table of bitfield descriptions"""

        # make list of bitfields that are set and their descriptions
        set_bits = [(bitfield, self.bitfields[bitfield]["description"]) for bitfield in self.bitfields.keys() if self.bitfields[bitfield]["value"]]

        # check for empty list
        if len(set_bits) == 0:
            return []

        (registers, descriptions) = zip(*set_bits)

        table = tp(registers, descriptions)

        return table.list()

    def get_diagram(self) -> list:
        """generates ascii diagram representation of register as list of strings"""

        raise NotImplemented

    
