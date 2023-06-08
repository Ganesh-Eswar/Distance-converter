import tkinter.font as font  
from tkinter import ttk
from tkinter import *
import distance_con_backend as db

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("700x800")
        self.title("Distance converter")
        self.resizable(False,False)

class TitleFrame():
    def __init__(self,cont) -> None:
        
        # setting tile frame 
        self.Frame1 = Frame(cont,background="pink",width=700,padx=10,pady=10,height=80)
        self.Frame1.place(x=0,y=0)

        self.title_font = font.Font(family="Times",weight="bold",
                            slant="italic",size=30)

        self.title_name = Label(self.Frame1,text="Distance converter",
                        foreground="black",background="pink",
                        font=self.title_font)

        self.title_name.place(x=170,y=0)


# Middle portion
class MiddlePortion():
    def __init__(self,cont) -> None:
        

        # two containers
        self.middle_main_frame = Frame(cont,width=600,height=540)
        self.middle_main_frame.place(x=50,y=150)

        self.middle_sub_container = Frame(self.middle_main_frame,background="#a8cacf",
                                    width=570,height=510)
        self.middle_sub_container.place(x=15,y=20)

        #millimeter creation
        self.mm_meter_font = font.Font(family="Arial",size=15)
        self.mm_meter_label = Label(self.middle_sub_container,text="Millimetre",
                            foreground="white",background="#a8cacf",
                            font=self.mm_meter_font,padx=10,pady=10)
        self.mm_meter_label.place(x=45,y=10)

        self.calculated_mm_value = StringVar(value="Value shown here")
        self.mm_meter_value_font = font.Font(family="Arial",size=15)
        self.mm_meter_value_label = Label(self.middle_sub_container,textvariable=self.calculated_mm_value,
                            foreground="black",background="#a8cacf",
                            font=self.mm_meter_value_font,padx=10,pady=10
                            )

        self.mm_meter_value_label.place(x=320,y=10)

        # Separator

        self.separtor1 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor1.place(x=0,y=55,relwidth=10)


        #Kilometer creation
        self.kilo_meter_font = font.Font(family="Arial",size=15)
        self.kilo_meter_label = Label(self.middle_sub_container,text="Kilometre",
                            foreground="white",background="#a8cacf",
                            font=self.kilo_meter_font,padx=10,pady=10)
        self.kilo_meter_label.place(x=45,y=60)

        self.calculated_kilo_value = StringVar(value="Value shown here")
        self.kilo_meter_value_font = font.Font(family="Arial",size=15)
        self.kilo_meter_value_label = Label(self.middle_sub_container,textvariable=self.calculated_kilo_value,
                            foreground="black",background="#a8cacf",
                            font=self.kilo_meter_value_font,padx=10,pady=10
                            )

        self.kilo_meter_value_label.place(x=320,y=60)

        # Separator

        self.separtor2 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor2.place(x=0,y=105,relwidth=10)



        #Miles creation
        self.miles_font = font.Font(family="Arial",size=15)
        self.miles_label = Label(self.middle_sub_container,text="Mile",
                            foreground="white",background="#a8cacf",
                            font=self.miles_font,padx=10,pady=10)
        self.miles_label.place(x=45,y=110)

        self.calculated_mile_value = StringVar(value="Value shown here")
        self.mile_value_font = font.Font(family="Arial",size=15)
        self.mile_value_label = Label(self.middle_sub_container,textvariable=self.calculated_mile_value,
                            foreground="black",background="#a8cacf",
                            font=self.mile_value_font,padx=10,pady=10
                            )

        self.mile_value_label.place(x=320,y=110)

        # Separator

        self.separtor3 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor3.place(x=0,y=155,relwidth=10)


        #Inches creation
        self.inches_font = font.Font(family="Arial",size=15)
        self.inches_label = Label(self.middle_sub_container,text="Inch",
                            foreground="white",background="#a8cacf",
                            font=self.inches_font,padx=10,pady=10)
        self.inches_label.place(x=45,y=160)

        self.calculated_inches_value = StringVar(value="Value shown here")
        self.inches_value_font = font.Font(family="Arial",size=15)
        self.inches_value_label = Label(self.middle_sub_container,textvariable=self.calculated_inches_value,
                            foreground="black",background="#a8cacf",
                            font=self.inches_value_font,padx=10,pady=10
                            )
        self.inches_value_label.place(x=320,y=160)

        # Separator

        self.separtor4 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor4.place(x=0,y=205,relwidth=10)


        #Yards creation
        self.yards_font = font.Font(family="Arial",size=15)
        self.yards_label = Label(self.middle_sub_container,text="Yard",
                            foreground="white",background="#a8cacf",
                            font=self.yards_font,padx=10,pady=10)
        self.yards_label.place(x=45,y=210)

        self.calculated_yards_value = StringVar(value="Value shown here")
        self.yards_value_font = font.Font(family="Arial",size=15)
        self.yards_value_label = Label(self.middle_sub_container,textvariable=self.calculated_yards_value,
                            foreground="black",background="#a8cacf",
                            font=self.yards_value_font,padx=10,pady=10
                            )
        self.yards_value_label.place(x=320,y=210)

        # Separator

        self.separtor5 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor5.place(x=0,y=255,relwidth=10)



        #Feets creation
        self.feet_font = font.Font(family="Arial",size=15)
        self.feet_label = Label(self.middle_sub_container,text="Feet",
                            foreground="white",background="#a8cacf",
                            font=self.feet_font,padx=10,pady=10)
        self.feet_label.place(x=45,y=260)

        self.calculated_feet_value = StringVar(value="Value shown here")
        self.feet_value_font = font.Font(family="Arial",size=15)
        self.feet_value_label = Label(self.middle_sub_container,textvariable=self.calculated_feet_value,
                            foreground="black",background="#a8cacf",
                            font=self.feet_value_font,padx=10,pady=10
                            )
        self.feet_value_label.place(x=320,y=260)

        # Separator

        self.separtor6 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor6.place(x=0,y=305,relwidth=10)

        #Cubit creation
        self.cubit_font = font.Font(family="Arial",size=15)
        self.cubit_label = Label(self.middle_sub_container,text="Cubits",
                            foreground="white",background="#a8cacf",
                            font=self.cubit_font,padx=10,pady=10)
        self.cubit_label.place(x=45,y=310)

        self.calculated_cubit_value = StringVar(value="Value shown here")
        self.cubit_value_font = font.Font(family="Arial",size=15)
        self.cubit_value_label = Label(self.middle_sub_container,textvariable=self.calculated_cubit_value,
                            foreground="black",background="#a8cacf",
                            font=self.cubit_value_font,padx=10,pady=10
                            )
        self.cubit_value_label.place(x=320,y=310)

        # Separator

        self.separtor7 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor7.place(x=0,y=355,relwidth=10)


        #Nautical mile creation
        self.nautical_mile_font = font.Font(family="Arial",size=15)
        self.nautical_mile_label = Label(self.middle_sub_container,text="Nautical mile",
                            foreground="white",background="#a8cacf",
                            font=self.nautical_mile_font,padx=10,pady=10)
        self.nautical_mile_label.place(x=45,y=360)

        self.calculated_nautical_mile_value = StringVar(value="Value shown here")
        self.nautical_mile_value_font = font.Font(family="Arial",size=15)
        self.nautical_mile_value_label = Label(self.middle_sub_container,textvariable=self.calculated_nautical_mile_value,
                            foreground="black",background="#a8cacf",
                            font=self.nautical_mile_value_font,padx=10,pady=10
                            )

        self.nautical_mile_value_label.place(x=320,y=360)

        # Separator

        self.separtor8 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor8.place(x=0,y=405,relwidth=10)



        #Forlongs creation
        self.forlongs_font = font.Font(family="Arial",size=15)
        self.forlongs_label = Label(self.middle_sub_container,text="Forlongs",
                            foreground="white",background="#a8cacf",
                            font=self.forlongs_font,padx=10,pady=10)
        self.forlongs_label.place(x=45,y=410)

        self.calculated_forlongs_value = StringVar(value="Value shown here")
        self.forlongs_value_font = font.Font(family="Arial",size=15)
        self.forlongs_value_label = Label(self.middle_sub_container,textvariable=self.calculated_forlongs_value,
                            foreground="black",background="#a8cacf",
                            font=self.forlongs_font,padx=10,pady=10
                            )

        self.forlongs_value_label.place(x=320,y=410)

        # Separator

        self.separtor9 = ttk.Separator(self.middle_sub_container,orient='horizontal')

        self.separtor9.place(x=0,y=455,relwidth=10)

        #Astronomical Units creation
        self.astronomical_units_font = font.Font(family="Arial",size=15)
        self.astronomical_units_label = Label(self.middle_sub_container,text="Astronomical unit",
                            foreground="white",background="#a8cacf",
                            font=self.astronomical_units_font,padx=10,pady=10)
        self.astronomical_units_label.place(x=45,y=460)

        self.calculated_astronomical_units_value = StringVar(value="Value shown here")
        self.astronomical_units_value_font = font.Font(family="Arial",size=15)
        self.astronomical_units_value_label = Label(self.middle_sub_container,textvariable=self.calculated_astronomical_units_value,
                            foreground="black",background="#a8cacf",
                            font=self.astronomical_units_font,padx=10,pady=10
                            )

        self.astronomical_units_value_label.place(x=320,y=460)

class Calculation():
    def __init__(self,cont) -> None:
        
        self.va = EnterSection(cont)
        self.mid = MiddlePortion(cont)
            
        # calculate part 
        def calculate_values():
            self.enter_value = int(self.va.user_value.get())
            self.calculation_part = db.DistanceConverter(self.enter_value)
            self.mid.calculated_astronomical_units_value.set(self.calculation_part.astronomical_units())
            self.mid.calculated_feet_value.set(self.calculation_part.feet())
            self.mid.calculated_cubit_value.set(self.calculation_part.cubit())
            self.mid.calculated_forlongs_value.set(self.calculation_part.forlong())
            self.mid.calculated_inches_value.set(self.calculation_part.inches())
            self.mid.calculated_kilo_value.set(self.calculation_part.kilometer())
            self.mid.calculated_mile_value.set(self.calculation_part.miles())
            self.mid.calculated_mm_value.set(self.calculation_part.millimeter())
            self.mid.calculated_nautical_mile_value.set(self.calculation_part.nautical_mile())
            self.mid.calculated_yards_value.set(self.calculation_part.yards())
            

        self.calculate_button_font = font.Font(family="Arial",size=10,weight='bold')

        self.calculate_button = Button(cont,text="Calculate",command=calculate_values,
                                background="red",foreground="white",padx=5,
                                pady=5,activebackground="yellow",width=10,
                                font=self.calculate_button_font,
                                state="active",cursor="hand2")
                   

        self.calculate_button.place(x=570,y=700)

class EnterSection():
    
    
    
    def __init__(self,cont) -> None:
        
        #Enter part 

        def isOkey(input):
            
            try:
                if(input == ""):
                    
                    return True
                
                number = int(input)
                if(0<=number<=100000000):
                    
                    return True 
                else:
                    return False 
            except:
                return False 

        self.regist = cont.register(isOkey)

        self.enter_label_font = font.Font(family="Arial",size=15)
        self.enter_label = Label(cont,text="Enter the value in meters: ",font=self.enter_label_font)
        self.enter_label.place(x=70,y=100)

        self.user_value = StringVar()
        self.user_entry_font = font.Font(size=20)
        self.user_entry = Entry(cont,width=10,foreground="red",
                        takefocus=True,textvariable=self.user_value,
                        font=self.user_entry_font,
                        validate="all",validatecommand=(self.regist,"%P"))

        self.user_entry.place(x=400,y=100)

if __name__ == "__main__":
    win = Window()
    ti = TitleFrame(win)
    cal = Calculation(win)
    win.mainloop()

