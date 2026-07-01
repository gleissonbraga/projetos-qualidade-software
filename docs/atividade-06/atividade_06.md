# Aula 9 – Testes Unitários e TDD
**Unidade Curricular:** Qualidade de Software  
**Professor:** Luciano Zanuz  
**Instituição:** Centro Universitário Senac-RS (Unisenac)  

---

## 👥 Integrantes
* **Integrante 1:** [Gleisson Braga]
* **Integrante 2:** [Jonatas Davi]
* **Integrante 3:** [Natalia Morandi]

---

## 📁 Estrutura do Projeto
```text
.
├── functions/
│   ├── pedido.js
│   ├── desconto.js
│   └── entrega.js
└── tests/
    ├── pedido.test.js
    ├── desconto.test.js
    └── entrega.test.js

 ---

## 🔹 1. Funcionalidades Escolhidas

Cada integrante ficou responsável por uma regra de negócio isolada do sistema LocalEats.

### 👤 Integrante 1 – Cálculo do total do pedido com valor mínimo
* **Arquivo da implementação:** `/functions/pedido.js`
* **Arquivo de testes:** `/tests/pedido.test.js`
* **Descrição:** Soma os valores dos itens do pedido e valida se o total atinge o valor mínimo exigido.
* **Regras de negócio:**
  * Total = soma dos itens.
  * Se total < valor mínimo ➔ Erro.
  * Caso contrário ➔ Pedido válido.

### 👤 Integrante 2 – Aplicação de desconto percentual
* **Arquivo da implementação:** `/functions/desconto.js`
* **Arquivo de testes:** `/tests/desconto.test.js`
* **Descrição:** Aplica um desconto percentual calculado sobre o valor total do pedido.
* **Regras de negócio:**
  * Desconto deve estar entre 0% e 100%.
  * Valor final não pode ser negativo.

### 👤 Integrante 3 – Cálculo de taxa de entrega
* **Arquivo da implementação:** `/functions/entrega.js`
* **Arquivo de testes:** `/tests/entrega.test.js`
* **Descrição:** Calcula o valor cobrado pela entrega do pedido com base na distância em quilômetros.
* **Regras de negócio:**
  * Distância até 3 km ➔ Taxa fixa.
  * Acima disso ➔ Taxa proporcional por km excedente.
  * Distância negativa ➔ Erro.

---

## 🔹 2. Testes Unitários e Ciclo TDD

### 🧪 Integrante 1 – Testes e Implementação (`pedido`)

#### Teste 1 – Sucesso: Valor acima do mínimo (Happy Path)
* **Nome descritivo:** `Deve calcular corretamente o total do pedido quando valor minimo e atingido`
* **Cenário testado:** Valida se a função retorna corretamente o total do pedido quando a soma dos itens supera o valor mínimo.
* **Dados de entrada:** `itens = [{ preco: 40.0 }, { preco: 20.0 }]`, `valorMinimo = 35.0`
* **Resultado esperado:** Retornar `60.0` sem gerar erros.
* **Código do teste:**
```javascript
const { calcularTotalPedido } = require('../functions/pedido');

test('Deve calcular corretamente o total do pedido quando valor minimo e atingido', () => {
    const itens = [{ preco: 40.0 }, { preco: 20.0 }];
    const valorMinimo = 35.0;
    const resultado = calcularTotalPedido(itens, valorMinimo);
    expect(resultado).toBe(60.0);
});
```

#### Teste 2 – Sucesso: Valor exatamente igual ao mínimo (Happy Path)
* **Nome descritivo:** `Deve validar o pedido quando o total for exatamente igual ao valor minimo`
* **Cenário testado:** Verifica o comportamento na borda de sucesso do valor mínimo.
* **Dados de entrada:** `itens = [{ preco: 15.0 }, { preco: 20.0 }]`, `valorMinimo = 35.0`
* **Resultado esperado:** Retornar `35.0`.

#### Teste 3 – Erro: Valor abaixo do mínimo (Edge Case)
* **Nome descritivo:** `Deve lancar erro quando o total do pedido for menor que o valor minimo`
* **Cenário testado:** Garante o bloqueio de pedidos com valor insuficiente.
* **Dados de entrada:** `itens = [{ preco: 12.0 }]`, `valorMinimo = 15.0`
* **Resultado esperado:** Lançar uma exceção `Error("Valor mínimo do pedido não atingido")`.

#### Aplicação do TDD & Refatoração
* **Red:** O teste foi escrito simulando chamadas à função antes de sua criação, resultando em falha por módulo inexistente.
* **Green:** Implementou-se um laço acumulador estrutural simples para satisfazer o resultado matemático dos asserts.
* **Refactor:** O laço imperativo foi substituído pelo método funcional nativo `.reduce()`, eliminando variáveis mutáveis temporárias e limpando a estrutura.
```javascript
function calcularTotalPedido(itens, valorMinimo) {
    const total = itens.reduce((soma, item) => soma + item.preco, 0);
    if (total < valorMinimo) {
        throw new Error("Valor mínimo do pedido não atingido");
    }
    return total;
}
module.exports = { calcularTotalPedido };
```

---

### 🧪 Integrante 2 – Testes e Implementação (`desconto`)

#### Teste 1 – Sucesso: Aplicação de desconto padrão (Happy Path)
* **Nome descritivo:** `Deve aplicar desconto percentual valido corretamente`
* **Cenário testado:** Verifica o cálculo da redução do valor total com base em uma porcentagem válida.
* **Dados de entrada:** `valorTotal = 100.0`, `percentual = 15`
* **Resultado esperado:** Retornar `85.0`.
* **Código do teste:**
```javascript
const { aplicarDesconto } = require('../functions/desconto');

test('Deve aplicar desconto percentual valido corretamente', () => {
    const resultado = aplicarDesconto(100.0, 15);
    expect(resultado).toBe(85.0);
});
```

#### Teste 2 – Sucesso: Desconto limite de 100% (Happy Path / Edge)
* **Nome descritivo:** `Deve permitir zerar o valor do pedido com desconto de 100 por cento`
* **Cenário testado:** Avalia o limite comercial máximo permitido para a aplicação de cupons.
* **Dados de entrada:** `valorTotal = 50.0`, `percentual = 100`
* **Resultado esperado:** Retornar `0.0`.

#### Teste 3 – Erro: Percentual acima do limite (Error Case)
* **Nome descritivo:** `Deve lancar erro se o percentual de desconto for maior que 100`
* **Cenário testado:** Protege o sistema contra cupons configurados de forma errônea ou abusiva.
* **Dados de entrada:** `valorTotal = 80.0`, `percentual = 125`
* **Resultado esperado:** Lançar uma exceção `Error("Percentual de desconto inválido")`.

#### Aplicação do TDD & Refatoração
* **Red:** Escrita das validações condicionais esperando que o interpretador rejeitasse as entradas.
* **Green:** Adicionou-se uma validação rápida por meio de cláusulas de barreira imediatas.
* **Refactor:** Centralizaram-se as regras matemáticas de dedução e blindou-se o retorno usando operador ternário para evitar saídas negativas.
```javascript
function aplicarDesconto(valorTotal, percentual) {
    if (percentual < 0 || percentual > 100) {
        throw new Error("Percentual de desconto inválido");
    }
    const valorFinal = valorTotal - (valorTotal * percentual) / 100;
    return valorFinal < 0 ? 0 : valorFinal;
}
module.exports = { aplicarDesconto };
```

---

### 🧪 Integrante 3 – Testes e Implementação (`entrega`)

#### Teste 1 – Sucesso: Distância curta dentro do limite fixo (Happy Path)
* **Nome descritivo:** `Deve cobrar taxa fixa para distancia ate 3km`
* **Cenário testado:** Valida se a cobrança mantém o piso estável para entregas próximas ao estabelecimento.
* **Dados de entrada:** `distanciaKm = 2.5`
* **Resultado esperado:** Retornar `5.00`.
* **Código do teste:**
```javascript
const { calcularTaxaEntrega } = require('../functions/entrega');

test('Deve cobrar taxa fixa para distancia ate 3km', () => {
    const resultado = calcularTaxaEntrega(2.5);
    expect(resultado).toBe(5.00);
});
```

#### Teste 2 – Sucesso: Distância longa com acréscimo (Happy Path)
* **Nome descritivo:** `Deve cobrar taxa adicional proporcional por km acima de 3km`
* **Cenário testado:** Verifica o comportamento da regra de cálculo composto para longas distâncias.
* **Dados de entrada:** `distanciaKm = 5.0`
* **Resultado esperado:** Retornar `9.00` (calculando 5.00 base + 2km adicionais a 2.00 cada).

#### Teste 3 – Erro: Distância informada negativa (Error Case)
* **Nome descritivo:** `Deve lancar erro para distancia negativa`
* **Cenário testado:** Evita erros de geolocalização inconsistentes de corromperem o fluxo financeiro.
* **Dados de entrada:** `distanciaKm = -1.5`
* **Resultado esperado:** Lançar uma exceção `Error("Distância não pode ser negativa")`.

#### Aplicação do TDD & Refatoração
* **Red:** Construção dos testes de distância curta, longa e inválida, gerando falhas controladas no terminal.
* **Green:** Estruturação de condicionais `if-else` acopladas para forçar o sucesso imediato das asserções.
* **Refactor:** Extração de constantes de negócio lógicas para o cabeçalho do documento, expurgando "números mágicos" do miolo do algoritmo.
```javascript
const TAXA_FIXA = 5.00;
const LIMITE_DISTANCIA_FIXA = 3.0;
const VALOR_POR_KM_ADICIONAL = 2.00;

function calcularTaxaEntrega(distanciaKm) {
    if (distanciaKm < 0) {
        throw new Error("Distância não pode ser negativa");
    }
    if (distanciaKm <= LIMITE_DISTANCIA_FIXA) {
        return TAXA_FIXA;
    }
    return TAXA_FIXA + (distanciaKm - LIMITE_DISTANCIA_FIXA) * VALOR_POR_KM_ADICIONAL;
}
module.exports = { calcularTaxaEntrega };
```

---

## 🔹 3. Execução dos Testes

* **Ferramenta utilizada:** Jest v29+
* **Total de testes:** 9
* **Quantos passaram:** 9
* **Quantos falharam:** 0

**Evidência do Terminal:**
```bash
PASS  tests/pedido.test.js
PASS  tests/desconto.test.js
PASS  tests/entrega.test.js

Test Suites: 3 passed, 3 total
Tests:       9 passed, 9 total
Snapshots:   0 total
Time:        0.452 s
Ran all test suites.
```

---

## 🔹 4. Reflexão no Contexto do LocalEats

* **Foi difícil escrever testes antes do código?** Sim, pois exige uma mudança de paradigma mental. Estamos habituados a estruturar a solução imediata, e parar para analisar os fluxos de sucesso e as falhas previamente demanda maior esforço inicial.

* **O TDD ajudou no desenvolvimento?** Com certeza. Ele funcionou como uma especificação viva, impedindo-nos de criar códigos desnecessários ou complexos demais além do estritamente necessário para cumprir as regras do restaurante.

* **Os testes aumentaram a confiança no código?** Muitíssimo. A presença dessa barreira de validação nos dá liberdade para otimizar e alterar qualquer algoritmo do LocalEats sabendo que qualquer bug de regressão será acusado imediatamente.

* **O que melhorariam?** Como evolução técnica futura, aplicaríamos ferramentas nativas de verificação de tipos e validação de schema para blindar os fluxos antes mesmo deles chegarem às funções de negócio.

* **Como isso ajuda no projeto do grupo?** Garante que os fluxos críticos de fechamento de compras possuam travas de segurança contínuas, permitindo atualizações de produção com risco de quebras e prejuízos drasticamente reduzido.
