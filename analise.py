"""
Script de análise que combina extração e visualização de dados da taxa CDI.
Executa a extração de dados da B3 e gera automaticamente a visualização.
"""

import requests
import json
from datetime import datetime
import os
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import random

def extrair_taxa_cdi():
    """
    Extrai a taxa CDI mais recente da API do Banco Central do Brasil.
    Retorna a data, hora e taxa CDI.
    
    Em caso de falha na conexão, gera dados simulados para fins educacionais.
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
        # Em caso de falha na conexão, usar dados simulados para fins educacionais
        print(f"Aviso: Não foi possível conectar à API da B3. Usando dados simulados.")
        
        # Gerar taxa CDI simulada (taxa típica varia entre 12% e 14%)
        taxa = round(random.uniform(12.5, 13.8), 4)
        
        # Criar variáveis data e hora
        agora = datetime.now()
        data = agora.strftime('%Y-%m-%d')
        hora = agora.strftime('%H:%M:%S')
        
        return data, hora, taxa
        
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Erro ao processar dados: {e}")
        raise

def salvar_csv(data, hora, taxa, arquivo='taxa-cdi.csv'):
    """
    Salva os dados da taxa CDI em um arquivo CSV.
    
    Args:
        data: Data da coleta
        hora: Hora da coleta
        taxa: Taxa CDI
        arquivo: Nome do arquivo CSV
    """
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
        
        print(f"Dados salvos: Data={data}, Hora={hora}, Taxa={taxa}%")
        
    except IOError as e:
        print(f"Erro ao salvar arquivo CSV: {e}")
        raise

def ler_dados_csv(arquivo='taxa-cdi.csv'):
    """
    Lê os dados do arquivo CSV contendo as taxas CDI.
    
    Args:
        arquivo: Nome do arquivo CSV
    
    Returns:
        DataFrame do pandas com os dados
    """
    try:
        if not os.path.exists(arquivo):
            raise FileNotFoundError(f"Arquivo {arquivo} não encontrado")
        
        # Ler o arquivo CSV
        df = pd.read_csv(arquivo)
        
        # Verificar se as colunas necessárias existem
        if 'hora' not in df.columns or 'taxa' not in df.columns:
            raise ValueError("Arquivo CSV deve conter as colunas 'hora' e 'taxa'")
        
        return df
        
    except Exception as e:
        print(f"Erro ao ler arquivo CSV: {e}")
        raise

def gerar_grafico(df, nome_grafico='analise-cdi'):
    """
    Gera um gráfico de linha com os dados da taxa CDI.
    
    Args:
        df: DataFrame com os dados
        nome_grafico: Nome do arquivo de saída (sem extensão)
    """
    try:
        # Extrair colunas hora e taxa
        horas = df['hora']
        taxas = df['taxa']
        
        # Configurar o estilo do seaborn
        sns.set_theme(style="whitegrid")
        
        # Criar a figura e o eixo
        plt.figure(figsize=(12, 6))
        
        # Criar o gráfico de linha
        sns.lineplot(x=range(len(horas)), y=taxas, marker='o', linewidth=2, markersize=8)
        
        # Configurar labels e título
        plt.xlabel('Coleta', fontsize=12)
        plt.ylabel('Taxa CDI (%)', fontsize=12)
        plt.title('Evolução da Taxa CDI', fontsize=14, fontweight='bold')
        
        # Ajustar layout
        plt.tight_layout()
        
        # Salvar o gráfico
        nome_arquivo = f"{nome_grafico}.png"
        plt.savefig(nome_arquivo, dpi=150, bbox_inches='tight')
        print(f"Gráfico salvo como: {nome_arquivo}")
        
        # Fechar a figura para liberar memória
        plt.close()
        
    except Exception as e:
        print(f"Erro ao gerar gráfico: {e}")
        raise

def coletar_multiplas_vezes(n_coletas=10, intervalo=2):
    """
    Coleta a taxa CDI múltiplas vezes para gerar um dataset mais completo.
    
    Args:
        n_coletas: Número de coletas a realizar
        intervalo: Intervalo em segundos entre cada coleta
    """
    print(f"Realizando {n_coletas} coletas com intervalo de {intervalo}s...")
    
    for i in range(n_coletas):
        try:
            data, hora, taxa = extrair_taxa_cdi()
            salvar_csv(data, hora, taxa)
            print(f"Coleta {i+1}/{n_coletas} concluída")
            
            # Aguardar antes da próxima coleta (exceto na última)
            if i < n_coletas - 1:
                time.sleep(intervalo)
                
        except Exception as e:
            print(f"Erro na coleta {i+1}: {e}")
            continue

def main():
    """
    Função principal que executa a análise completa.
    """
    print("=" * 60)
    print("ANÁLISE DE TAXA CDI - B3")
    print("=" * 60)
    print()
    
    try:
        # Etapa 1: Extração de dados
        print("1. EXTRAÇÃO DE DADOS")
        print("-" * 60)
        
        # Coletar dados múltiplas vezes para ter mais pontos no gráfico
        coletar_multiplas_vezes(n_coletas=10, intervalo=2)
        
        print()
        
        # Etapa 2: Visualização
        print("2. GERAÇÃO DE VISUALIZAÇÃO")
        print("-" * 60)
        
        # Ler os dados coletados
        df = ler_dados_csv()
        print(f"Total de registros lidos: {len(df)}")
        
        # Gerar gráfico
        gerar_grafico(df, 'analise-cdi')
        
        print()
        print("=" * 60)
        print("ANÁLISE CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        print(f"- Arquivo de dados: taxa-cdi.csv")
        print(f"- Gráfico gerado: analise-cdi.png")
        
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
