"""
Script para visualizar os dados da taxa CDI.
Lê o arquivo CSV e gera um gráfico usando seaborn.
O nome do gráfico é passado como argumento de linha de comando.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

def ler_dados_csv(arquivo='taxa-cdi.csv'):
    """
    Lê os dados do arquivo CSV contendo as taxas CDI.
    
    Args:
        arquivo: Nome do arquivo CSV (padrão: 'taxa-cdi.csv')
    
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

def gerar_grafico(df, nome_grafico):
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

def main():
    """
    Função principal que executa a leitura e visualização dos dados.
    """
    # Verificar se o nome do gráfico foi passado como argumento
    if len(sys.argv) < 2:
        print("Uso: python visualizacao.py <nome-do-gráfico>")
        print("Exemplo: python visualizacao.py grafico-cdi")
        return 1
    
    # Obter o nome do gráfico do argumento de linha de comando
    nome_grafico = sys.argv[1]
    
    try:
        print("Lendo dados do arquivo CSV...")
        df = ler_dados_csv()
        
        print(f"Total de registros: {len(df)}")
        
        print("Gerando visualização...")
        gerar_grafico(df, nome_grafico)
        
        print("Visualização concluída com sucesso!")
        
    except Exception as e:
        print(f"Erro durante a execução: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
