import matplotlib.pylab as plb
import tkinter as tk
import pandas as pd
import h5py

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *

# Read dataset
data = pd.read_hdf("data.h5")

# Bikin window pake tkinter
root = Tk()
root.geometry('500x500')

frame = Frame(root)
frame.pack(side="top", expand=True, fill="both")

# Nyiapin variable buat aplikasinya
x = 0
filters = ['', '', '', '', '', '', '', '', '']
data_filtered = data

# Fungsi-fungsian
# Buat bersihin window/framenya sebelum dipopulate button baru
def clear_frame():
   for widgets in frame.winfo_children():
      widgets.destroy()

# Buat filtering dataframe
def data_filtering(filters, x):
    if x == 0:
        data_filtered = data.loc[data['gender'] == filters[0]]
        return pd.unique(data_filtered['masterCategory'])
    
    elif x == 1:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1])]
        return pd.unique(data_filtered['subCategory'])
    
    elif x == 2:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1]) & (data['subCategory'] == filters[2])]
        return pd.unique(data_filtered['articleType'])
    
    elif x == 3:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1]) & (data['subCategory'] == filters[2]) & (data['articleType'] == filters[3])]
        return pd.unique(data_filtered['baseColour'])

    elif x == 4:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1]) & (data['subCategory'] == filters[2]) & (data['articleType'] == filters[3]) & (data['baseColour'] == filters[4])]
        return pd.unique(data_filtered['season'])

    elif x == 5:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1]) & (data['subCategory'] == filters[2]) & (data['articleType'] == filters[3]) & (data['baseColour'] == filters[4]) & (data['season'] == filters[5])]
        return pd.unique(data_filtered['year'])
    
    elif x == 6:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1]) & (data['subCategory'] == filters[2]) & (data['articleType'] == filters[3]) & (data['baseColour'] == filters[4]) & (data['season'] == filters[5]) & (data['year'] == filters[6])]
        return pd.unique(data_filtered['usage'])
    
    elif x == 7:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1]) & (data['subCategory'] == filters[2]) & (data['articleType'] == filters[3]) & (data['baseColour'] == filters[4]) & (data['season'] == filters[5]) & (data['year'] == filters[6]) & (data['usage'] == filters[7])]
        return pd.unique(data_filtered['productDisplayName'])
    
    elif x == 8:
        data_filtered = data.loc[(data['gender'] == filters[0]) & (data['masterCategory'] == filters[1]) & (data['subCategory'] == filters[2]) & (data['articleType'] == filters[3]) & (data['baseColour'] == filters[4]) & (data['season'] == filters[5]) & (data['year'] == filters[6]) & (data['usage'] == filters[7]) & (data['productDisplayName'] == filters[8])]
        return pd.unique(data_filtered['id'])

# Buat generate list button baru
def button_click(filter):
    global x, filters
    
    if x <= 7:
        filters[x] = filter

        buttons = data_filtering(filters, x)
        x += 1
        
        root.update()
        root.update_idletasks()
        clear_frame()

        for item in buttons:
            button = Button(frame, text=item, command=lambda x=item: button_click(x))
            button.pack(fill=BOTH, expand=YES)

    else:
        filters[x] = filter
        
        items = data_filtering(filters, x)

        root.update()
        root.update_idletasks()
        clear_frame()
        
        fig = plb.figure(figsize=(5,4))

        with h5py.File('images.h5', 'r') as hf:
            photo = plb.imshow(hf[str(items[0])])
            plb.axis('off')

        canvas = FigureCanvasTkAgg(fig, frame)
        toolbar = NavigationToolbar2Tk(canvas, frame)
        toolbar.update()
        canvas._tkcanvas.pack(fill=tk.BOTH, expand=1)
        
        frame.pack(fill=tk.BOTH, expand=1)

# Set button pertama, isinya gender
for item in pd.unique(data['gender']):
    button = Button(frame, text=item, command=lambda x=item: button_click(x))
    button.pack(fill=BOTH, expand=YES)

root.mainloop()