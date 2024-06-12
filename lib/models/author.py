class Author:
    def __init__(self, author_id, name, bio):
        self.author_id = author_id
        self.name = name
        self.bio = bio

    def __str__(self):
        return f"Author {self.name} (ID: {self.author_id})"

    def to_dict(self):
        return {
            "author_id": self.author_id,
            "name": self.name,
            "bio": self.bio
        }