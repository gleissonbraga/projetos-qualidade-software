Feature: Login de usuário

  Scenario: Usuário realiza login com sucesso
    Given que o usuário está na página de login
    When realizar login com usuário válido
    Then o usuário deve acessar a página inicial


#  Scenario: Usuário tenta login com senha inválida
#    Given que o usuário está na página de login
#    When informar usuário válido e senha inválida
#    And clicar no botão de login
#    Then deve visualizar uma mensagem de erro

#  Scenario: Usuário tenta login sem preencher campos
#    Given que o usuário está na página de login
#    When clicar no botão entrar sem informar dados
#    Then deve visualizar validação dos campos