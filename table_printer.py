styles = {
    "plain": {
        "padding":                  1,
        "vertical":                 '│',
        "horizontal":               '─',
        "junction":                 '┼',
        "top_junction":             '┬',
        "bottom_junction":          '┴',
        "right_junction":           '┤',
        "left_junction":            '├',
        "top_right_junction":       '┐',
        "top_left_junction":        '┌',
        "bottom_right_junction":    '┘',
        "bottom_left_junction":     '└'
    }
}

class Table_Printer:

    line_width = 80

    def __init__(self, col1, col2, style = "plain"):

        self.col1   = col1
        self.col2   = col2
        self.style  = style
        self._table = None

        self._generate()

    def list(self):
        return self._table

    def _generate(self):

        tbl_str_list = []

        # calculate column 0 width. characters only (not including padding)
        col0_width = 0
        
        for entry in self.col1:
            if len(entry) > col0_width:
                col0_width = len(entry)

        # calculate column 1 width. characters only (not including padding)
        col1_width = self.line_width - col0_width - (3 + (4 * styles[self.style]["padding"]))

        # store column widths
        self.col_widths = (col0_width, col1_width)

        # generate top border
        tbl_str_list.append(self._create_top_border())

        # generate entries
        for (register, description) in zip(self.col1, self.col2):
            tbl_str_list.extend(self._create_entry_row(register, description))
            tbl_str_list.append(self._create_row_separator())

        #replace last element since it should be bottom border instead
        tbl_str_list[-1] = self._create_bottom_border()

        self._table = tbl_str_list

    def _create_top_border(self):

        cw = self.col_widths
        row_str = ""

        row_str += styles[self.style]["top_left_junction"]
        row_str += styles[self.style]["horizontal"] * (cw[0] + styles[self.style]["padding"] + styles[self.style]["padding"])
        row_str += styles[self.style]["top_junction"]
        row_str += styles[self.style]["horizontal"] * (cw[1] + styles[self.style]["padding"] + styles[self.style]["padding"])
        row_str += styles[self.style]["top_right_junction"]

        return row_str

    def _create_bottom_border(self):

        cw = self.col_widths
        row_str = ""

        row_str += styles[self.style]["bottom_left_junction"]
        row_str += styles[self.style]["horizontal"] * (cw[0] + styles[self.style]["padding"] + styles[self.style]["padding"])
        row_str += styles[self.style]["bottom_junction"]
        row_str += styles[self.style]["horizontal"] * (cw[1] + styles[self.style]["padding"] + styles[self.style]["padding"])
        row_str += styles[self.style]["bottom_right_junction"]

        return row_str 

    def _create_row_separator(self):

        cw = self.col_widths
        row_str = ""

        row_str += styles[self.style]["left_junction"]
        row_str += styles[self.style]["horizontal"] * (cw[0] + styles[self.style]["padding"] + styles[self.style]["padding"])
        row_str += styles[self.style]["junction"]
        row_str += styles[self.style]["horizontal"] * (cw[1] + styles[self.style]["padding"] + styles[self.style]["padding"])
        row_str += styles[self.style]["right_junction"]
        
        return row_str

    def _create_entry_row(self, register, description):

        cw = self.col_widths
        row_str_list = list()

        # split description into list of words
        desc_words = description.split()

        # calculate if it will require more than one "row" to fit description
        desc_entry_rows = list()
        str_entry = ""

        for word in desc_words:
            
            # new line needed wont fit on this line
            if (len(str_entry) + len(word)) > cw[1]:
                str_entry = str_entry[:-1]
                desc_entry_rows.append(str_entry)
                str_entry = ""
            
            str_entry += word + " "

        # add str_entry if not empty
        if str_entry:
            str_entry = str_entry[:-1]
            desc_entry_rows.append(str_entry)

        # iterate through list and create rows
        first_line = True
        for str_entry in desc_entry_rows:

            row_str = ""

            row_str += styles[self.style]["vertical"]

            # fill register box if first line, else empty space
            if first_line:
                first_line = False

                row_str += " " * styles[self.style]["padding"]
                row_str += register
                row_str += " " * (cw[0] - len(register))
                row_str += " " * styles[self.style]["padding"]
            else:
                row_str += " " * (styles[self.style]["padding"] + cw[0] + styles[self.style]["padding"])

            row_str += styles[self.style]["vertical"]
            row_str += " " * styles[self.style]["padding"]
            row_str += str_entry
            row_str += " " * (cw[1] - len(str_entry))
            row_str += " " * styles[self.style]["padding"]
            row_str += styles[self.style]["vertical"]

            row_str_list.append(row_str)

        return row_str_list
