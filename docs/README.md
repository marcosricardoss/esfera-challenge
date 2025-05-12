# Desafio Técnico – Vaga Python Sênior

## Descrição

O objetivo deste desafio é avaliar sua capacidade de:

- Modelar soluções seguindo boas práticas (SOLID, Clean Code, DDD).
- Trabalhar com persistência de dados relacionais.
- Construir processamento assíncrono baseado em eventos.
- Implementar testes de qualidade (unitários e de integração).
- Tratar falhas de forma resiliente.
- Lidar com grande volume de dados com atenção à performance.

Você terá no máximo **7 dias** para entregar a solução.

---

## Escopo do Desafio

### 1. Leitura de Dados

Ler um arquivo CSV contendo informações de usuários e seus endereços.

**Exemplo de CSV:**

```csv
user_id,name,email,created_at,address_id,street,city,state,zipcode,country
1,John Doe,john@example.com,2024-01-01T10:00:00,101,123 Main St,New York,NY,10001,USA
2,Jane Smith,jane@example.com,2024-01-02T11:30:00,102,456 Market St,San Francisco,CA,94105,USA
```

> Será fornecido um CSV com **mais de 10.000 registros** para testes.

---

### 2. Modelagem de Banco de Dados

Criar a modelagem com pelo menos duas tabelas:

- `users`
- `addresses`

**Relacionamento:**  
Cada usuário possui um endereço único (1:1).

> Utilizar ORM (preferencialmente SQLAlchemy).

---

### 3. Persistência de Dados

- Ler o CSV e persistir os dados de forma eficiente.
- Buscar otimizar o carregamento para volumes altos.

---

### 4. Geração de Eventos

- Após persistir um novo usuário, gerar um evento `UserCreated`.
- O evento deve conter o ID do usuário e o timestamp.

---

### 5. Processamento Assíncrono

- Criar um worker para consumir `UserCreated`.
- Simular envio de e-mail de boas-vindas (logar).
- Registrar o evento na tabela `user_events` (auditoria).

---

## Requisitos Técnicos

- Python 3.10+
- FastAPI (opcional)
- SQLAlchemy
- Celery ou equivalente
- RabbitMQ ou Redis
- Banco relacional (PostgreSQL ou SQLite)
- Boas práticas: SOLID, Clean Code
- Tratamento de erros
- Testes unitários e de integração (preferencialmente com Pytest)

---

## Critérios de Avaliação

- Qualidade e clareza do código
- Estrutura do projeto
- Uso de padrões e boas práticas
- Eficiência no processamento de grandes volumes
- Resiliência e logs adequados
- Qualidade dos testes

---

## Entrega

- Disponibilizar em repositório Git.
- README com instruções de execução.
- Explicação das escolhas técnicas.