
# ! 1. Describe the Problem

# ? As a user
# ? So that I can manage my time
# ? I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

# ! 2. Design the Method Signature

# * extract_reading_time(text):
# calculates the amount of seconds to read text passed in based on 200 wpm
# returns an Integer

# ?  The method doesnt print anything or have any other effects, it only returns an integer.

# ! 3. Create Examples as Tests

# * extract_reading_time("hello") ==> > 1
# * extract_reading_time(5) ==> None
# * extract_reading_time(True) ==> None
# * extract_reading_time("To be, or not, to be. That is the question. Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles. And by opposing end them. ") ==> > 10
# * extract_reading_time(" ") ==> 0
# * extract_reading_time(3.141) ==> None


# ! 4. Implement the Behaviour

def extract_reading_time(text):
    if type(text) != type("string"):
        return None
    elif text == " ":
        return 0
    else:
        try:
            length = text.split(" ")
            return len(length) / (20 / 6)
        except:
            return 1 / (20 / 6)


def test_extract_reading_time_exists():
    extract_reading_time("text")

def test_extract_reading_time_returns_low_value_for_one_word():
    assert extract_reading_time("hello") < 1

def test_extract_reading_time_cannot_take_int():
    assert extract_reading_time(5) == None

def test_extract_reading_time_cannot_take_bool():
    assert extract_reading_time(True) == None

def test_extract_reading_time_returns_higher_value_for_sentence():
    assert extract_reading_time(
        "To be, or not, to be. That is the question. Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles. And by opposing end them. ") > 10

def test_extract_reading_time_returns_zero_for_empty_string():
    assert extract_reading_time(" ") == 0


def test_extract_reading_time_cannot_take_float():
    assert extract_reading_time(3.141) == None
