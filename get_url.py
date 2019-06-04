from urllib.request import urlopen

with urlopen('http://www.xbeat.net/vbspeed/') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    for palavra in story_words:
        print(palavra)
