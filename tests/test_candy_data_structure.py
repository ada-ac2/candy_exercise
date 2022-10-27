import pytest
from candy_problem.candy_problem import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert type(new_candy_data) == dict

# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    new_candy_data = create_new_candy_data_structure(friend_favorites)
    
    # Assert
    assert len(new_candy_data) == 8
    '''
    Add your assertions here!
    '''
    assert new_candy_data["lollipop"] == ["Sally", "Bob"]

'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''

def test_get_friends_favorite_candy_count():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    # Act
    result = get_friends_favorite_candy_count(friend_favorites)

    # Assert
    assert type(result) == dict
    assert len(result) == 8
    assert result["lollipop"] == 2

def test_get_friends_who_like_specific_candy():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    
    data = create_new_candy_data_structure(friend_favorites)
    candy_type = "lollipop"

    # Act
    result = get_friends_who_like_specific_candy(data, candy_type)

    # Assert
    assert len(result) == 2
    assert type(result) == tuple 
    assert result == ("Sally", "Bob")


def test_create_candy_set():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        ["Bob", ["milky way", "licorice", "lollipop"]],
        ["Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        ["Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    
    data = create_new_candy_data_structure(friend_favorites)

    # Act
    result = create_candy_set(data)
    
    # Assert
    assert type(result) == set
    assert len(result) == 8