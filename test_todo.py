
# ! 1. Describe the Problem

# ? As a user
# ? So that I can keep track of my tasks
# ? I want to check if a text includes the string #TODO.


# ! 2. Design the Method Signature

# * def has_todo_or_not():
# looks inside a string to see if it contains #TODO
# return a boolean value, either True or False


# ?  The method doesnt print anything or have any other effects, it only returns a boolean based on the TODO check.

# ! 3. Create Examples as Tests

# * has_todo_or_not(""): ==> False
# * has_todo_or_not("#TODO"): ==> True
# * has_todo_or_not("TODO"): ==> False
# * has_todo_or_not("#Todo"): ==> False
# * has_todo_or_not("#HELLO"): ==> False
# * has_todo_or_not("#TODO Make sure to get groceries"): ==> True
# * has_todo_or_not("Hello, how are you? #TODO Could you bring a spare shovel when you come in today"): ==> True
# * has_todo_or_not("Hello, how are you? #Todo Could you remember to water the plants."): ==> Fasle
# * has_todo_or_not(129): ==> False
# * has_todo_or_not(True): ==> False
# * has_todo_or_not(3.141): ==> False
# * has_todo_or_not([]): ==> False (!!!)


# ! 4. Implement the Behaviour

def has_todo_or_not(text):
    if type(text) is str:
        if "#TODO" in text:
            return True
        else:
            return False
    else:
        return False


def test_has_todo_or_not():
    assert has_todo_or_not("") == False


def test_todo_has_correct_syntax_true():
    assert has_todo_or_not("#TODO") == True


def test_lowercase_todo_false():
    assert has_todo_or_not("#Todo") == False


def test_for_missing_hashtag_false():
    assert has_todo_or_not("TODO") == False


def test_different_string_with_hashtag_false():
    assert has_todo_or_not("#HELLO") == False


def test_long_string_text_true():
    assert has_todo_or_not("#TODO Make sure to get groceries") == True


def test_todo_in_middle_of_string_true():
    assert has_todo_or_not(
        "Hello, how are you? #TODO Could you bring a spare shovel when you come in today") == True


def test_lowercase_todo_in_string_false():
    assert has_todo_or_not(
        "Hello, how are you? #Todo Could you remember to water the plants.") == False


def test_integer_input_false():
    assert has_todo_or_not(129) == False


def test_boolean_input_false():
    assert has_todo_or_not(True) == False


def test_float_input_is_false():
    assert has_todo_or_not(3.141) == False


def test_to_see_if_this_function_will_take_a_LIST():
    assert has_todo_or_not([]) == False  # YAYYYYYYY LEARNING!!!
