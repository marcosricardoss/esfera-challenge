
### 📘 README.md — Desafio Esfera

Este repositório contém a solução para o **Desafio Esfera**, com foco em processamento de dados em larga escala usando filas assíncronas, Celery, PostgreSQL e Docker.

---

### 🚀 Como executar o projeto

1. **Pré-requisitos**:
   - Ter o **Docker** e **Docker Compose** instalados.

2. **Configurar variáveis de ambiente**:
   - Renomeie o arquivo `example.env` para `.env`.
   - O `.env` contém todas as variáveis de ambiente necessárias para rodar o projeto.

3. **Subir o projeto**:
   - Via Docker Compose:

     ```bash
     docker-compose up
     ```

   - Ou via Make:

     ```bash
     make run
     ```

---

### ✅ Executando os testes

- Usando `pytest` com `coverage`:

  ```bash
  coverage run -m pytest -vv
  ```

- Ou via `make`:

  ```bash
  make tests
  ```

- Também é possível executar os testes diretamente com:

  ```bash
  pytest
  ```

---

### ⚙️ Configuração de processamento com Celery

Este projeto utiliza o **Celery** para o processamento assíncrono de tarefas, com suporte a limitação de taxa (`rate_limit`).

#### 🕐 Exemplo de configuração de `rate_limit`:

```python
@shared_task(rate_limit="5/s")
def create_user_task(...):
    ...
```

- `"5/s"` → processa no máximo 5 tarefas por segundo
- `"100/m"` → processa no máximo 100 tarefas por minuto
- `"10/h"` → processa no máximo 10 tarefas por hora

A variável de ambiente RATE_LIMIT pode ser definida no `.env` para ajustar o limite de taxa.

> **Nota:** para execução local com alto volume (ex: 10.000 registros), comece com valores como `10/s` ou `20/s` e aumente gradualmente de acordo com a capacidade do seu sistema.
