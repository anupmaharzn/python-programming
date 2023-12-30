# regular experssion pattern

# character identifers

| character | Description | Example Pattern Code | Example Match |
| :---: | :---: | :---: | :---: |
| \d | A digit | file\_\d\d  | file_23 |
| \w | Alphanumeric | \w-\w\w\w  | A-b_1 |
| \s | White space | a\sb\sb  | a b c |
| \D | A non digit | \D\D\D  | ABC |
| \W | Non-alphanumeric | \W\W\W\W\W  | "-+=) |
| \S | Non-whitespace | \S\S\S\S  | Yoyo |

# quantifier in regex

- quantifier are the occurrence indicators (or repetition operators)

| character | Description | Example Pattern Code  | Example Match |
| :---: | :---: | :---:  | :---: |
| + | Occurs one or more times | version \w-\w+  | version \w-\w+ |
| {3} | Occurs exactly 3 times | \D{3} |  abc |
| {2,4} | Occurs 2 to 4 times | \d{2,4} | 123 |
| {3,} | Occurs 3 or more | \w{3,} |  anycharacters |
| \_ | Occurs zero or more times | A*B*C\* |  AAACC |
| ? | once or none | plurals? |  plural |

# additional regex

- | pip is or operator
- . period is wild card
 - [...] accept any one of the character within the square bracket eg [aeiou]
 - [.-.] accept any one of the character in the range [0-9] [a-zA-z]
 - [^...] not one of the character

- position anchors
 -- ^ carrot is start with
 -- $ dollor is end with
