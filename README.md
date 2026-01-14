
---

# 🚗 Consultor FIPE Desktop

Uma aplicação Desktop desenvolvida em **Python** e **PyQt6** para consultar a Tabela FIPE (Fundação Instituto de Pesquisas Econômicas) de forma rápida e prática. O sistema permite pesquisar preços médios de veículos no mercado brasileiro.

---

## 📋 Funcionalidades

O aplicativo permite realizar o fluxo completo de consulta da FIPE:

1. **Consultar Marcas:** Lista todas as marcas para Carros, Motos ou Caminhões.
2. **Consultar Modelos:** Exibe os modelos disponíveis de uma marca específica.
3. **Consultar Anos:** Mostra os anos de fabricação disponíveis para um modelo.
4. **Ver Preço:** Exibe a ficha técnica completa (Preço, Mês de Referência, Código Fipe, Combustível, etc).

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3](https://www.python.org/)**: Linguagem principal.
* **[PyQt6](https://pypi.org/project/PyQt6/)**: Framework para a Interface Gráfica (GUI).
* **[HTTPX](https://pypi.org/project/httpx/)**: Biblioteca moderna e rápida para requisições HTTP (API).
* **API FIPE**: Os dados são obtidos através da [API Parallelum](https://deividfortuna.github.io/fipe/).

---

## 📂 Estrutura de Arquivos

Para que o projeto funcione corretamente, organize os arquivos da seguinte maneira em seu computador:

```text
projeto-fipe/
│
├── app.py                  # Arquivo Principal (Execute este arquivo)
├── requirements.txt        # Lista de dependências
│
└── engine/                 # Pasta com a lógica e interface
    ├── mainwindow.ui       # Arquivo do Qt Designer (Opcional para execução)
    ├── fipe_client.py      # Lógica de conexão com a API
    └── mainwindow_qt.py    # Interface gráfica convertida

```
---

## 🚀 Instalação e Execução

Siga os passos abaixo para rodar o projeto na sua máquina:

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.8** (ou superior) instalado.

### 2. Baixar o Projeto

Baixe os arquivos e organize-os conforme a estrutura mostrada acima.

### 3. Criar Ambiente Virtual (Recomendado)

Para evitar conflitos de bibliotecas, crie um ambiente virtual:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

```

### 4. Instalar Dependências

Instale as bibliotecas necessárias listadas no `requirements.txt`:

```bash
pip install -r requirements.txt

```

*Caso não queira usar o arquivo, instale manualmente:* `pip install PyQt6 httpx`

### 5. Executar o Aplicativo

Rode o arquivo principal:

```bash
python app.py

```

---

## 📖 Como Usar

O aplicativo funciona através de **Códigos**. O fluxo de uso é:

1. **Buscar Marca:**
* Selecione o tipo (Carro/Moto/Caminhão) e clique em "Executar".
* Copie o **Código** da marca desejada que aparecerá na lista à direita.


2. **Buscar Modelo:**
* Cole o código da marca no campo "Código da Marca".
* Clique em "Executar" para ver a lista de modelos.
* Copie o **Código** do modelo desejado.


3. **Buscar Ano:**
* Cole o código da marca e do modelo nos respectivos campos.
* Clique em "Executar" e copie o **Código** do ano desejado.


4. **Buscar Preço:**
* Preencha os três códigos (Marca, Modelo e Ano).
* Clique em "Executar" para ver o preço e os detalhes finais.



---

## 🤝 Contribuição

Projeto desenvolvido para fins educacionais. Sinta-se à vontade para enviar sugestões ou melhorias no código!