import pandas as pd
from datetime import datetime
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter import *
import os

import matplotlib.pyplot as plt
import seaborn as sns

list_Estimatenum=[]
list_Productnum=[]
list_Totalquantity=[]
list_time=[]
list_date=[]

#####################Load inventory and Estimates files############################
def import_inventory():
    root = Tk()# we don't want a full GUI, so keep the root window from appearing
    root.withdraw()
    filename_i = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename_i)
    #Inventory spreadsheet
    global inventory
    inventory = pd.read_csv(filename_i)

def import_estimates():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename_e = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename_e)
    #Estimates spreadsheet
    global estimates
    estimates = pd.read_csv(filename_e)
    #r"C:\Users\jeffz\Documents\inventory start\Estimates.csv"

#ADD ENTRY
def add_record():
    global Estimatenum
    Estimatenum = input("Estimate/service appointment number (type 'ditto' to repeat):")
    list_Estimatenum.append(Estimatenum)
    global Productnum
    Productnum = input("Input Product#:") #C9-1000-12-BK and C9-1000-12-W as test
    list_Productnum.append(Productnum)
    global Totalquantity
    Totalquantity = int(input("Input total quantity used:"))
    list_Totalquantity.append(Totalquantity)
    dt = datetime.now()
    global time
    time = dt.strftime("%H:%M:%S")
    list_time.append(time)

    global date
    date = dt.strftime("%d/%m/%Y")
    list_date.append(date)  

    #check if Product num is valid
    productnumbers = inventory['Product num'].unique()
    
    if Productnum in productnumbers:
        print("The product number is valid")
    else:
        print("The product number is not valid, retry")
        #list_Estimatenum.del(-1)
        #list_Productnum.del(-1)
        #list_Totalquantity.del(-1)
        #list_Estimatenum.del(-1)
        #list_time.del(-1)
        #list_date.del(-1)

def clear_record():
    list_Estimatenum.clear()
    list_Productnum.clear()
    list_Totalquantity.clear()
    list_Estimatenum.clear()
    list_time.clear()
    list_date.clear()

################ENTER new estimat record#####################

def view_record():
    ####################combine values into a dataframe matching the 'Estimates' csv file##########
    global Addeditems
    Addeditems = pd.DataFrame({'Estimate number': list_Estimatenum,
                        'Product num' : list_Productnum,#these can have multiple per estimate
                         'Quantity' : list_Totalquantity,
                         'Date entered': list_date,
                         'Time entered': list_time})
    print(Addeditems)

#####################locate product number on inventory spreadsheet and update the quantity and date and time entered###############
def update_inventory():
    rowtoadjust = inventory.loc[inventory['Product num'].isin(list_Productnum),['Total_Units']]
    unitstoadjust = rowtoadjust.iat[0,0]#isolate sell value for 'total units'
    global inventoryupdated
    inventoryupdated = inventory.copy()
    inventoryupdated.loc[inventoryupdated['Product num'].isin(list_Productnum),['Total_Units','Date of last entry','Time of last entry']] = [(unitstoadjust-Totalquantity),date,time]

###################add new estimate record to estimates dataframe

def view_modified_products():
    print(inventoryupdated.loc[inventoryupdated['Product num'].isin(list_Productnum),['Product category', 'Product num','Total_Units','Date of last entry','Time of last entry']])
 
def view_products_to_update():
    print(inventory.loc[inventory['Product num'].isin(list_Productnum),['Product category', 'Product num','Total_Units','Date of last entry','Time of last entry']])
 
#inventoryupdated['Total Units']
def save_inventory():
  date_write = date.replace("/","_")
    inventoryupdated.to_csv("inventory_updated_"+date_write+"out.csv")

def save_estimates():
    global estimates_updated
    estimates_updated = pd.concat([estimates, Addeditems], ignore_index = True, axis = 0)
    estimates_updated
    date_write = date.replace("/","_")
    estimates_updated.to_csv(rootpath + date_write+"\\estimates_"+date_write+".csv")




#####plotting

instock.loc[instock['Product category']=='Lighted Strings']#subset data by group
instock.loc[instock['Product num']=='5MM-50L-25-6-G-PW']#subset data by product num

#def ylogplot(X):
#    ax= sns.barplot(x='Product num',y='Total Units',data=bycategory.get_group(instock['Product category'].unique()[X]))#
#    ax.set(title = instock['Product category'].unique()[X], yscale = 'log')
#    ax.tick_params(axis='x', rotation=25)
#    ax.tick_params(axis='y', which='minor')
#    plt.show()

####VIEW PLOT OF Socket wire
#plot(0)#socket wire
#plot(1)#Retrofit bulbs
#plot(2)#Lighted strings
#plot(3)#accessories - log
#plot(4)#Patio Lights
#plot(5)#Floods
def showproductnumbers():
    print(inventory['Product num'].unique())

def saveplot(X):
    instock = inventoryupdated[inventoryupdated['Total_Units']>0]#only select data where there is stock
    date_write = date.replace("/","_")
    ax= sns.barplot(x='Product num',y='Total_Units',data=instock.loc[instock['Product category']==instock['Product category'].unique()[X]])#
    #show_values_on_bars(ax, h_v="v", space=0.4)
    ax.set(title = instock['Product category'].unique()[X])
    ax.tick_params(axis='x', rotation=25)
    for p in ax.patches:#add values above bar charts
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points')
    fg = plt.gcf()
    fg.set_size_inches(8, 8)
    plt.savefig(rootpath+ date_write +"\\plots_"+instock['Product category'].unique()[X]+date_write+'.png')
    plt.show()

saveplot(4)
saveplot(0)
saveplot(1)
saveplot(2)
saveplot(3)
saveplot(4)
saveplot(5)


for i in range(6):
    saveplot(i)

#display according to categories:
#1. Socket Wire
#2. Retrofit Bulbs
#3. Lighted Strings
#4. Accessories
#5. Patio Lights
#6. Floods
#7. Other Decor

def viewplot(X):
    instock = inventory[inventory['Total_Units']>0]#only select data where there is stock
    bycategory = instock.groupby('Product category')#subset data into groups
    date_write = date.replace("/","_")
    ax= sns.barplot(x='Product num',y='Total_Units',data=bycategory.get_group(instock['Product category'].unique()[X]))
    ax.tick_params(axis='x', rotation=25)
    ax.set(title=instock['Product category'].unique()[X])#
    #fg = plt.gcf()
    #fg.set_size_inches(8, 8)
    for p in ax.patches:#add values above bar charts
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points')
    #plt.show()

instock = inventory[inventory['Total_Units']>0]

#example facet grid
tips = sns.load_dataset("instock")
g = sns.FacetGrid(col="time")
g = sns.FacetGrid(tips, col="day", height=4, aspect=.5)
g.map(sns.barplot, "sex", "total_bill", order=["Male", "Female"])
plt.show()

fig, axs = plt.subplots(ncols=3, nrows=2)
sns.barplot(x='Product num',y='Total_Units',data=bycategory.get_group(instock['Product category'].unique()[1]))
sns.barplot(x='Product num',y='Total_Units',data=bycategory.get_group(instock['Product category'].unique()[2]))
view_plot(1)
view_plot(1)
view_plot(1)
view_plot(1)
view_plot(1)
plt.show()


sns.regplot(x='value', y='wage', data=df_melt, ax=axs[0])
sns.regplot(x='value', y='wage', data=df_melt, ax=axs[1])
sns.boxplot(x='education',y='wage', data=df_melt, ax=axs[2])


prod_cat = sns.FacetGrid(
        instock,
        col="Product category",
        height = 3.5,
        aspect = .7
    )
g.map(sns.barplot, data = instock, x='Product num',y='Total_Units')
plt.show()

sns.barplot(x='Product num',y='Total_Units',data=bycategory.get_group(instock['Product category'].unique()[X]))


tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time")
g = sns.FacetGrid(tips, col="day", height=4, aspect=.5)
g.map(sns.barplot, "sex", "total_bill", order=["Male", "Female"])
plt.show()

instock = inventory[inventory['Total Units']>0]#only select data where there is stock
bycategory = instock.groupby('Product category')#subset data into groups
bycategory.get_group(instock['Product category'].unique()[0])['Total Units']
bycategory.get_group(instock['Product category'].unique()[0])['Product num']

sns.barplot(x='Product num',y='Total Units',data=instock.loc[instock['Product category']==instock['Product category'].unique()[4]])
plt.show()
# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')





