Feature: Finalização de pedido

Scenario: Finalizar pedido com sucesso
    Given que o usuário está na página de login
    When realiza login com credenciais válidas
    And adiciona um item ao carrinho
    And finaliza o pedido
    Then o sistema exibe a mensagem "Pedido Realizado!"

# Scenario: Visualizar detalhes do pedido
#     Given que um pedido foi realizado
#     When o usuário seleciona "Ver Detalhes"
#     Then os detalhes do pedido são exibidos

# Scenario: Adicionar item ao carrinho
#     Given que o usuário está autenticado
#     When adiciona um item ao carrinho
#     Then o carrinho deve conter o item