Feature: Change room type

    This feature changes a rooms type
    Scenario Outline:change room type from type1 to type2
        Admin wants to change room type from type1 to type2
        When the admin calls /changeRoomtype with type = <type1>
        Then prompt appears to change room type with status 200
        And he receives the room with type <type2>

        Examples:
            |type1 | type2  |
            |"individual"| "double" |
            |"double"|"suite"|
            |"suite"|"individual"|
            | "double"|"individual" |
            |"suite" | "double"|