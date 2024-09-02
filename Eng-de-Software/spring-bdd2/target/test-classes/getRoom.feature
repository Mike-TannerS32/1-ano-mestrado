Feature: GET Room

    #getRoom
    Scenario Outline: get room with a type
        Client wants to find a room with type
        When the client calls /getRoom with type = "<type>"
        Then the client receives status code of 200 for type
        And the client receives room with "<type>" type

        Examples:
          |  type |
          | individual| 
          | double    |
          | suite     |
