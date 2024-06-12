class Genre:
    def __init__(self, genre_id, name, description):
        self.genre_id = genre_id
        self.name = name
        self.description = description

    def __str__(self):
        return f"Genre {self.name} (ID: {self.genre_id})"

    def to_dict(self):
        return {
            "genre_id": self.genre_id,
            "name": self.name,
            "description": self.description
        }