from colorama import init,deinit,Fore



init()

def netSales():
    print(Fore.YELLOW,'''
        Net sales show the revenue your company makes after deductions such as discounts, returns, 
        and allowances are subtracted from your total profits. They are different from gross sales, which represent total sales 
        before any deductions during a certain period. Finding net sales will help you create an income statement, a valuable 
        planning tool for anticipating your income and expenses.

        Formula [Gross Sales – Deductions = Net Sales]

        Ref: https://www.patriotsoftware.com/accounting/training/blog/net-sales-explained/
    ''')


def otherIncome():
    print(Fore.YELLOW,'''
        Income from interest that deposit in the bank.
        Income from selling non-current assets.
        Revaluation gain on fixed assets.
        Interest charged from customers.
        Gain on exchange rate.
        Penalty from employee, customers and suppliers.

        Other income that generally recorded in the income statement is the aggregation of this small income together. 
        And generally, it should not exceed 10% of total income.
    ''')

def totalRevenues():
    print(Fore.YELLOW,'''
        Total Revenues:
            Formula [Total Revenue = Net Sales + Other Income]
    ''')

def grossProfit():
    print(Fore.YELLOW,'''
        Gross profit is the profit a company makes after deducting the costs associated with making and selling its products,
        or the costs associated with providing its services. 
        Gross profit will appear on a company's income statement and can be calculated by subtracting the cost of goods sold (COGS)
        from revenue (sales). 

        Formula [Revenue/Total - Cost of goods sold]

        Notes:
        1. Also called gross income, gross profit is calculated by subtracting the cost of goods sold from revenue.
        2. Gross profit only includes variable costs and does not account for fixed costs.
        3. Gross profit assesses a company's efficiency at using its labor and supplies in producing goods or services.

    ''')

def depreciation():
    print(Fore.YELLOW,'''
        Depreciation is the systematic allocation of an asset's cost to expense over the useful life of the asset.

        Example of Depreciation
        Let's assume that a retailer purchased displays for its store at a cost of $120,000. The displays have a useful life of 10 years
         and will have no salvage value. The straight-line method of depreciation will result in depreciation of $1,000 per 
         month ($120,000 divided by 120 months). The monthly journal entry to record the depreciation will be a debit of $1,000 to 
         the income statement account Depreciation Expense and a credit of $1,000 to the balance sheet contra asset account 
         Accumulated Depreciation.

        Depreciation on the Income Statement
        The depreciation reported on the income statement is the amount of depreciation expense that is appropriate for 
        the period of time indicated in the heading of the income statement.

        Using our example, the monthly income statements will report $1,000 of depreciation expense. The quarterly income statements 
        will report $3,000 of depreciation expense, and the annual income statements will report $12,000 of depreciation expense. 
        Each month $1,000 of depreciation expense is being matched to the 120 monthly income statements during which the displays 
        are used to generate sales revenues.
    ''')

def interest():
    print(Fore.YELLOW,'''
        An interest expense is the cost incurred by an entity for borrowed funds. 
        Interest expense is a non-operating expense shown on the income statement. 
        It represents interest payable on any borrowings – bonds, loans, convertible debt or lines of credit. 
        It is essentially calculated as the interest rate times the outstanding principal amount of the debt.
        Interest expense on the income statement represents interest accrued during the period covered by the financial statements,
        and not the amount of interest paid over that period. While interest expense is tax-deductible for companies, in an 
        individual's case, it depends on his or her jurisdiction and also on the loan's purpose.


        Thus, for allowance of a claim for deduction of interest under this provision following three conditions are there:

        (i) The money, that is capital, must have been borrowed by the assessee

        (ii) It must have been borrowed for the purpose of business.

        (iii) The assessee must have paid interest on the borrowed amount i.e. he has shown the same as an item of expenditure.
    
    ''')

    def profitBeforeTax():
        print(Fore.YELLOW,'''
            Profit before tax (PBT) is a measure that looks at a company's profits before the company has to pay corporate income tax. 
            It deducts all expenses from revenue including interest expenses and operating expenses except for income tax.
        ''')

    def grossProfitMargin():
        print(Fore.YELLOW,'''
            Gross profit margin is a metric used to assess a company's financial health and business model by
            revealing the amount of money left over from sales after deducting the cost of goods sold. 
            The gross profit margin is often expressed as a percentage of sales and may be called the gross margin ratio.
            Formula [Gross Profit Margin = (Net Sales − COGS)/Netsales]
        ''')