import cv2 as cv
from tkinter import *
from tkinter.filedialog import *
import os


root = Tk()
root.title("Color Spaces Converter")
root.geometry("325x650")


#labels
set_Directory=Label(root,text="Select Directory")
set_Directory.grid(row=1,column=0,padx=25,pady=20)

file_name=Label(root,text="Save as(FileName): ")
file_name.grid(row=2,column=0,padx=25,pady=20)

file_format=Label(root,text="Save as(File Extension): ")
file_format.grid(row=3,column=0)


convert_to_gray=Label(root,text="Convert to Gray: ")
convert_to_gray.grid(row=4,column=0)

convert_to_HSV=Label(root,text="Convert to HSV: ")
convert_to_HSV.grid(row=5,column=0)

convert_to_LAB=Label(root,text="Convert to LAB: ")
convert_to_LAB.grid(row=6,column=0)

convert_to_RGB=Label(root,text="Convert to RGB: ")
convert_to_RGB.grid(row=7,column=0)

convert_from_HSV_to_BGR=Label(root,text="Convert from HSV to BGR: ")
convert_from_HSV_to_BGR.grid(row=8,column=0)

convert_from_LAB_to_BGR=Label(root,text="Convert from LAB to BGR: ")
convert_from_LAB_to_BGR.grid(row=9,column=0)


#buttons
set_Directory_Button=Button(root,text="Locate Directory",fg="white",bg="gray",padx=40,pady=5,command=lambda:get_Directory())
set_Directory_Button.grid(row=1,column=1)

convert_to_gray_button=Button(root,text="Locate Image",fg="white",bg="gray",padx=40,pady=20,command=lambda:color_convert('Gray'))
convert_to_gray_button.grid(row=4,column=1)

convert_to_HSV_button=Button(root,text="Locate Image",fg="white",bg="gray",padx=40,pady=20,command=lambda:color_convert('HSV'))
convert_to_HSV_button.grid(row=5,column=1)

convert_to_LAB_button=Button(root,text="Locate Image",fg="white",bg="gray",padx=40,pady=20,command=lambda:color_convert('LAB'))
convert_to_LAB_button.grid(row=6,column=1)

convert_to_RGB_button=Button(root,text="Locate Image",fg="white",bg="gray",padx=40,pady=20,command=lambda:color_convert('RGB'))
convert_to_RGB_button.grid(row=7,column=1)

convert_from_HSV_to_BGR_button=Button(root,text="Locate Image",fg="white",bg="gray",padx=40,pady=20,command=lambda:color_convert('HSV_to_BGR'))
convert_from_HSV_to_BGR_button.grid(row=8,column=1)

convert_from_LAB_to_BGR_button=Button(root,text="Locate Image",fg="white",bg="gray",padx=40,pady=20,command=lambda:color_convert('LAB_to_BGR'))
convert_from_LAB_to_BGR_button.grid(row=9,column=1)

#optionmenu
default_variable=StringVar(root)
default_variable.set("File Format")
file_format_option_menu=OptionMenu(root,default_variable,".PNG",".JPEG")
file_format_option_menu.grid(row=3,column=1)


#text
software_message=Text(width=40,height=5,bg="white",fg="black")
software_message.grid(row=0,column=0,columnspan=3)

input_filename=Text(width=20,height=0.5,bg="white",fg="black")
input_filename.grid(row=2,column=1,columnspan=3)


#class
software_message.insert(END, "Select Directory to save files in")
save_as=""
def get_Directory():
    global save_as
    ask_Directory=askdirectory(title='Select Directory')
    save_as=ask_Directory
    software_message.delete("1.0", "end")
    software_message.insert(END,"Path succesfully loaded\n")
    software_message.insert(END,"Input filename, file extension, and preferred color")

class color_Conversion:
    def initialize(self):
        open_image = askopenfilenames()
        self.img = cv.imread(open_image[0])
    def to_Gray(self):
        self.converted_image=cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)

    def to_HSV(self):
        self.converted_image = cv.cvtColor(self.img, cv.COLOR_BGR2HSV)

    def to_LAB(self):
        self.converted_image=cv.cvtColor(self.img,cv.COLOR_BGR2LAB)

    def to_RGB(self):
        self.converted_image=cv.cvtColor(self.img,cv.COLOR_BGR2RGB)

    def to_HSV_BGR(self):
        self.converted_image=cv.cvtColor(self.img,cv.COLOR_HSV2BGR)

    def to_LAB_BGR(self):
        self.converted_image = cv.cvtColor(self.img, cv.COLOR_LAB2BGR)

    def saving(self):
        software_message.delete("1.0", "end")
        filename = str(input_filename.get("1.0", 'end-1c')) + default_variable.get()
        file_path=os.path.join(save_as, filename)
        print(file_path)
        print(os.path.exists(file_path))
        if os.path.exists(file_path) == True:
            software_message.insert(END,"Filename Already Exists!")
            return
        else:
            cv.imshow('Converted Image',self.converted_image)
            cv.imwrite(file_path, self.converted_image)
            software_message.insert(END, "Successfuly saved in " + save_as + " as " + filename)



def color_convert(color_choice):
    if default_variable.get() == "File Format":
        software_message.delete("1.0", "end")
        software_message.insert(END, "Input File Extension")
    else:
        turn_color = color_Conversion()

        if color_choice == 'Gray':
            turn_color.initialize()
            turn_color.to_Gray()
            turn_color.saving()

        elif color_choice == 'HSV':
            turn_color.initialize()
            turn_color.to_HSV()
            turn_color.saving()

        elif color_choice == 'LAB':
            turn_color.initialize()
            turn_color.to_LAB()
            turn_color.saving()

        elif color_choice == 'RGB':
            turn_color.initialize()
            turn_color.to_RGB()
            turn_color.saving()

        elif color_choice == 'HSV_to_BGR':
            turn_color.initialize()
            turn_color.to_HSV_BGR()
            turn_color.saving()

        elif color_choice == 'LAB_to_BGR':
            turn_color.initialize()
            turn_color.to_LAB_BGR()
            turn_color.saving()
        else:
            return 0

cv.waitKey(0)
root.mainloop()