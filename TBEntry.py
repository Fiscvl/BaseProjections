from datetime import *
from dateutil.relativedelta import *

import pandas as pd
from BaseProjections.Constants import *

class CTBEntry():
    
#Not used yet - to be implemented as needed    
    def __init__(self, inputs, journal_entry, formats, rev_expense_log):
        self.journal_entry = journal_entry
        self.rev_explog = rev_expense_log
        self.transaction_log = []

        print("TB Entry log flag: ", self.rev_explog)


    def CTBEntryAddMonthsTransactions(self, month, TB):
        return TB


