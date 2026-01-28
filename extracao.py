"""
Script para extrair a taxa CDI do Banco Central do Brasil.
Salva os dados em um arquivo CSV com data, hora e taxa.
"""

import requests
import json
from datetime import datetime
import os
import csv

def extrair_taxa_cdi():
    """
    Extrai a taxa CDI mais recente da API do Banco Central do Brasil.
    Retorna a data, hora e taxa CDI.
    """
    try:
        # URL da API do Banco Central para série histórica do CDI (código 12)
        url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados/ultimos/1?formato=json'
        
        # Fazendo a requisição HTTP
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Convertendo a resposta para JSON
        dados = response.json()
        
        if dados and len(dados) > 0:
            # Pegar o último registro
            ultimo_registro = dados[-1]
            taxa = float(ultimo_registro['valor'])
            
            # Criar variáveis data e hora
            agora = datetime.now()
            data = agora.strftime('%Y-%m-%d')
            hora = agora.strftime('%H:%M:%S')
            
            return data, hora, taxa
        else:
            raise ValueError("Nenhum dado CDI encontrado na API")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer requisição: {e}")
        raise
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Erro ao processar dados: {e}")
        raise

def salvar_csv(data, hora, taxa):
    """
    Salva os dados da taxa CDI em um arquivo CSV.
    
    Args:
        data: Data da coleta
        hora: Hora da coleta
        taxa: Taxa CDI
    """
    arquivo = 'taxa-cdi.csv'
    
    # Verifica se o arquivo já existe para determinar se precisa escrever o cabeçalho
    arquivo_existe = os.path.exists(arquivo)
    
    try:
        with open(arquivo, 'a', newline='', encoding='utf-8') as csvfile:
            campos = ['data', 'hora', 'taxa']
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            
            # Escreve cabeçalho apenas se o arquivo não existir
            if not arquivo_existe:
                writer.writeheader()
            
            # Escreve os dados
            writer.writerow({
                'data': data,
                'hora': hora,
                'taxa': taxa
            })
        
        print(f"Dados salvos com sucesso: Data={data}, Hora={hora}, Taxa={taxa}%")
        
    except IOError as e:
        print(f"Erro ao salvar arquivo CSV: {e}")
        raise

def main():
    """
    Função principal que executa a extração e salvamento dos dados.
    """
    print("Iniciando extração da taxa CDI...")
    
    try:
        # Extrair dados
        data, hora, taxa = extrair_taxa_cdi()
        
        # Salvar no CSV
        salvar_csv(data, hora, taxa)
        
        print("Extração concluída com sucesso!")
        
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
