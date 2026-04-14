# Estratégia Inicial de Testes – LocalEats

## 📌 Contexto

Vocês fazem parte da equipe de Qualidade de Software de uma startup responsável pela plataforma **LocalEats**, desenvolvida para conectar moradores e turistas a restaurantes independentes.

O sistema possui versão web e mobile e permite:

- Buscar restaurantes por tipo de culinária, localização e preço  
- Visualizar cardápios, fotos e avaliações  
- Salvar favoritos  
- Receber recomendações personalizadas  
- Compartilhar experiências  

### ⚠ Problemas identificados

- Lentidão em horários de pico  
- Telas confusas  
- Resultados incorretos  
- Falhas em smartphones  
- Dificuldade em ações simples  
- Avaliações desaparecendo  
- Inconsistências entre web e mobile  

---

## 🎯 Objetivo

Definir uma estratégia inicial de testes considerando:

- Níveis de teste  
- Prioridade baseada em risco  
- Pirâmide de testes  
- Testes em produção  

---

## 1️⃣ Funcionalidades principais

- Busca de restaurantes  
- Visualização de cardápio e avaliações  
- Finalização de pedido e pagamento  
- Cadastro e login  
- Gerenciamento de avaliações  

---

## 2️⃣ Níveis de teste

### Funcionalidade foco: Finalização de Pedido e Pagamento

**Teste Unitário**  
Validar funções de cálculo (itens, taxas, cupons).  
👉 Garantir lógica correta isoladamente  

**Teste de Integração**  
Integração entre pedidos, pagamento e banco de dados.  
👉 Evitar falhas de comunicação  

**Teste de Sistema (E2E)**  
Fluxo completo do pedido até confirmação.  
👉 Garantir funcionamento geral  

**Teste de Aceitação**  
Usuário consegue concluir compra corretamente.  
👉 Validar necessidade de negócio  

---

## 3️⃣ Prioridades e riscos

### Funcionalidades críticas

- Busca de restaurantes  
- Finalização de pedido  

### Justificativa

Falhas nessas áreas geram:

- Abandono da plataforma  
- Perda de receita  
- Impacto na reputação  

### Maior impacto

Se o usuário não encontra ou não consegue pagar, o sistema perde valor para restaurantes e usuários.

---

## 4️⃣ Pirâmide de testes

### 🔽 Base (maior volume)

**Testes Unitários**

- Baixo custo  
- Rápidos  
- Feedback imediato  

---

### 🔼 Meio

**Testes de Integração / API**

- Validam comunicação entre serviços  
- Garantem consistência entre web e mobile  

---

### 🔺 Topo (menor volume)

**Testes UI / Manuais**

- Mais caros e lentos  
- Usados apenas nos fluxos críticos  

---

## 5️⃣ Testes em produção

### ✔ Deve usar?

Sim, de forma controlada.

### 📍 Situações

**Monitoramento de performance**  
Identificar lentidão real  

**Canary Releases**  
Liberar mudanças para poucos usuários  

### Justificativa

Permite detectar problemas reais que não aparecem em desenvolvimento.

---

## 📊 Conclusão

A estratégia prioriza:

- Confiabilidade  
- Performance  
- Experiência do usuário  

Baseada no modelo **ISO 25010**, focando nos principais problemas atuais da plataforma.

---

## 📦 Entregável

- Formato: `.md`  
- Repositório:  
  `/aula-04-estrategia-inicial-testes.md`  

---
