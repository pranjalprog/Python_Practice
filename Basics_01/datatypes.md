# Objects Types / Data Types 
-Numbers : 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
- Strings : 'spam', "Bob's", b'a/x01c', u'sp\xc4m'
- Lists :  [1, [2, 'three'], 4.5], lists(range(10))
- Tuple : (1, 'spam', 4, 'U'), tuple('spam') , namedtuple

[backet], (paranthesis), {curlybraces}
- Dictonaries : {
    'food' : 'spam'
    'taste' : 'yum'  
} - isme indexing 0 se start nahi hoti hai 

- Set : set('abc') ,{'a','b','c'}
- File : open('eggs.txt'), open(r'C:\ham.bin','wb')
- Boolean : True, false
- None : None
- Functions , modules, classes

-Advances : Types -> Decorators, generators ,Iterators, MetaProgramming



h1 = [1,2,3]
>>> h2 = h1[:]
>>> h1
[1, 2, 3]
>>> h2
[1, 2, 3]
>>> h1[0]
1
>>> h1[0] = 55
>>> h1
[55, 2, 3]
>>> h2
[1, 2, 3]
>>> 



repr() -> returns the official, unambiguous string representation of an object (often valid Python code to recreate it)

str() -> returns a user-friendly, informal string representation meant for readability

print() -> outputs the rendered text directly to the console



### Python Number Functions

* **`math.floor(x)`**: Rounds down towards negative infinity.
* *Example:* `math.floor(-3.7) -> -4`


* **`math.trunc(x)`**: Chops off decimals towards zero.
* *Example:* `math.trunc(-3.7) -> -3`


* **`math.ceil(x)`**: Rounds up towards positive infinity.
* *Example:* `math.ceil(3.2) -> 4`


* **`round(x)`**: Rounds to the nearest integer (even ties).
* *Example:* `round(2.5) -> 2`



### Other Python Number & Math Libraries

* **`statistics`**: Statistical calculations (mean, median, mode, standard deviation).
* *Example:* `statistics.mean([1, 2, 3, 4]) -> 2.5`


* **`decimal`**: Fixed-point and floating-point arithmetic with precise control over rounding.
* *Example:* `Decimal('0.1') + Decimal('0.2') -> Decimal('0.3')`


* **`fractions`**: Rational number arithmetic (fractions support).
* *Example:* `Fraction(1, 3) + Fraction(1, 3) -> Fraction(2, 3)`


* **`cmath`**: Mathematical functions for complex numbers.
* *Example:* `cmath.sqrt(-1) -> 1j`

### Python String Methods & Libraries

#### 1. Common Built-in String Methods

* **`s.upper()` / `s.lower()**`: Converts string to uppercase or lowercase.
* *Example:* `'hello'.upper()` $\rightarrow$ `'HELLO'`


* **`s.strip()`**: Removes leading and trailing whitespace.
* *Example:* `'  hi  '.strip()` $\rightarrow$ `'hi'`


* **`s.replace(old, new)`**: Replaces a substring with another.
* *Example:* `'apple'.replace('p', 'z')` $\rightarrow$ `'azzle'`


* **`s.split(sep)`**: Splits a string into a list based on a delimiter.
* *Example:* `'a,b,c'.split(',')` $\rightarrow$ `['a', 'b', 'c']`



---

#### 2. String & Text Libraries

* **`string` Module**: Provides useful string constants.
* *Example:* `string.ascii_letters` $\rightarrow$ `'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'`


* **`re` Module (Regular Expressions)**: For advanced pattern matching and text searching.
* *Example:* `re.findall(r'\d+', 'Order 45, items 12')` $\rightarrow$ `['45', '12']`

