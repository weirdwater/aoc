
# AoC 2022

Since I want a bit more experience with python I decided to do this year's AoC, in python. Definitely not because @ganzsz made me do it.

## Lessons learned

### Python

* To read each line of a file as a string, use `with open (filename) as file:`
* When reading each line in a file using `open` return characters can be stripped using `string.strip()` 
* To parse an int, use `int()`
* To get the index number of an list item, use enumerate to get the list's entries `tuple[int,a]`
* `list.sort()` is a mutable operation
* To get a subset of a list, use a range selector in the index selector: [0:5]
* Maps can be created using _dictionaries_ `{}`, very similar to JS objects. Added benefit: dictionaries have a .get method which allows you to safely access a member.
* Python's type system has inference. Doing a None check results in the type changing
* Enum members can have literal values
* Float is the return type of a division
* Iterables can be mapped using a generator expression: `f(x) for x in list()`
* To modify how an iterable is iterated through, you can write a custom iterator, or: Create a generator function (which uses yield in its body)
* An Iterable has a `__next__` method, a container has `__getter__` and `__setter__` methods, and a Sequence has all three + `__len__`

### Process

* I found myself future proofing code, anticipating changes. But often they would make the program with the current goal more complex than needed.
