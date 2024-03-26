from fpdf import FPDF

# orientation where "P" = portrait, could be L for landscape, FPDF(orientation="P", unit="mm", format="A4")
# all text must have specified font, size (bit not mm) pdf.set_font pdf.set_font('helvetica', 'B', 16), B = bold, 16 size, and hel.. font
# cell will be the text container
#output shirtificate.pdf
#Portrait |  A4, which is 210mm wide by 297mm tall |  top of the PDF should say “CS50 Shirtificate” as text, centered horizontally | shirt’s image should be centered horizontally.


def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page()
    pdf.label(name)
    pdf.output("shirtificate.pdf")



class PDF(FPDF):
        def header(self):
            self.set_font('helvetica','B',65)
            self.cell(0, 25, 'CS50 Shirtificate', align= 'C', new_x="LMARGIN", new_y="NEXT")
        
        def label(self,name):
             self.name = name
             self.label = f"{name} took CS50"
             

        def footer(self):
            self.image("shirtificate.png", x = 'C', y = 50)
            self.set_text_color(255,255,255)
            self.set_font('helvetica','B',25)
            self.cell(0,190,self.label, align= 'C')

    
if __name__ == "__main__":
    main()




