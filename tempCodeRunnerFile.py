assert reverse_words("the sky is blue") == "blue is sky the"
assert reverse_words("  hello world  ") == "world hello"
assert reverse_words("a good   example") == "example good a"
assert reverse_words("  ") == ""
assert reverse_words("word") == "word"