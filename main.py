import csv
import pandas as pd
from MetaInvoiceToCsv.parser import getWabas
from MetaInvoiceToCsv.extractor import getText
from MetaInvoiceToCsv.transformer import limpar_waba_dataframe


pdf_file = 'data/pdf/creditos_set25.pdf'

texto = getText(pdf_file)
df_base = getWabas(texto)
wabas = limpar_waba_dataframe(df_base)


wabas.to_csv('output/Invoice_set25.csv', index=False, quotechar='"', quoting=csv.QUOTE_ALL)
