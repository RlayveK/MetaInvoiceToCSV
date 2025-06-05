import pandas as pd

def limpar_waba_dataframe(wabas_raw):
    df = pd.DataFrame(wabas_raw, columns=["Nome", "Waba", "Valor"])
    
    # Extrair valor se for lista
    df['Valor'] = df['Valor'].apply(lambda x: x[0] if isinstance(x, list) and len(x) > 0 else None)
    
    # Converter string para float, removendo vírgulas
    df['Valor'] = df['Valor'].apply(lambda x: float(x.replace(',', '')) if isinstance(x, str) else x)
    
    return df