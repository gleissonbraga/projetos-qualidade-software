# Testes Funcionais vs Estruturais – LocalEats

## 1. Funcionalidade escolhida: Busca de restaurantes

### O que a funcionalidade faz
A funcionalidade de busca permite que o usuário encontre restaurantes com base em critérios como nome, categoria (ex: pizza, sushi), localização ou avaliações.

### O que o usuário espera
- Encontrar restaurantes relevantes ao que foi pesquisado
- Resultados rápidos e corretos
- Possibilidade de buscar com termos parciais
- Não receber resultados errados ou vazios sem motivo

---

## 2. Testes Caixa-Preta (Visão do Usuário)

### Entradas possíveis
- Nome do restaurante (ex: "Pizza")
- Categoria (ex: "Japonesa")
- Campo vazio
- Texto inexistente (ex: "asdfgh")
- Caracteres especiais (ex: "@#$$%")
- Busca com espaços (ex: "   pizza   ")

### Comportamentos esperados
- Retornar restaurantes relacionados ao termo buscado
- Mostrar lista vazia quando não houver resultados
- Ignorar espaços extras
- Tratar letras maiúsculas/minúsculas da mesma forma

### Situações de erro
- Não retornar nenhum resultado mesmo existindo restaurantes
- Retornar restaurantes que não correspondem à busca
- Travar ou demorar muito para responder
- Exibir erro ao inserir caracteres especiais

---

## 3. Testes Caixa-Branca (Visão do Sistema)

### Possível implementação
A busca pode estar implementada com:
- Filtro em banco de dados (`LIKE`, `ILIKE`)
- Normalização de texto (lowercase, trim)
- Validação de entrada
- Regras de relevância (ordenação por avaliação, distância, etc.)

### Estruturas lógicas possíveis
- `if (searchTerm === "")`
- `if (result.length === 0)`
- `if (containsSpecialCharacters)`
- Validação de tamanho mínimo da busca
- Tratamento de exceções do banco

### Situações que precisam ser testadas
- Entrada vazia
- Entrada com espaços
- Entrada com caracteres especiais
- Retorno com lista vazia
- Erro na consulta ao banco
- Ordenação correta dos resultados
- Performance da busca

---

## 4. Comparação entre as abordagens

### Diferença principal
- **Caixa-preta:** testa o comportamento da funcionalidade sem conhecer o código
- **Caixa-branca:** testa a lógica interna e os caminhos do código

### Tipos de problemas encontrados

**Caixa-preta:**
- Resultados incorretos
- Problemas de usabilidade
- Falhas visíveis ao usuário

**Caixa-branca:**
- Erros em condições (ifs)
- Falhas em validações
- Caminhos de código não testados
- Problemas de performance

---

## 5. Reflexão no contexto do LocalEats

### Qual abordagem é mais útil?
Ambas são importantes, mas para os problemas atuais do sistema (resultados incorretos e comportamentos inesperados), a combinação das duas abordagens é essencial.

- A caixa-preta ajuda a identificar que existe um problema
- A caixa-branca ajuda a entender por que o problema acontece

### Apenas uma abordagem seria suficiente?
Não.

Usar apenas caixa-preta pode identificar erros, mas não suas causas.
Usar apenas caixa-branca pode garantir código correto, mas não a experiência do usuário.

### Justificativa
No contexto do LocalEats, onde há inconsistências e falhas específicas:
- A caixa-preta garante que o sistema funcione do ponto de vista do usuário
- A caixa-branca garante que a lógica interna esteja correta

Portanto, o uso combinado das duas abordagens é necessário para garantir qualidade real no sistema.

---

## Conclusão

A combinação de testes funcionais e estruturais permite uma cobertura mais completa do sistema, garantindo tanto a experiência do usuário quanto a qualidade do código interno. Essa abordagem é fundamental para sistemas como o LocalEats, que apresentam problemas reais em produção.