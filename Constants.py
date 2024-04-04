#Input path
kInputPath = "Data\\Input\\"

#Output path
kOutputPath =   "Data\\Output\\"

kTBHeader = ['Account', 'DR', 'CR']
kCollectionsMonthsLag = 1
kCollectionsMonthsLate = 2
kCollectionDaysBad = -1
kFirstDayofMonth = 1
kContractRenewing = "Recurring"

kSkipContract = -1
kFirst = 0
kStd_cat_columns = 40
kStd_num_columns = 14
kDR = "DR"
kCR = "CR"
kJELines = 2
kMonthsInYear = 12

kCategory = "Category"

kAccIndex = "AccountIndex"
kIS_string = "IS"
kBS_string = "BS"
kAssets = "Assets"
kDepts = "Department"
kLiabilities = "Liabilities"
kEquity = "Equity"
kRetainedEarnings = "Retained Earnings"
kFS_line = "FS_line"

kFS = "FS"
kBS = "BS"
kIS = "IS"

# Class/main module names - Projections.py
kClassExp =  "CExpenses"
kClassRev = "CRevenues"
kClassEmpl = "CEmployees"
kClassCont = "CContractors"
kClassCapEx =  "CCapExSW"
kClassTB = "CTBEntry"
#kClass = 



#Inputs filename
kInputs_file = "Inputs.xlsx"
#inputs tab
kInputs = "Inputs"
#Input parameters
kInStartDateIndex = 0
kInStartDate = "Start Date"
kInEndDateIndex = 1
kInEndDate = "End Date"
kInActualsDateIndex = 2
kInActualsDate = "Actuals Date"
kInActualsMonthIndex = 3
kInSimMonthsIndex = 4
kInTotalsMonthsIndex = 5
kInIncomeAcIndex = 6
kInCashAcIndex = 7
kInSSRateIndex = 8
kInSSCapIndex = 9
kInMedicareIndex = 10
kInSUIRateIndex = 11
kInSUICapIndex = 12
kInFUTARateIndex = 13
kInFUTACapIndex = 14
kInChurnIndex = 15
kInCapSWBalTermIndex = 16
kInCapSWAmortTermIndex = 17
kInNewClientDaysIndex = 18
kInClientCollectionDays = 19
kInNewContractLength = 20
kBaseCommissionRate = 21
kMonthsLookbackChurn = 22

#Accounts tab
kInternalAccount = "Internal Only-"
#Accounts layout
kTBAccountIndex = 0
kAccounts = "Accounts"
kAccNum = 1
kAccNumName = "Account #"
kFSAcc = 2
kFSAccName = "FS Account"
kBSorIS = 3
kBSorISName = "Statement"
kDept = 4
kDeptName = "Department"
kCombined = 5
kCombinedName = "Combined: FS Account and Dept"
kExternal = 6
kExternalName = "External"
kAccountFields = 7

# Products tab
kProducts = "Products"
#Products layout
kProductNameIndex = 0
kProductAccountIndex = 1
kProductPercent = "Percent"
kProductPercentIndex = 2

kRevExpAccounts = "RevExpAccounts"
#Revenue/Expenses Fields
kClass = "Class"
kClassIndex = 0
kListType = "List_Type"
kListTypeIndex = 1
kDRCR = "DR-CR"
kDRCRIndex = 2
kAccount = "Account"
kAccountIndex = 3
kAccountSheet ="Sheet"
kAccountSheetIndex = 4

#RevExp tab
kRevExpTypes = "RevExpTypes"
#RevExp fields
kRevExpType = "Class"
kRevExpLog = "Log"

#Commissions tab
kCommissionsTab = "RevCommissions"
kRevCommisionsIn = "RevCommissions"
kCommRevType = "Rev Type"
kCommRevTypeIndex = 0
kCommUse = "Use?"
kCommUseIndex = 1
kCommCommType = "Comm Type"
kCommCommTypeIndex = 2
kCommInitial = "Initial"
kCommInitialIndex = 3
kCommRenew = "Renew"
kCommRenewIndex = 4

kSW_cap_file = "SW_Cap.xlsx"

#capSW Table
kcapSWType	= "Type"
kcapSWTypeIndex	= 0
kcapSWCompType = "CompType"
kcapSWCompTypeIndex = 1
kcapSWSubType = "SubType"
kcapSWSubTypeIndex = 2
kcapSWTypeSW = "CapSW"
kcapSWCompTypeEmpl = "Employee"
kcapSWCompTypeCont = "Contractor"
kcapSWSubTypeExp = "Exp"
kcapSWCompDebit = "Debit"
kcapSWCompDebitIndex = 3
kcapSWCompCredit = "Credit"
kcapSWCompCreditIndex = 4

#CapEx SW Data from above table
kCapExType = "FA"
kCapSWType = "CapSW"
kCapExCapType = "Cap"
kCapSWExpType = "Exp"


kTB_file = "TBs_in.xlsx"
#Tab names are "YYYY-MM" from projectection start to last month actually closed
# Trial Balance (TB) layout
kTBAcIndex = 0
kDRIndex = 1
kCRIndex = 2

kExpensesXL = "Expenses.xlsx"
kExpenses="Expenses"
#Expenses layout
kExpensesDescription = 0
kExpensesType = 1
kExpensesStart = 2
kExpensesEnd = 3
kExpensesAmount = 4
kExpensesDept = 5
kExpensesAcDr = 6
kExpensesAcCr = 7

#Revenue Inputs Workbook
kRev_input_file = 'RevenueInputs.xlsx'
kExisting = "Existing"

# Existing Invoice Fields											
kExistingProduct = 'Product'
kExistingType = 'Type'
kExistingInvoiceDate = 'Invoice Date'
kExistingCollectionDate = 'Collection Date'
kExistingAmount = 'Amount'
kExistingRecognitionStart = 'Recognition Start'
kExistingRecognitionEnd = 'Recognition End'
kExistingClientID = "Client ID"
kExistingContractMonths = 'Contract Months'
kExistingMRR = 'Amount Recognized per Month'
kExistingCommission = 'Commission Percent'

kRenew = "Renew"
kContracts = "Contracts"

# Contracts Fields
kContractsStartDate = 'Start Date'
kContractsEndDate = 'End Date'
kContractsTotalContract = 'Total Contract Value'
kContractsMRR = 'MRR'
kContractsProduct = 'Product'
kContractsFrequency = 'Frequency'
kContractsType = 'Type'
kContractsAcctID = 'Client ID'
kContractsRenewalInfo = 'Renew Info'
kContractsCollectionDate = 'Collection Date'
kContractsInvoiceDate = 'Invoice Date'
kContractsCommission = 'Commission Percent'

kNew = "New"

# New Fields
kNewOffset = 'Offset'
kNewBookDate = 'Start Date'
kNewBookings = 'New'
kNewUpsellBookings = 'Upsell'
kNewTotals = 'Total'
kNewCommission = 'Commission Percent'


#Output Files
kExisting_file = "Existing.xlsx"
kRenew_file = "Renewals.xlsx"
kNew_file = "New.xlsx"
kFSOut = "FS.xlsx"
kTBOut = "TBs.xlsx"

kProducts_file = "_products.xlsx"

#Expense output files are not used
kExpensesOut = "ExpensesOut.csv"

#Tab names

#Collections output file
kCollections_file = "Collections.xlsx"

kCollectionsTab = "Collections"
kCollectionsDays = "Days"
kCollectionsWeight = "Weight"
kCollectionsWtdAvgDays = "Weighted Avg Days"
kCollectionsWtdAvgDaysClientIndex = 0
kCollectionsWtdAvgDaysIndex = 4
kCollectionsWtgAvgDays = "Wtd Avg Days"

#churn
kChurn_file = "Churn.xlsx"
kChurnInvoices = "Churn Invoices"
kChurnOutput = "Churn Outputs"
kChurnOccuranceSummary = "Churn Occurance Summary"
kChurnInvoiceSummary = "Churn Invoice Summary"
kChurnPercentages = "Churn Percentages"


kCommMRR = "MRR"
kCommCollection = "Collection"
kCommInvoice = "Invoice"

#Comp filename and tab names
kEmplFile = "Employees.xlsx"
kEmplPeople = 'Employees'
kEmplTypes = 'EmployeeTypes'
kEmplAccounts = 'EmployeeAccounts'

kContFile = "Contractors.xlsx"
kContPeople = 'Contractors'
kContTypes = 'ContractorsTypes'
kContAccounts = 'ContractorsAccounts'

#Contractors file has same exact structure as the Employees file
#Just the Individual info tabs are different\
#The 2nd & 3rd tabs for compnensation use the same constants structure and names

#Employee/Contractor table - column number
kCompNumIndex= 0
kCompDeptIndex= 1
kCompNameIndex= 2
kCompTitleIndex = 3
kCompBeginIndex = 4
kCompEndIndex = 5
kCompMonthlyIndex = 6
kCompYearlyIndex = 7
kCompSalariedIndex = 8
kCompBonusIndex = 9
kCompBonusIndex = 10
kCompBenefitsIndex = 11
kCompCapSWIndex = 12
kCompCapSWaccIndex = 13

#Types field list, these are the list of rountines used to calculate total compensation
#Comp types used - column numbers
kCompTypeIndex = 0
kCompTypeRowIndex = 1
kCompTypeCRColumnIndex = 2

#Accounts used for all the various type of expenses
#Comp expense accounts - column numbers											
kCompAccDeptIndex = 0
kCompAccCompIndex = 1
kCompAccBonusIndex = 2
kCompAccVacationIndex = 3
kCompAccFICAIndex = 4
kCompAccMedicareIndex = 5
kCompAccFUTAIndex = 6
kCompAccSUIIndex = 7
kCompAccHealthIndex = 8
kCompAccWCIndex = 9
kCompAccEmplSetupIndex = 10
kCompAccCapSWIndex = 11
kCompAccCapSWAmortIndex = 12

kCapAcFile = 'CapSwAccounts.xlsx'
kCapAc = "CapSwAccounts"
# Capitalized SW & Fixed Asset fields
kCapType = "Type"
kCapTypeIndex = 0
kCapAssetAC = "SubType"
kCapAssetACIndex = 1
kCapAssetAC = "Asset_ac"
kCapAssetACIndex = 2
kCapContraAC = "Contra_ac"
kCapContraACIndex = 3
kCapExpenseAC = "Expense_ac"
kCapExpenseACIndex = 4
kCapInitialTerm = "Initial term"
kCapInitialTermIndex = 5
kCapTerm = "Term"
kCapTermIndex = 6

kCapSWComp = "CapSWComp.xlsx"
kCapSWCont = "CapSWContractors.xlsx"
kcapSWAccts_file = "CapSwAccounts.xlsx"
kCapSWCompEmployees = "Employers"
kCapSWCompContractors = "Contractors"
kCapSWCompString = "_SW"
kCapSWTotals = "Totals"
kCapExSW = "CapSwAccounts.xlsx"
kCapSwAccounts = "CapSwAccounts"

#churn invoice list fields
kChurnClientIDindex = 0
kChurnProductIndex = 1
kChurnStart = 2
kChurnEnd = 3
kChurnMRR = 4

#Churn result fields
kProductChurnProduct = "Product"
kProductChurnProductIndex = 0
kProductChurnCount = "Overall Churn"
kProductChurnCountIndex = 1
kProductChurnPercent = "Churn Percent"
kProductChurnPercentIndex = 2

kContractInfoFrequency = 0
kContractInfoRenewalInfo = 1
kContractInfoFrequency= 2

#Revenue Worksheet names
kRevenue = "Revenue"
kInvoices = "Invoices"
kDeferred = "Deferred"
kAccrual = "Accrual"
kCollections = "Collections"
kCommissions = "Commissions"

# Revenues Dataframe Headers & Index - Outputs for Existing & Renewals that goes to init 
kRevLineNum = "Line #"
kRevLineNumIndex = 0
kRevClientId = "Client ID"
kRevClientIdIndex = 1
kRevProduct = "Product"
kRevProductIndex = 2
kRevInvoiceDate = "Invoice Date"
kRevInvoiceDateIndex = 3
kRevInvoiceAmt = "Invoice Amount"
kRevInvoiceAmtIndex = 4
kRevCollectDate = "Collection Date"
kRevCollectDateIndex = 5
kRevStartMRR = "MRR Start"
kRevStartMRRIndex = 6
kRevEndMRR = "MRR End"
kRevEndMRRIndex = 7
kRevMRRAmt = "MRR Amount"
kRevMRRAmtIndex = 8
kRevMRRTerm = "Term"
kRevMRRTermIndex = 9
kRevRenewNum = "Renewal Number"
kRevRenewNumIndex = 10
kRevCommission = "Commission Percent"
kRevCommissionIndex = 11
kRevCommissionType = "Commission Type"
kRevCommissionTypeIndex = 12
# number of fields above
kRevColumns = 13

#Contracts Info sent for processing
kFrequencyIndex = 0
kRenewalInfoIndex = 1
kContractsTypeIndex = 2

# Revenues Dataframe Headers & Index - Outputs for New
kNewLineNum = "Line #"
kNewLineNumIndex = 0
kNewClientID = "Not Used 1"
kNewClientIDIndex = 1
kNewProduct ="Product"
kNewProductIndex = 2
kNewInvoiceDate = "Invoice Date"
kNewInvoiceDateIndex = 3
kNewInvoiceAmt = "Invoice Amount"
kNewInvoiceAmtIndex = 4
kNewCollectDate = "Collection Date"
kNewCollectDateIndex = 5
kNewStartMRR = "MRR Start"
kNewStartMRRIndex = 6
kNewEndMRR = "MRR End"
kNewEndMRRIndex = 7
kNewMRRAmt = "MRR Amount"
kNewMRRAmtIndex = 8
kNewMRRTerm = "Term"
kNewMRRTermIndex = 9
kNewRenewNum = "Renewal Number"
kNewRenewNumIndex = 10
kNewCommission = "Commission Percent"
kNewCommissionIndex = 11
kNewCommissionType = "Commission Type"
kNewCommissionTypeIndex = 12
# number of fields above
kNewColumns = 13 # number of fields above

#CapExSW table
kCapExType = "Type"
kCapExTypeIndex = 0
kCapExCompType = "CompType"
kCapExCompTypeIndex = 1
kCapExSubType = "SubType"
kCapExSubTypeIndex = 2
kCapExDebit = "Debit"
kCapExDebitIndex = 3
kCapExCredit = "Credit"
kCapExCreditIndex = 4
kCapExAccumulated= "Accumulated"
kCapExAccumulatedIndex = 5
kCapExInitial = "Initial term"
kCapExInitialIndex = 6
kCapExTerm = "Term"
kCapExTermIndex = 7

kChurnOutClientID = "Client ID"
kChurnOutProduct = "Product"
kChurnOutStart = "Start"
kChurnOutEnd = "End"
kChurnOutMidPoint = "Mid Point"
kChurnOutMidPointIndex = 4
kChurnOutMRR = "MRR"
kChurnOutCommission = "Commission %"
kChurnOutInvoicesEnd = "Begin | End"
kChurnOutSameInvoice = "Next Invoice Same" 
kChurnOutEndInvoice = "End Invoice"
kChurnOutEndInvoiceChurn = "End Invoice Churn"
kChurnOutProductChurn = "Mid Invoice Churn"
kChurnOutInvoiceCount = "Invoice Count"
kChurnOutOverallChurn = "Overall Churn"
kChurnOutChurnPercent = "Churn Percent"

#Transaction Log
kTransFile = "Transaction Log.xlsx"
#Tabs are the class + sub class ("Empl/Cont", if it needs/exists)
kTransMonth = "Month"
kTransDrAcct = "DR Acct"
kTransCRAcct = "CR Acct"
kTransAmount ="Amount"

