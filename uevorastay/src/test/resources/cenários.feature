Feature: Verify the product service

  Scenario: client makes call to GET category
    Given the service URL
    When the client calls /getCategory
    Then the client receives status code of 200 for category
    And the client receives category with name

Feature: Verify the product service

  Scenario: client makes call to GET product
    When the client calls /getProduct
    Then the client receives status code of 200
    And the client receives product with name

Podem haver vários cenários para a mesma operação

Que cenários são necessários atribuir a cada operação?
Operação 1 - definir quartos de hotel, de acordo com as caracteristicas
    cenário 1 - definir quarto individual
    cenario 2 - definir quarto duplo
    cenario 3 - definir suite
    cenario 4 - definir numero do quarto
Feature: define hotel rooms, according to their characteristics
    As an admin
    I want to define hotel rooms according to their characteristics
    Either individual, double or suite
    Each time also adding the respective number to the room

    Scenario: definir quarto individual
        When admin calls /defineindividual
        Then admin receives status code of 201
        And admin receives room with number and individual status
    Scenario: definir quarto duplo
        When admin calls /defineduplo
        Then admin receives status code of 201
        And admin receives room with number and duplo status
    Scenario: admin makes call to define suite
        When admin calls /definesuite
        Then admin receives status code of 201
        And admin receives room with number and suite status 

operação 2 - listar quartos de hotel, incluindo as suas especificações
    cenario 1 - procurar quarto individual
    cenario 2 - procurar quarto duplo
    cenario 3 - procurar suite
    cenario 4 - procurar por numero de quarto
operação 3 - editar quartos de hotel
    cenario 1 - passar de individual para duplo
    cenario 2 - passar de duplo para suite
    cenario 3 - passar de individual para suite
    cenario 4 - passar de duplo para individual
    cenario 5 - passar de suite para duplo
    cenario 6 - passar de suite para individual
operação 4 - listar as reservas do hotel
    cenario 1 - devolver os quartos por categoria e numero
    cenario 2 - devolver os quartos por numero
operação 5 - listar quartos disponíveis
    cenario 1 - sem quartos disponíveis
    cenario 2 - pelo menos 1 quarto disponivel
operação 6 - efetuar reservas de quartos
    cenario 1 - efetua pedido de reserva
operação 7 - Alterar reservas de quartos
    cenario 1 - efetua pedido de alteração de reserva
operação 8 - Realizar check in de hóspedes
    cenario 1 - associa o hospede ao quarto numerado
operação 9 - Realizar check out de hóspedes
    cenario 1 - desassocia o hospede do quarto
operação 10 - Marcar quarto como “precisa de limpeza”
    cenario 1 - quarto numero tal com aviso “precisa de limpeza”
operação 11 - Marcar quarto como “limpo”
    cenario 1 - 
operação 12 - Marcar quarto como “precisa de serviço de quartos”

