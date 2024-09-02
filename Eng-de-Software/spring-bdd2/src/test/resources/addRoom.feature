Feature: Add room

    This Feature adds a room to the hotel system

    #add room
    Scenario Outline: Add a room with type
        Admin wants to add a room with a type
        When the admin calls /addRoom with type = "<type>"
        Then he receives status code of 200
        And receives the room with the "<type>" characteristic

        Examples:
          |  type |
          | individual| 
          | double    |
          | suite     |

    # Add individual room   
    #Scenario: Admin wants to add an individual room
    #When the admin calls /addIndividualRoom
    #Then he receives status code of 200
    #And receives the room with the individual characteristic
    
    
    #Add double room
    #Scenario: Admin wants to add double room
    #When the admin calls /addDoubleRoom
    #Then he receives status code of 200
    #And receives the room with the double characteristic
    
    #Add suite
    #Scenario: Admin wants to add suite
    #When the admin calls /addsuite
    #Then he receives status code of 200
    #And he receives the room with the suite characteristic