## 1. Fluxo Funcional Escolhido

### Login de Usuário

**Descrição:**
Permite autenticar um usuário no sistema LocalEats.

**Importância:**
Controla o acesso às funcionalidades do sistema e garante que apenas usuários válidos possam utilizar a aplicação.

**Cenários automatizados:**

* Login válido → acesso ao sistema.
* Login inválido → exibição de mensagem de erro.
* Campo obrigatório não preenchido → validação do formulário.

### Adição de Item ao Carrinho

**O que faz**  
Permite adicionar produtos ao carrinho de compras.

**Importância**  
Parte central do fluxo de compra, pois permite ao usuário selecionar os itens desejados antes da finalização do pedido.

**Cenários automatizados**

- Item adicionado com sucesso
- Carrinho atualizado corretamente

### Fluxo de Pedido (Checkout)

**O que faz**  
Permite finalizar o pedido após a seleção dos produtos.

**Importância**  
Fluxo crítico de negócio, responsável pela conclusão da compra.

**Cenários automatizados**

- Pedido finalizado com sucesso
- Exibição de feedback ao usuário após a conclusão do pedido

---

### Observações sobre o Codegen

**O que o Codegen fez bem**

* Identificou automaticamente os elementos da interface
* Gerou rapidamente os fluxos de login e checkout
* Ajudou na descoberta inicial de seletores

**O que gerou de desnecessário**

* Cliques redundantes em elementos da página
* Código mais extenso do que o necessário
* Seletores pouco precisos em alguns pontos

---

### Melhorias realizadas

* Remoção de cliques desnecessários gerados pelo Codegen
* Centralização dos seletores em classes Page Object
* Reutilização de código entre diferentes testes
* Uso de validações mais específicas e confiáveis
* Maior legibilidade e manutenção dos testes

---

## 4. Execução dos Testes

**Ferramentas utilizadas:**

* Python
* Pytest
* Playwright

**Resultado da execução:**

```bash
=============================== test session starts ================================

collected 5 items                                                                  

tests/test_add_carrinho.py::test_adicionar_item_ao_carrinho[chromium] PASSED
tests/test_checkout.py::test_checkout_fluxo[chromium] PASSED
tests/test_login.py::test_login_com_sucesso[chromium] PASSED
tests/test_login_invalido.py::test_login_com_credenciais_invalidas[chromium] PASSED
tests/test_login_vazio.py::test_login_com_senha_vazia[chromium] PASSED

================================ 5 passed in 20.69s ================================
```

**Total de testes:** 5
**Passaram:** 5
**Falharam:** 0

---

## 5. Análise Crítica

O teste quebrou em algum momento? Por quê?
Sim. Em versões iniciais, o Codegen gerou seletores genéricos e redundantes que causaram falhas e instabilidade.

Quais seletores foram mais difíceis?
Elementos de validação pós-login e confirmação de pedido foram os mais sensíveis, por dependerem de textos dinâmicos.

O Codegen ajudou ou gerou problemas?
Ajudou na criação inicial dos fluxos, mas gerou código redundante que precisou de refatoração.

O teste é confiável? Por quê?
Sim. Agora utiliza seletores mais específicos e valida elementos reais da interface.

O que tornaria o teste mais robusto?
Uso de atributos como data-testid para evitar dependência de texto visível.

Quais são os riscos de manutenção?
Mudanças de texto ou layout podem exigir ajustes nos seletores.

---

## 6. Reflexão no Contexto do LocalEats

Testes automatizados substituem testes manuais?
Não. Eles complementam os testes manuais e reduzem tarefas repetitivas.

Vale a pena automatizar todos os fluxos?
Não. Apenas fluxos críticos devem ser automatizados.

Qual tipo de teste deve ser priorizado?
Fluxos críticos como login, carrinho e checkout.

Como isso ajuda no projeto do grupo?
Aumenta a confiança no sistema e reduz riscos em alterações futuras.
