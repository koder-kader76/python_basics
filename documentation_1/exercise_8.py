# Large Integers

# Using the Python documentation, determine how you can write large integers in a way that makes them easier to read.

# source: https://docs.python.org/3/reference/lexical_analysis.html#literals

# 2.4.5. Integer literals

# There is no limit for the length of integer literals apart from what can be stored in available memory.

# Underscores are ignored for determining the numeric value of the literal. They can be used to group digits for enhanced readability. One underscore can occur between digits, and after base specifiers like 0x.

# Note that leading zeros in a non-zero decimal number are not allowed. This is for disambiguation with C-style octal literals, which Python used before version 3.0.

# example code
2147483647
79228162514264337593543950336
100_000_000_000