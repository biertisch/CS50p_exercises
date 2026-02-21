from fpdf import FPDF


class PDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")

    def shirtify(self, name):
        self.add_page()

        # Title
        self.set_font("helvetica", style="B", size=42)
        self.cell(0, 30, "CS50 Shirtifcate", align="C")

        # Image
        self.image("shirtificate.png", x=10, y=55, w=190)

        # White text
        self.set_xy(10, 100)
        self.set_font("helvetica", size=20)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, f"{name} took CS50", align="C")


def main():
    pdf = PDF()
    pdf.shirtify(input("Name: "))
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
