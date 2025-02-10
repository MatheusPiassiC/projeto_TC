# Este arquivo contém a documentação do projeto, incluindo instruções de configuração, exemplos de uso da API e limitações.

## API de Manipulação de Autômatos

Este projeto implementa uma API RESTful para manipular e analisar autômatos utilizando a biblioteca Automata e o framework FastAPI em Python.

### Estrutura do Projeto

```
api-automatos
├── src
│   ├── main.py
│   ├── routers
│   │   ├── afd.py
│   │   ├── automato_pilha.py
│   │   └── maquina_turing.py
│   ├── models
│   │   └── automato.py
│   ├── services
│   │   ├── afd_service.py
│   │   ├── automato_pilha_service.py
│   │   └── maquina_turing_service.py
│   └── utils
│       └── visualizacao.py
├── requirements.txt
└── README.md
```

### Instruções de Configuração

1. **Instalar Dependências**: Utilize o comando `pip install -r requirements.txt` para instalar os pacotes necessários.

2. **Executar a API**: Inicie a aplicação FastAPI executando `uvicorn src.main:app --reload`. Isso iniciará o servidor e permitirá que você acesse a API.

3. **Acessar a Documentação**: Abra seu navegador e vá para `http://127.0.0.1:8000/docs` para acessar a interface Swagger, onde você pode testar os endpoints interativamente.

### Exemplos de Uso da API

- **Criar um Autômato**: Utilize o endpoint correspondente para criar um autômato (AFD, autômato com pilha ou máquina de Turing) fornecendo os dados necessários no formato JSON.

- **Recuperar Informações**: Acesse os endpoints para obter informações sobre os autômatos criados, como estados, transições e estados de aceitação.

- **Testar Aceitação de Strings**: Envie strings para verificar se são aceitas pelos autômatos.

- **Visualizar Autômatos**: Utilize os endpoints de visualização para gerar representações gráficas dos autômatos em formatos como PNG ou SVG.

### Limitações

- O sistema não utiliza um banco de dados, portanto, os autômatos são armazenados em memória e serão perdidos ao reiniciar a aplicação.
- A validação de entradas é básica e pode não cobrir todos os casos de erro.

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorias e correções.

### Licença

Este projeto está licenciado sob a MIT License.