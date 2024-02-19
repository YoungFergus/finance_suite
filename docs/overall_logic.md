Login to main menu on command line and you have options for what to do.

1. Add a new investment position
    - You need a ticker, a category, a % allocation for the category, and a trigger
    Dependent on: categories and trigger rules
2. Import transactions from Charles Schwab file
    - Dependent on DB existing
3. Set your portfolio allocation strategy
    - Create categories
    - Set an allocation % for the category
    - View your overall allocations
4. Create an investment add strategy - developed, not tested
    - Amount to invest per period
    - Frequency of investment (daily, weekly, bi-weekly, bi-monthly, monthly, quarterly, semi-annually)
    - When to start this add strategy
5. View statistics


Investment add strategy
configurations.json
{ "Add_Strategy: {
    "Strategy_Name": user_input,
    "Frequency":     user_select_from_list,
    "Start_Date":    user_input,
    "Period_Amount": user_input},
  
}