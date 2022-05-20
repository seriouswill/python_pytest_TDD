### python_pytest_TDD
repo for my foray into TDD

## Utilizing the Method Design Recipe Method!

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

_Pull out verbs for potential methods and nouns for potential objects!_

## 2. Design the Method Signature

_Include the name of the method, its parameters, return value, and side effects._

```python
# EXAMPLE

# * capital_and_punctuation_check(text):
# checks the text argument has a capital letter at the start.
# Checks text has a sentence ending punctuation at the end.
# returns a Boolean

# The method doesn't print anything or have any other side-effects
```

## 3. Create Examples as Tests

_Make a list of examples of what the method will take and return._

```python
# EXAMPLE

capital_and_punctuation_check("Hello.") ==> True
capital_and_punctuation_check("Hello") ==> False
capital_and_punctuation_check("hello.") ==> False
capital_and_punctuation_check("hello") ==> False
capital_and_punctuation_check("Hello?") ==> True
capital_and_punctuation_check("y tho?") ==> False
capital_and_punctuation_check("Welcome!") ==> True
capital_and_punctuation_check("welcome!") ==> False
capital_and_punctuation_check(17) ==> False
capital_and_punctuation_check("") ==> False
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
