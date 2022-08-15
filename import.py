import def_init as media

# In this case self is toy_story
# toy_story = media.Movie()

# This concept of self is really difficult to understand
# This will now throw and error because it is looking for arguments

# New code
toy_story = media.Movie("Toy Story", "A story of a boy", "https://en.wikipedia.org/wiki/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

print(toy_story.storyline)