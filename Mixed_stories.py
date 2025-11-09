with open("Mixed_stories.txt", "r") as infile, \
     open("story_A.txt", "w") as story_a, \
     open("story_B.txt", "w") as story_b:

    for index, line in enumerate(infile):
        if index % 2 == 0:
            story_a.write(line)
        else:
            story_b.write(line)

print("The story successfully transitioned to Story A and Story B")
