'''
I,  Daniel Obazee    , affirm that the work submitted for this assignment is entirely my own. I have not engaged in any form of academic dishonesty, including but not limited to cheating, plagiarism, or the use of unauthorized materials. This includes, but is not limited to, the use of resources such as Chegg, MyCourseHero, StackOverflow, ChatGPT, or other AI assistants, except where explicitly permitted by the instructor. I have neither provided nor received unauthorized assistance and have accurately cited all sources in adherence to academic standards. I understand that failing to comply with this integrity statement may result in consequences, including disciplinary actions as determined by my course instructor and outlined in institutional policies. By signing this statement, I acknowledge my commitment to upholding the principles of academic integrity.
'''

# INF360 - Programming in Python
# Assignment: Sherlock Text Processing
# Description:
#     - Reads story.txt using a relative path
#     - Replaces all occurrences of "Sherlock Holmes" with my name
#     - Counts occurrences of "the"
#     - Saves modified story to mystory.txt


import re

#  Read story.txt using a relative path
with open("story.txt", "r", encoding="utf-8") as file:
    story = file.read()

# Regex to find "Sherlock Holmes"
pattern_sherlock = r"Sherlock Holmes"

#  Substitute with your name + store count
replacement_name = "Daniel Obazee"
modified_story, sherlockCount = re.subn(pattern_sherlock, replacement_name, story)

#  Regex to find "the"
pattern_the = r"\bthe\b"

#  Count occurrences of "the"
wordCount = len(re.findall(pattern_the, story, flags=re.IGNORECASE))

#  Print formatted string with original + replacement + count
print(f"Original name: Sherlock Holmes")
print(f"Replacement name: {replacement_name}")
print(f"Total replacements made: {sherlockCount}")

#  Print total number of occurrences of "the"
print(f'The word "the" appears {wordCount} times in the story.')

#  Save modified story to mystory.txt
with open("mystory.txt", "w", encoding="utf-8") as outfile:
    outfile.write(modified_story)