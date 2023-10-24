# Readme: API de Gerenciamento de Hotel com Flask

Este repositório contém um código Python desenvolvido como parte de um curso sobre a criação de uma API com Flask. A API tem como objetivo oferecer um sistema de gerenciamento de hotéis, demonstrando o uso dos métodos HTTP GET, POST, PUT e DELETE.

## Descrição do Código

O código se concentra em criar uma API de gerenciamento de hotéis usando Python e o framework Flask. O sistema é construído com o intuito de mostrar os conceitos básicos de operações CRUD (Create, Read, Update, Delete) em uma aplicação web. Aqui estão os principais componentes e funcionalidades do código:

### Modelagem de Hotel

O código inclui um modelo de hotel representado pela classe `HotelModel`. Essa classe descreve a estrutura de um hotel, incluindo propriedades como nome, número de estrelas, diária e cidade.

### Recursos da API

O código define dois recursos principais:

1. **Hoteis (Hotels)**: Este recurso permite obter a lista de todos os hotéis disponíveis. O método `GET` é utilizado para isso.

2. **Hotel**: Este recurso permite acessar informações detalhadas sobre um hotel específico, bem como adicionar, atualizar e excluir hotéis. Os métodos `GET`, `POST`, `PUT` e `DELETE` são usados para manipular informações de hotéis individuais.

### Exemplo de Dados

O código inclui um exemplo de dados representando uma lista de hotéis, cada um com um ID, nome, número de estrelas, diária e cidade.

## Como Usar

Para usar este código, siga estas etapas:

1. **Clonar o Repositório**: Clone este repositório em sua máquina local.

2. **Configuração do Ambiente**: Certifique-se de que você tenha Python e Flask instalados em sua máquina.

3. **Executar o Código**: Execute o código em sua máquina. Certifique-se de que o servidor Flask esteja em execução.

4. **Interagir com a API**: Use uma ferramenta como Postman, curl ou até mesmo seu navegador para interagir com os endpoints da API. Você pode realizar operações como listar hotéis, adicionar um novo hotel, atualizar informações de hotel e excluir hotéis.

## Endpoints da API

Aqui estão os principais endpoints da API e os métodos HTTP associados a eles:

- **Obter a lista de todos os hotéis** (Método: GET): `/hoteis`
- **Obter informações detalhadas de um hotel específico** (Método: GET): `/hotel/<hotel_id>`
- **Adicionar um novo hotel** (Método: POST): `/hotel/<hotel_id>`
- **Atualizar informações de um hotel existente** (Método: PUT): `/hotel/<hotel_id>`
- **Excluir um hotel** (Método: DELETE): `/hotel/<hotel_id>`

## Contribuições

Este é um projeto de demonstração destinado a fins de aprendizado. Contribuições são bem-vindas se você deseja expandir ou melhorar este código.

## Autor

Este código foi criado como parte de um curso de Flask API por **João Pedro Araujo Queiroz Barbosa**. 

