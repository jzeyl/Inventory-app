# Inventory-app

This repository is an excercise in CRUD operations applied both with and without using a relational database. 

The objective was to create a simple inventory tracking database. There are two tables: 'inventory' and 'estimates'. The main functionality of this program to update a product inventory table with another table, 'estimates', which specifies sales and specific the products which will update the inventory.  

The estmate has the following fields:

Estimate num,Product num,Quantity,Date entered,Time entered

The first app is implemented in Python only, and creates a new updated spreadsheet each time entries are logged. The other version achieves the same result with a few short SQL scripts and viewing in a software (I used [DB Browser for SQLITE](https://sqlitebrowser.org/dl/)).

# 1 - Python with flat files (no SQL database)

The inventory and estimate csv spreadsheets are first loaded with 'import_inventory' and 'import_estimates'.  



An 'add record' command prompts for user input of the estimate ID, product numbers, and quantities. 

Other commands let me check the records that will be updated in the main inventory sheet, and their values before and after updating. If the new record product number is mistyped relative to the inventory spreadsheet, there is an output warning. The code also adds a couple columns with the date and time that the inventory is being updated. A couple commands will let the user quickly save the updated inventory spreadsheet, estimates record, and plots in a folder with date (date of entry) automatically included.

Functions
|Type|  Function name | Description   | 
|---|---|---|
|Data Import|  import_inventory() | Prompts opening of file viewer to select inventory spreadsheet. Table is saved as 'inventory' object.  | 
||  import_estimates() | Prompts opening of file viewer to select estimates spreadsheet. Table is saved as 'estimates' object.   || 
|Editing records|  add_record | Prompts the user to input new 'estimate' record  |  
||  clear_record() | Removes the added record  ||   
||  view_record() | Prints the added record as a dataframe  |   
||  view_products_to_update() | Prints the rows that will be updated in the 'inventory' spreadsheet based on the added record  |   
||  update_inventory() | Creates a new 'inventory' dataframe with updated values  |   
||  view_modified_products() | View the cells that were modified  |   
|Saving|  save_inventory() | Save updated 'inventory' spreadsheet with a datestamp  |  
||  save_estimates() | Save updated 'estimates' spreadsheet with a datestamp  |   
||  saveplot() |  Save bar plots of inventory, grouped by product category with a datestamp |  


# 2 - SQL commands
The other option is a few codes of SQL and a software. New values are added by modifying a table in DB Brower GUI and including the text 'add' in the corresponding cells in an adjacent column to indicate which new records to add.
| Files | Function |
|----|----|
|Update inventory.sql| Updates the 'inventory' spreadsheet based on the new records added to the 'estimates' spreadsheet|
|view all matching product numbers.sql| A query to view the products that are found in both 'inventory' and 'estimates' spreadsheets|
|view changed cells.sql| A query to view the updated cells in the 'inventory' spreadsheet to check the updated values|


