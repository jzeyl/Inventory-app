# Inventory-app

This is a simple database app. I created one before knowing much about SQL so it's implemented in Python and updates the v

# 1 - no SQL used
The main functionality is to update the main inventory spreadsheet using another spreadsheet 'Estimates' which indicates the products used at each sale. The CSV files of the inventory and . With a couple commands it will prompt the user to load the latest inventory and estimate spreadsheets to be updated.  An 'add record' command which prompts for user input of the estimate ID, product numbers, and quantities. Another command lets me check the records that will be modified in the main inventory sheet, and their values before and after updating. If the product number is mistyped there is an output warning. It also adds a couple columns with the date and time that the inventory is being updated.
A couple commands will let the user quickly save the updated inventory spreadsheet, estimates record, and plots in a folder with date (date of entry) automatically included.

Functions
|  Function name | Description   |   |   |   |
|---|---|---|---|---|
|  import_inventory() | Prompts opening of file viewer to select inventory spreadsheet  |   |   |   |
|  import_estimates() | Prompts opening of file viewer to select estimates spreadsheet   |   |   |   |
|  add_record | Prompts the user to input new 'estimate' record  |   |   |   |
|  clear_record() | Removes the added record  |   |   |   |
|  view_record() | Prints the added record as a dataframe  |   |   |   |
|  view_products_to_update() | Prints the rows that will be updated in the 'inventory' spreadsheet based on the added record  |   |   |   |
|  update_inventory() | Creates a new 'inventory' dataframe with updated values  |   |   |   |
|  view_modified_products() | View the cells that were modified  |   |   |   |
|  save_inventory() | Save updated 'inventory' spreadsheet with a datestamp  |   |   |   |
|  save_estimates() | Save updated 'estimates' spreadsheet with a datestamp  |   |   |   |
|  saveplot() |  Save bar plots of inventory, grouped by product category with a datestamp |   |   |   |


# 2 SQL commands
The other option is a few codes of SQL and a software
