
# ! 1. Describe the Problem

# ? As a user
# ? So that I can improve my grammar
# ? I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.


# ! 2. Design the Method Signature

# * capital_and_punctuation_check(text):
# checks the text argument has a capital letter at the start.
# Checks text has a sentence ending punctuation at the end.
# returns a Boolean

# ?  The method doesnt print anything or have any other effects, it only returns a boolean based on the two checks.

# ! 3. Create Examples as Tests

# * capital_and_punctuation_check("Hello.") ==> True
# * capital_and_punctuation_check("Hello") ==> False
# * capital_and_punctuation_check("hello.") ==> False
# * capital_and_punctuation_check("hello") ==> False
# * capital_and_punctuation_check("Hello?") ==> True
# * capital_and_punctuation_check("y tho?") ==> False
# * capital_and_punctuation_check("Welcome!") ==> True
# * capital_and_punctuation_check("welcome!") ==> False
# * capital_and_punctuation_check(17) ==> False
# * capital_and_punctuation_check("") ==> False
# ! at this point I worry if I have overcomplicated things...
# * capital_and_punctuation_check("Hello. How are you?") ==> True
# * capital_and_punctuation_check("Hello. how are you?") ==> False
# * capital_and_punctuation_check("Hello, how are you?") ==> True
# * capital_and_punctuation_check("Hello! Long time no speak!") ==> True
# * capital_and_punctuation_check("Hello. How are you?") ==> True


# ! 4. Implement the Behaviour

def capital_and_punctuation_check(text):
    try:
        return True if text[-1] in [".", "?", "!"] and text[0].isupper() else False
    except:
        return False


def test_capital_and_punctation_check():
    assert capital_and_punctuation_check("Hello.") == True


def test_punctation_missing_end():
    assert capital_and_punctuation_check("Hello") == False


def test_capital_missing_start():
    assert capital_and_punctuation_check("hello.") == False


def test_punctation_has_question_mark_at_end():
    assert capital_and_punctuation_check("Hello?") == True


def test_lowercase_start_wuestion_mark_end():
    assert capital_and_punctuation_check("y tho?") == False


def test_exclamation_at_end():
    assert capital_and_punctuation_check("Welcome!") == True


def test_exclamation_at_end_lowercase_start():
    assert capital_and_punctuation_check("welcome!") == False


def test_for_integer_input():
    assert capital_and_punctuation_check(17) == False


def test_for_empty_string():
    assert capital_and_punctuation_check("") == False
