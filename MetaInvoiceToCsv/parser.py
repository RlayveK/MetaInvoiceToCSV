import re

def extrair_id_sub(subtexto):
    match = re.search(r'\d+', subtexto)
    return match.group(0) if match else ''
import re

def encontrarValor(id, inVoice):

    
    pos = inVoice.find(str(id))
                
    if pos > -1:
        pos_usd = inVoice.find("USD", pos+1)
                    
        pos_valor = inVoice.rfind("$", 0, pos_usd)
                          
        if pos_usd != -1 and pos_valor != -1:
                    preco = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d{2})?',inVoice[ pos_valor+1: pos_usd].strip())
        else:
            preco = 0

        return preco 

def getWabas(texto):

    wabaEncontrados = []    
    pos = 0
    waba = ""
    pos_bar = 0
    tirar='''Account summary
Product Price type QuantityDiscount 
percentageTotal
'''

    first_name = input("Primeiro nome: ")
    ultimo = "121266107581982"

    pos_ultimo = texto.find(ultimo)

    while pos < pos_ultimo - 10:
        if pos == 0:
            # Primeira ocorrência
            pos = texto.find(first_name)
            pos_bar = texto.find("/", pos)
            nome = texto[pos:pos_bar].strip()
            subtexto = texto[pos_bar + 1:]
            waba = extrair_id_sub(subtexto)
        else:
            pos_usd = texto.find("USD", pos + 1)
            pos_bar = texto.find("/", pos_usd)
            nome = texto[pos_usd + 3:pos_bar].strip()
            subtexto = texto[pos_bar + 1:]
            waba = extrair_id_sub(subtexto)
            pos = pos_bar + len(waba) + 1
        
        nome = nome.strip().replace(tirar, '').strip()
        wabaEncontrados.append((nome, waba, encontrarValor(waba, subtexto)))
    return wabaEncontrados

