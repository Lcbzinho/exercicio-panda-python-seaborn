# Exercício Pandas, Python e Seaborn

Este projeto contém três scripts Python para extração, visualização e análise de dados da taxa CDI (Certificado de Depósito Interbancário) do Banco Central do Brasil.

## 📋 Descrição

O projeto é composto por três scripts principais:

1. **extracao.py** - Extrai a taxa CDI da API do Banco Central e salva em CSV
2. **visualizacao.py** - Gera visualizações gráficas dos dados coletados
3. **analise.py** - Combina extração e visualização em um único processo automatizado

## 🚀 Instalação

### Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalando as dependências

```bash
pip install -r requirements.txt
```

As dependências incluem:
- `pandas` - Manipulação e análise de dados
- `seaborn` - Visualização estatística de dados
- `requests` - Requisições HTTP
- `matplotlib` - Biblioteca base para visualizações

## 📊 Uso

### 1. Script de Extração (`extracao.py`)

Extrai a taxa CDI atual e salva no arquivo `taxa-cdi.csv`:

```bash
python extracao.py
```

O script:
- Conecta-se à API do Banco Central do Brasil
- Captura a taxa CDI mais recente
- Salva os dados com data, hora e taxa no formato CSV
- Em caso de falha na API, usa dados simulados para fins educacionais

**Formato do CSV gerado:**
```csv
data,hora,taxa
2026-01-28,10:30:15,13.75
```

### 2. Script de Visualização (`visualizacao.py`)

Lê o arquivo CSV e gera um gráfico em formato PNG:

```bash
python visualizacao.py <nome-do-gráfico>
```

**Exemplo:**
```bash
python visualizacao.py grafico-cdi
```

Isso irá gerar o arquivo `grafico-cdi.png` com a visualização dos dados.

O script:
- Lê o arquivo `taxa-cdi.csv`
- Extrai as colunas de hora e taxa
- Cria um gráfico de linha mostrando a evolução da taxa CDI
- Salva a imagem no formato PNG com o nome especificado

### 3. Script de Análise Completa (`analise.py`)

Executa todo o processo de extração e visualização automaticamente:

```bash
python analise.py
```

O script:
- Realiza 10 coletas da taxa CDI com intervalo de 2 segundos
- Salva todos os dados no arquivo `taxa-cdi.csv`
- Gera automaticamente o gráfico `analise-cdi.png`
- Exibe um resumo completo da análise

## 📁 Estrutura do Projeto

```
exercicio-panda-python-seaborn/
├── README.md              # Este arquivo
├── requirements.txt       # Dependências do projeto
├── .gitignore            # Arquivos ignorados pelo Git
├── extracao.py           # Script de extração de dados
├── visualizacao.py       # Script de visualização
└── analise.py            # Script de análise completa
```

## 🔄 Fluxo de Trabalho Típico

### Opção 1: Execução passo a passo

```bash
# 1. Coletar dados (executar múltiplas vezes para mais pontos)
python extracao.py
python extracao.py
python extracao.py

# 2. Gerar visualização
python visualizacao.py minha-analise
```

### Opção 2: Execução automatizada

```bash
# Executa tudo de uma vez
python analise.py
```

## 📈 Exemplo de Saída

Após executar os scripts, você terá:

1. **taxa-cdi.csv** - Arquivo com os dados coletados
2. **[nome].png** - Gráfico visual da evolução da taxa CDI

O gráfico mostra:
- Eixo X: Número da coleta
- Eixo Y: Taxa CDI (%)
- Linha com marcadores mostrando a evolução temporal

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem de programação
- **Pandas** - Análise e manipulação de dados tabulares
- **Seaborn** - Visualização estatística de alta qualidade
- **Matplotlib** - Backend para renderização de gráficos
- **Requests** - Cliente HTTP para consumir APIs

## 🔒 Tratamento de Erros

Os scripts incluem tratamento robusto de erros:

- **Falha na API**: Usa dados simulados para fins educacionais
- **Arquivo não encontrado**: Mensagem clara de erro
- **Argumentos faltantes**: Instruções de uso
- **Problemas de rede**: Timeout e retry configurados

## 📝 Observações

- Os arquivos CSV e PNG gerados são automaticamente ignorados pelo Git (configurado em `.gitignore`)
- A API do Banco Central é pública e não requer autenticação
- Em ambientes sem acesso à internet, o script usa dados simulados automaticamente
- Os dados simulados seguem padrões realistas de taxa CDI (12.5% - 13.8%)

## 👨‍🎓 Projeto Educacional

Este projeto foi desenvolvido como exercício prático para aprendizado de:
- Consumo de APIs REST
- Manipulação de dados com Pandas
- Visualização de dados com Seaborn
- Boas práticas de programação Python
- Tratamento de erros e exceções
- Organização de projetos Python

## 📄 Licença

Este é um projeto educacional de código aberto.

## 🙋‍♂️ Autor

Desenvolvido como parte do exercício de análise de dados com Python, Pandas e Seaborn.