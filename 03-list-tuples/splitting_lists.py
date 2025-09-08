pangram = """The quick brown 
           fox jumps\tover 
           the lazy dog"""
# ["the", "quick", "brown", "fox", "jumps", "over", ]
words = pangram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
# [""]
print(numbers.split())

numbers_list = numbers.split(sep=",")
# ["9", "223", "372", ""]
numbers = "213252159277342582"
numbers_list = numbers.split(sep="2")
# ["13", "5", "159", "7734", "58"]
print(numbers_list)