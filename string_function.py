story='''once upon a time there was a youtuber named Harry 
who uploaded python course with notes upon'''

#string function
print(len(story))
print(story.endswith("notes")) #notes then return true 
print(story.endswith("dhjhff")) #any thing type then return false
print(story.count("a")) #"a" character count total 6
print(story.count("b")) #"b" character count total 1
print(story.count("upon")) #"upon" string count 2
print(story.capitalize()) #start "o" character return capital
print(story.find("Harry")) #find harry string value no.
print(story.replace("Harry", "withcodeharry")) # Harry name change and replace withcodeharry
