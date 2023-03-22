import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    # prepare the dataframe
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # prepare the pdf
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # prepare data for header
    filename = Path(filepath).stem
    invoice_nr, i_date = filename.split("-")

    # pdf header text
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {i_date}", ln=1)


    # pdf body text = table

    # pdf footer text

    pdf.output(f"PDFs/{filename}.pdf")