name = input("enter name:")
number = int(input("enter mobile number:"))
age = input("enter your age:")
location = input("enter your location:")
line = name + ':' + str(number) + ':' + str(age) + ':' + location
option = input("Export to A) PDF B) Text \n")

from fpdf import FPDF


def exporttoPdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=line, ln=1, align="C")
    pdf.output(name + ".pdf")
    print("successfully created pdf file")
    pass


def exporttoText():
    f = open(name + ".txt", 'w+')
    f.write(line)
    print("successfully created text file")
    f.close()
    pass


if option == "A" or option == "a":
    exporttoPdf()
elif option == "B" or option == "b":
    exporttoText()
else:
    print("Invalid entry")
