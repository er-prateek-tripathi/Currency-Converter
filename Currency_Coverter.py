# # Python Project on Currency Converter

import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
import pyautogui
import pygame
pygame.mixer.init()

#==============================================================================================================================================================================================================================================

class RealTimeCurrencyConverter():
    def __init__(self,url):
            self.data = requests.get(url).json()
            self.currencies = self.data['rates']

#==============================================================================================================================================================================================================================================       

    def convert(self, from_currency, to_currency, amount): 
        #initial_amount = amount 
        if from_currency != 'USD' : 
            amount = amount / self.currencies[from_currency] 
  
        # limiting the precision to 4 decimal places 
        amount = round(amount * self.currencies[to_currency], 4) 
        return amount
    
#==============================================================================================================================================================================================================================================

class App(tk.Tk):

    def __init__(self, converter):
        
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter
        self.initUI()
        self.Currency_Full_Form()
        self.Usage_Info()
        self.play_music()
        self.Quit()
        
#==========================================================================# Converter Label #=================================================================================================================================================

        #self.configure(background = 'blue')
        self.geometry("1920x1080")
        
        # Label
        self.intro_label = Label(self, text = '$ Real Time Currency Converter $',  fg = 'black', relief = tk.RAISED, borderwidth = 6)
        self.intro_label.config(font = ('algerian',48))#1ST HEADER
        self.intro_label.place(x = 000 , y = 90 , width = 1920 , height = 140) #LOCATION OF 1ST HEADER

#=======================================================================# Updated Currency #===================================================================================================================================================

        #self.date_label = Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.convert('INR','USD',1)} USD \n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 7)
        self.date_label = Label(self, text = f"1 United States Dollar equals = {self.currency_converter.convert('USD','INR',1)} Indian Rupee \n As Updated on : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth = 7)
        self.date_label.config(font = ('comic sans ms',18,'bold italic'))
        self.date_label.place(x = 520, y= 270 , width = 850 , height = 115) #LOCATION OF DATE

#===========================================================================# Entry box #======================================================================================================================================================
        
        valid = (self.register(self.restrictNumberOnly), '%d', '%P')
        self.amount_field = Entry(self,bd = 3, relief = tk.RIDGE, justify = tk.CENTER,validate='key', validatecommand=valid, borderwidth = 6)
        self.converted_amount_field_label = Label(self, text = '', fg = 'blue', bg = 'white', relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth = 6)

#=============================================================================# dropdown #=====================================================================================================================================================
        
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("USD") # default value
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("INR") # default value

#=======================================================================# Conversion Dropdowns #===============================================================================================================================================
        
        font = ("georgia",20, "bold italic")
        self.option_add('*TCombobox*Listbox.font', font)

#==============================================================================# From #========================================================================================================================================================
        
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,values=list(self.currency_converter.currencies.keys()),
         font = font, state = 'readonly', width = 15 , justify = tk.CENTER)
        self.from_currency_dropdown.place(x = 400, y= 450)

#========================================================================# From Input Box #====================================================================================================================================================
            
        self.amount_field.place(x = 425, y = 600 , width = 320 , height = 55 )
        self.amount_field.config(font = ('adobe hebrew' , 18 ))

#=================================================================================# To #=======================================================================================================================================================
        
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,values=list(self.currency_converter.currencies.keys()), 
        font = font, state = 'readonly', width = 15, justify = tk.CENTER)
        
        self.to_currency_dropdown.place(x = 1160, y= 450)

#============================================================================# To Input Box #==================================================================================================================================================
        
        self.converted_amount_field_label.place(x = 1185, y = 600 , width = 320 , height = 55 )
        self.converted_amount_field_label.config(font = ('adobe hebrew' , 18 , 'bold' ))

#============================================================================# Convert button #================================================================================================================================================
        
        self.convert_button = Button(self, text = "Convert Currency", fg = "black",bg = 'orange' ,  command = self.perform) 
        self.convert_button.config(font=('comic sans ms', 15, 'bold italic'))
        self.convert_button.place(x = 830, y = 750)

#=============================================================================# Quit Window #==================================================================================================================================================

    def Quit(self):
        quit = Button(self, text="Click to Quit/Exit", fg="black", bg = 'red' , command = self.iExit)
        quit.config(font=('comic sans ms', 13, 'bold italic'))
        quit.place(x = 1235 , y = 850)                   
        #self.quit.pack(side="bottom")


    def iExit(self):
        pyautogui.moveTo(920 , 650 )
        iexit = mbox.askyesno("Currency Converter","Confirm if you want to Exit")
        if iexit > 0:
            self.destroy()
        
#====================================================================# Background Sound System #===============================================================================================================================================
 
    def play_music(self):
        pygame.mixer.music.load("ThemeMusic.mp3")

        #Play Button
        play = Button(self , text = " Play Song " , fg = "black" , bg = "white" , command = self.PlaySong )
        play.config(font = ('arial', 13 , 'bold'))
        play.place(x = 1600 , y = 1000)

        #Pause Button
        pause = Button(self , text = " Pause Song " , fg = "black" , bg = "white" , command = self.PauseSong )
        pause.config(font = ('arial', 13 , 'bold'))
        pause.place(x = 1750 , y = 1000)
        pygame.mixer.music.play()

    def PauseSong(self):
        pygame.mixer.music.pause()

    def PlaySong(self):
        pygame.mixer.music.unpause()

#====================================================================# How to USE the Calculator #=============================================================================================================================================

    def Usage_Info(self):
        usage = Button(self , text = "How To Use!!" , bg = 'cyan' , command = self.UInfo)
        usage.config(font = ('algerian' , 15  ))
        usage.place(x = 0000 , y = 1000)


    def UInfo(self):
        pyautogui.moveTo(1140,820 )
        mbox.showinfo("How To Use!!" , "Usage : \n 1. Always input the amount to be converted in the left box. \n\n 2. You are not supposed to feed any data in the right input box , as it will not accept. \n Do not waste time on that. \n\n 3. To switch into other currencies there are two dropdowns above each input box. \n  You can use that for the purpose. \n\n 4. The currency is updated every day. \n\n 5. The Currency is updated from the API Key link,  DO NOT TRY to ALTER that in the SOURCE CODE. \n\n 6. The Calculator works on internet connectivity. \n \n After Reading \n \n Click OK to Close !!")
        
#=====================================================================# Currency Information #=================================================================================================================================================

    def Currency_Full_Form(self):
            fullform = Button(self, text="Currency Information",bg = 'yellow', command=self.fullForm)
            fullform.config(font = ('adobe hebrew',15,'bold italic'))
            fullform.grid(row=1, column=1)
            #fullform.place(x = 100 , y = 100)


    def fullForm(self):
        
        pyautogui.moveTo(1085,900)

        mbox.showinfo("FullForm"," 1. USD = United States Dollar \n 2. INR = Indian Rupee \n 3. AED = United Arab Emirates Dirham \n 4. ARS = Argentine Peso \n 5. AUD = Australian Dollar \n 6. BGN = Bulgarian Lev \n 7. BRL = Brazilian Real \n 8. BSD = Bahamian Dollar \n 9. CAD = Canadian Dollar \n 10. CHF = Swiss Franc Currency \n 11. CLP = Chilean Peso \n 12. CNY = Chinese Yuan \n 13. COP = Colombian Peso \n 14. CZK = koruna Of Czech Republic \n 15. DKK = Danish Krone , Denmark \n 16. DOP = Dominican Peso \n 17. EGP = Egyptian Pound \n 18. EUR = Euro \n 19. FJD = Fiji Dollar \n 20. GBP = British Pound Sterling \n 21. GTQ = Guatemalan Quetzal \n 22. HKD = Hong Kong Dollar \n 23. HRK = kuna , Croatia \n 24. HUF = Hungarian Forint \n 25. IDR = Indonesian Rupiah \n 26. ILS = Israeli New Shekel \n \n \nClick OK")
        pyautogui.moveTo(1085,900)

        mbox.showinfo("FullForm", " 27. ISK = króna , Iceland \n 28. JPY = Japanese Yen \n 29. KRW = Korean Republic Won \n 30. KZT = Tenge , Kzakhastan \n 31. MVR = Maldivian Rufiyaa \n 32. MXN = Mexican Peso \n 33. MYR = Malaysian Ringgit \n 34. NOK = Norwegian Krone \n 35. NZD = New Zealand Dollar \n 36. PAB = Panamanian Balboa \n 37. PEN = Peruvian Sol , Peru \n 38. PHP = Philippine Peso \n 39. PKR = Pakistani Rupee \n 40. PLN = Polish Zloty \n 41. PYG = Paraguayan Guarani , Pragua \n 42. RON = Romanian Leu \n 43. RUB = Russian Ruble \n 44. SAR = Saudi Riyal \n 45. SEK = Swedish Krona \n 46. SGD = Singapore Dollar \n 47. THB = Thai Baht \n 48. TRY = Turkish Lira \n 49. TWD = New Taiwan Dollar \n 50. UAH = Ukrainian Hryvnia \n 51. UYU = Uruguayan Peso \n 52. ZAR = South African Rand \n \n \nClick OK To Exit !!")
        pyautogui.moveTo(1085,900)

#========================================================================# Developers Information #============================================================================================================================================
      
    def initUI(self):
            inform = Button(self, text="Developers' Info",bg = 'lime', command=self.onInfo)
            inform.config(font = ('adobe hebrew',15,'bold italic'))
            #inform.grid(row=1, column=1)
            inform.place(x = 460 , y = 850)
            

    def onInfo(self):
        
        pyautogui.moveTo(1000,650)

        mbox.showinfo("Information","Project Group = 3 \n \nClick OK")
        pyautogui.moveTo(1020,695)

        mbox.showinfo("Information", "Name = Prateek Tripathi \n \nRegdn = 11908181 \n \nRoll No. = RK19RHB56 \n \nClick OK!!")
        pyautogui.moveTo(1020,695)

        mbox.showinfo("Information", "Name = Sahyogvir Singh \n \nRegdn = 11904949 \n \nRoll No. = RK19RHB45 \n \nClick OK!!")
        pyautogui.moveTo(1020,695)

        mbox.showinfo("Information", "Name = Aditya Yadav \n \nRegdn = 11914375 \n \nRoll No. = RK19RHB71 \n \nClick OK!!")
        pyautogui.moveTo(1020,695)

#==========================================================================# Calculations #====================================================================================================================================================

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr,to_curr,amount)
        converted_amount = round(converted_amount, 3)

        self.converted_amount_field_label.config(text = str(converted_amount))
        
    def restrictNumberOnly(self, action, string):
        regex = re.compile(r"[0-9,]*?(\.)?[0-9,]*$")
        result = regex.match(string)
        return (string == "" or (string.count('.') <= 1 and result is not None))

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = RealTimeCurrencyConverter(url)

    App(converter)
    mainloop()

# Online-Currency-Converter
# Online-Currency-Converter
Do Not Forget to Download the file 'ThemeMusic.mp3' in the same folder.
In which the python file is kept.
Its mandatory.