# RISK
Risk is a game of world/country/territory domination, based on a "per turn"
strategy.

## Basic rules:
- You have some troops (or units or soldiers) and you can attack the adjacent 
territories.
- Your troops also can defend your territories.
- Every territory that is owned by a player must have, at least, one unit.
- When you attack a territory there are 3 possibilities:
    1. Defender looses troops.
    1. Attacker looses troops.
    1. Both, attacker and defender loose troops.
- When a defender looses all the troops from a territory, the attacker has to
 pass, at least, one unit to the new conquered territory.
- The winner is the player who has more territories under control.
- When you own some territories, you can get more soldiers.
- There are also bonuses of soldiers for having under control some related 
regions of territories.

## Objective
- Develop a Risk game in Python.
- The game will be world-based.
- The basic territory will be the country.
- The regions will be the continents.

## Work
### Class Country
Develop a new class called Country in the module `countries.py`.

#### Class attributes
- **name** (public, string, mandatory): name of the country. This attribute
has to be sentwhen creating the class
- **owner** (private, string): It can be `None` (a country can be owned by
nobody until it is conquered).
- **adjacent_countries** (private, list): List of adjacent countries.
- **soldiers** (private, integer): number of soldiers in the country.

#### Class methods
- **set_owner(new_owner, number_of_soldiers)**
    ```
    Method to change the owner of the country.
    Returns nothing.
    Number of soldiers must be, at least, 1, otherwise, the player cannot
    conquer a country.
    If there are soldiers in the country (from the previous owner), the new
    owner cannot be set.
    If the owner to set is None, the soldiers of the territory will be set to 0
    and the value of `number_of_soldiers` will be ignored.
    ```   
- **is_adjacent(country_name)**
    ```
    Returns True or False.
    If a country_name is in the list of adjacent_countries, it should return
    True. Return False otherwise.
    This method has to be private.
    ```
- **move_soldiers(country, number_of_soldiers)**
    ```
    A country can only move units if the number of units is greater than one 
    (we cannot have a country with an owner but without soldiers).
    A country can only move troops to adjacent countries.
    The number of moved soldiers has to be removed from their original country.
    ```
- **remove_soldiers(number_of_soldiers)**
    ```
    Remove soldiers from the country. If the number of soldiers to remove is 
    greater than the total amount of soldiers in the country, all of them have
    to be removed (remember you cannot have a negative number of soldiers).
    ```
- **add_soldiers(number_of_soldiers)**
    ```
    Add soldiers to the country. You can only add soldiers if the country has
    an owner.
    ```
- **set_adjacent(name)**
    ```
    Add an adjacent country.
    Returns the number of adjacent countries.
    ```

#### Considerations
- str(country) should return the country name.
- len(country) should return the number of the soldiers in the country.
- A country without owner cannot have soldiers on it.
- A country with an owner must have soldiers on it.
- If you try to set an adjacent country more than once, it will only be added
once.
