import tkinter.font as font  
from tkinter import ttk
from tkinter import *
import distance_con_backend as db


root = Tk()
root.geometry("700x800")
root.title("Distance converter")
root.resizable(False,False)

# setting tile frame 
Frame1 = Frame(root,background="pink",width=700,padx=10,pady=10,height=80)
Frame1.place(x=0,y=0)

title_font = font.Font(family="Times",weight="bold",
                       slant="italic",size=30)

title_name = Label(Frame1,text="Distance converter",
                   foreground="black",background="pink",
                   font=title_font)

title_name.place(x=170,y=0)

#Enter part 

def isOkey(input):
    
    try:
        if(input == ""):
            calculate_button.config(state="disabled")
            return True
        
        number = int(input)
        
        if(0<=number<=100000000):
            calculate_button.config(state="normal")
            return True 
        else:
            return False 
    except:
        return False 

regist = root.register(isOkey)

enter_label_font = font.Font(family="Arial",size=15)
enter_label = Label(root,text="Enter the value in meters: ",font=enter_label_font)
enter_label.place(x=70,y=100)

user_value = StringVar()
user_entry_font = font.Font(size=20)
user_entry = Entry(root,width=10,foreground="red",
                   takefocus=True,textvariable=user_value,
                   font=user_entry_font,
                   validate="all",validatecommand=(regist,"%P"))

user_entry.place(x=400,y=100)

# Middle portion

# two containers
middle_main_frame = Frame(root,width=600,height=540)
middle_main_frame.place(x=50,y=150)

middle_sub_container = Frame(middle_main_frame,background="#a8cacf",
                             width=570,height=510)
middle_sub_container.place(x=15,y=20)

#millimeter creation
mm_meter_font = font.Font(family="Arial",size=15)
mm_meter_label = Label(middle_sub_container,text="Millimeters",
                       foreground="white",background="#a8cacf",
                       font=mm_meter_font,padx=10,pady=10)
mm_meter_label.place(x=45,y=10)

calculated_mm_value = StringVar(value="Value shown here")
mm_meter_value_font = font.Font(family="Arial",size=15)
mm_meter_value_label = Label(middle_sub_container,textvariable=calculated_mm_value,
                       foreground="black",background="#a8cacf",
                       font=mm_meter_value_font,padx=10,pady=10
                       )

mm_meter_value_label.place(x=320,y=10)

# Separator

separtor1 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor1.place(x=0,y=55,relwidth=10)


#Kilometer creation
kilo_meter_font = font.Font(family="Arial",size=15)
kilo_meter_label = Label(middle_sub_container,text="Kilometers",
                       foreground="white",background="#a8cacf",
                       font=kilo_meter_font,padx=10,pady=10)
kilo_meter_label.place(x=45,y=60)

calculated_kilo_value = StringVar(value="Value shown here")
kilo_meter_value_font = font.Font(family="Arial",size=15)
kilo_meter_value_label = Label(middle_sub_container,textvariable=calculated_kilo_value,
                       foreground="black",background="#a8cacf",
                       font=kilo_meter_value_font,padx=10,pady=10
                       )

kilo_meter_value_label.place(x=320,y=60)

# Separator

separtor2 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor2.place(x=0,y=105,relwidth=10)



#Miles creation
miles_font = font.Font(family="Arial",size=15)
miles_label = Label(middle_sub_container,text="Miles",
                       foreground="white",background="#a8cacf",
                       font=miles_font,padx=10,pady=10)
miles_label.place(x=45,y=110)

calculated_mile_value = StringVar(value="Value shown here")
mile_value_font = font.Font(family="Arial",size=15)
mile_value_label = Label(middle_sub_container,textvariable=calculated_mile_value,
                       foreground="black",background="#a8cacf",
                       font=mile_value_font,padx=10,pady=10
                       )

mile_value_label.place(x=320,y=110)

# Separator

separtor3 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor3.place(x=0,y=155,relwidth=10)


#Inches creation
inches_font = font.Font(family="Arial",size=15)
inches_label = Label(middle_sub_container,text="Inches",
                       foreground="white",background="#a8cacf",
                       font=inches_font,padx=10,pady=10)
inches_label.place(x=45,y=160)

calculated_inches_value = StringVar(value="Value shown here")
inches_value_font = font.Font(family="Arial",size=15)
inches_value_label = Label(middle_sub_container,textvariable=calculated_inches_value,
                       foreground="black",background="#a8cacf",
                       font=inches_value_font,padx=10,pady=10
                       )
inches_value_label.place(x=320,y=160)

# Separator

separtor4 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor4.place(x=0,y=205,relwidth=10)


#Yards creation
yards_font = font.Font(family="Arial",size=15)
yards_label = Label(middle_sub_container,text="Yards",
                       foreground="white",background="#a8cacf",
                       font=yards_font,padx=10,pady=10)
yards_label.place(x=45,y=210)

calculated_yards_value = StringVar(value="Value shown here")
yards_value_font = font.Font(family="Arial",size=15)
yards_value_label = Label(middle_sub_container,textvariable=calculated_yards_value,
                       foreground="black",background="#a8cacf",
                       font=yards_value_font,padx=10,pady=10
                       )
yards_value_label.place(x=320,y=210)

# Separator

separtor5 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor5.place(x=0,y=255,relwidth=10)



#Feets creation
feet_font = font.Font(family="Arial",size=15)
feet_label = Label(middle_sub_container,text="Feets",
                       foreground="white",background="#a8cacf",
                       font=feet_font,padx=10,pady=10)
feet_label.place(x=45,y=260)

calculated_feet_value = StringVar(value="Value shown here")
feet_value_font = font.Font(family="Arial",size=15)
feet_value_label = Label(middle_sub_container,textvariable=calculated_feet_value,
                       foreground="black",background="#a8cacf",
                       font=feet_value_font,padx=10,pady=10
                       )
feet_value_label.place(x=320,y=260)

# Separator

separtor6 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor6.place(x=0,y=305,relwidth=10)

#Cubit creation
cubit_font = font.Font(family="Arial",size=15)
cubit_label = Label(middle_sub_container,text="Cubits",
                       foreground="white",background="#a8cacf",
                       font=cubit_font,padx=10,pady=10)
cubit_label.place(x=45,y=310)

calculated_cubit_value = StringVar(value="Value shown here")
cubit_value_font = font.Font(family="Arial",size=15)
cubit_value_label = Label(middle_sub_container,textvariable=calculated_cubit_value,
                       foreground="black",background="#a8cacf",
                       font=cubit_value_font,padx=10,pady=10
                       )
cubit_value_label.place(x=320,y=310)

# Separator

separtor7 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor7.place(x=0,y=355,relwidth=10)


#Nautical mile creation
nautical_mile_font = font.Font(family="Arial",size=15)
nautical_mile_label = Label(middle_sub_container,text="Nautical Miles",
                       foreground="white",background="#a8cacf",
                       font=nautical_mile_font,padx=10,pady=10)
nautical_mile_label.place(x=45,y=360)

calculated_nautical_mile_value = StringVar(value="Value shown here")
nautical_mile_value_font = font.Font(family="Arial",size=15)
nautical_mile_value_label = Label(middle_sub_container,textvariable=calculated_nautical_mile_value,
                       foreground="black",background="#a8cacf",
                       font=nautical_mile_value_font,padx=10,pady=10
                       )

nautical_mile_value_label.place(x=320,y=360)

# Separator

separtor8 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor8.place(x=0,y=405,relwidth=10)



#Forlongs creation
forlongs_font = font.Font(family="Arial",size=15)
forlongs_label = Label(middle_sub_container,text="Forlongs",
                       foreground="white",background="#a8cacf",
                       font=forlongs_font,padx=10,pady=10)
forlongs_label.place(x=45,y=410)

calculated_forlongs_value = StringVar(value="Value shown here")
forlongs_value_font = font.Font(family="Arial",size=15)
forlongs_value_label = Label(middle_sub_container,textvariable=calculated_forlongs_value,
                       foreground="black",background="#a8cacf",
                       font=forlongs_font,padx=10,pady=10
                       )

forlongs_value_label.place(x=320,y=410)

# Separator

separtor9 = ttk.Separator(middle_sub_container,orient='horizontal')

separtor9.place(x=0,y=455,relwidth=10)

#Astronomical Units creation
astronomical_units_font = font.Font(family="Arial",size=15)
astronomical_units_label = Label(middle_sub_container,text="Astronomical Units",
                       foreground="white",background="#a8cacf",
                       font=astronomical_units_font,padx=10,pady=10)
astronomical_units_label.place(x=45,y=460)

calculated_astronomical_units_value = StringVar(value="Value shown here")
astronomical_units_value_font = font.Font(family="Arial",size=15)
astronomical_units_value_label = Label(middle_sub_container,textvariable=calculated_astronomical_units_value,
                       foreground="black",background="#a8cacf",
                       font=astronomical_units_font,padx=10,pady=10
                       )

astronomical_units_value_label.place(x=320,y=460)



# calculate part 
def calculate_values():
    
    enter_value = int(user_value.get())
    
    calculation_part = db.DistanceConverter(enter_value)
    calculated_astronomical_units_value.set(calculation_part.astronomical_units())
    calculated_feet_value.set(calculation_part.feet())
    calculated_cubit_value.set(calculation_part.cubit())
    calculated_forlongs_value.set(calculation_part.forlong())
    calculated_inches_value.set(calculation_part.inches())
    calculated_kilo_value.set(calculation_part.kilometer())
    calculated_mile_value.set(calculation_part.miles())
    calculated_mm_value.set(calculation_part.millimeter())
    calculated_nautical_mile_value.set(calculation_part.nautical_mile())
    calculated_yards_value.set(calculation_part.yards())
    

calculate_button_font = font.Font(family="Arial",size=10,weight='bold')

calculate_button = Button(root,text="Calculate",command=calculate_values,
                          background="red",foreground="white",padx=5,
                          pady=5,activebackground="yellow",width=10,
                          font=calculate_button_font,
                          state="disabled")

calculate_button.place(x=570,y=700)

root.mainloop()