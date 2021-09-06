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

    #check if product # is valid
    productnumbers = inventory['Product #'].unique()
    
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
                        'Product #' : list_Productnum,#these can have multiple per estimate
                         'Quantity' : list_Totalquantity,
                         'Date entered': list_date,
                         'Time entered': list_time})
    print(Addeditems)

#####################locate product number on inventory spreadsheet and update the quantity and date and time entered###############
def update_inventory():
    rowtoadjust = inventory.loc[inventory['Product #'].isin(list_Productnum),['Total Units']]
    unitstoadjust = rowtoadjust.iat[0,0]#isolate sell value for 'total units'
    global inventoryupdated
    inventoryupdated = inventory.copy()
    inventoryupdated.loc[inventoryupdated['Product #'].isin(list_Productnum),['Total Units','Date of last entry','Time of last entry']] = [(unitstoadjust-Totalquantity),date,time]

###################add new estimate record to estimates dataframe

def view_modified_products():
    print(inventoryupdated.loc[inventoryupdated['Product #'].isin(list_Productnum),['Product category', 'Product #','Total Units','Date of last entry','Time of last entry']])
 
def view_products_to_update():
    print(inventory.loc[inventory['Product #'].isin(list_Productnum),['Product category', 'Product #','Total Units','Date of last entry','Time of last entry']])
 
############write updated csv files to file##################
rootpath = r"C:\Users\jeffz\Documents\inventorystart\updates\\"
date_write = date.replace("/","_")
os.mkdir(rootpath+date_write)

#inventoryupdated['Total Units']
def save_inventory():
    date_write = date.replace("/","_")
    inventoryupdated.to_csv(rootpath + date_write+"\\inventory_"+date_write+".csv")

def save_estimates():
    global estimates_updated
    estimates_updated = pd.concat([estimates, Addeditems], ignore_index = True, axis = 0)
    estimates_updated
    date_write = date.replace("/","_")
    estimates_updated.to_csv(rootpath + date_write+"\\estimates_"+date_write+".csv")


#####plotting

instock.loc[instock['Product category']=='Lighted Strings']#subset data by group
instock.loc[instock['Product #']=='5MM-50L-25-6-G-PW']#subset data by product num

#def ylogplot(X):
#    ax= sns.barplot(x='Product #',y='Total Units',data=bycategory.get_group(instock['Product category'].unique()[X]))#
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


def saveplot(X):
    instock = inventoryupdated[inventoryupdated['Total Units']>0]#only select data where there is stock
    date_write = date.replace("/","_")
    ax= sns.barplot(x='Product #',y='Total Units',data=instock.loc[instock['Product category']==instock['Product category'].unique()[X]])#
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



def viewplot(X):
    instock = inventory[inventory['Total Units']>0]#only select data where there is stock
    bycategory = instock.groupby('Product category')#subset data into groups
    date_write = date.replace("/","_")
    ax= sns.barplot(x='Product #',y='Total Units',data=bycategory.get_group(instock['Product category'].unique()[X]))#
    #ax.set(title = instock['Product category'].unique()[X])
    ax.tick_params(axis='x', rotation=25)
    #fg = plt.gcf()
    #fg.set_size_inches(8, 8)
    for p in ax.patches:#add values above bar charts
        ax.annotate(format(p.get_height(), '.1f'), 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points')
    plt.show()
    #plt.savefig(rootpath+ date_write +"\\plots_"+instock['Product category'].unique()[X]+date_write+'.png')  

instock = inventory[inventory['Total Units']>0]#only select data where there is stock
bycategory = instock.groupby('Product category')#subset data into groups
bycategory.get_group(instock['Product category'].unique()[0])['Total Units']
bycategory.get_group(instock['Product category'].unique()[0])['Product #']

sns.barplot(x='Product #',y='Total Units',data=instock.loc[instock['Product category']==instock['Product category'].unique()[4]])
plt.show()
# function to add value labels
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')





