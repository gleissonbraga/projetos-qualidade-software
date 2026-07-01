Feature: Carrinho de compras

  Scenario: Adicionar produto ao carrinho

    Given que o usuário está logado
    When acessar um restaurante
    And selecionar um produto
    And adicionar o produto ao carrinho
    Then o produto deve aparecer no carrinho

# Scenario: Remover produto do carrinho
#   Given que o usuário está logado
#   When acessar um restaurante
#   And selecionar um produto
#   And adicionar o produto ao carrinho
#   And remover o produto do carrinho
#   Then o produto não deve aparecer no carrinho

# Scenario: Verificar carrinho vazio
#   Given que o usuário está logado
#   When acessar a página do carrinho sem adicionar produtos
#   Then o carrinho deve estar vazio