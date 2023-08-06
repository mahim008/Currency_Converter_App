from tkinter import *

class CurrencyConverter:
    def __int__(self):
        app_window = Tk()
        app_window.title("Currency Converter")
        app_window.configure(bg="yellow")
        Label(app_window, font="Helvetica 12 bold", bg="yellow", text="Amount to Convert").grid(row = 1, column = 1, stricky = W)
        Label(app_window, font="Helvetica 12 bold", bg="yellow", text="Conversion Rate").grid(row = 2, column = 1, stricky = W)
        Label(app_window, font="Helvetica 12 bold", bg="yellow", text="Converted Amount").grid(row = 3, column = 1, stricky = W)


