import tkinter as tk
import tkinter.filedialog
from tkinter import PhotoImage
from pa.pa.spiders.ycharts import run_scraper
import os

class ScrapeApp(tk.Tk):

    save_path = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/buyback_history/')

    def __init__(self):
        tk.Tk.__init__(self)


        # title
        self.label_title = tk.Label(self, text='Stock Buyback History')
        # self.label_title.config(font=("Lucida Grande font", 30))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

        # line 1 stock name
        self.label_stock = tk.Label(self, text='Enter stock symbol')
        self.label_stock.grid(row=2, column=0, padx=10, pady=10)


        self.entry_stock = tk.Entry(self)
        self.entry_stock.grid(row=2, column=1, sticky='W', padx=10, pady=10)

        # line 2 save path
        self.button = tk.Button(self, text='Browse path', command=self.browse_button)
        self.button.grid(row=4, column=0, padx=10, pady=10, ipadx = 20)

        self.label_path = tk.Label(self, text=self.save_path)
        self.label_path.grid(row=4, column=1, padx=10, pady=10 )

        # line 2 go

        # self.logo = PhotoImage(file='Doge.png')
        # self.logo = self.logo.subsample(8)
        self.button = tk.Button(self, text='Export',  command=self.scrape_button)
        self.button.grid(row=5, column=0, padx=10, pady=10, sticky='W', ipadx = 40,  columnspan=2)


    def browse_button(self):

        path = tk.filedialog.askdirectory()
        if path != '':
            self.save_path = path
            print(self.save_path)
            self.label_path.configure(text=self.save_path)


    def get_stock(self):
        stock = self.entry_stock.get()
        stock = stock.strip().upper()
        return stock

    def scrape_button(self):
        if self.get_stock() != '':
            run_scraper(self.get_stock(),self.save_path)

app = ScrapeApp()
app.title("stock buyback")
# app.geometry("500x500")
app.mainloop()

