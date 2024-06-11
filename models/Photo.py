from config import db

class Photo(db.Model):
    __tablename__ = "photo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120))
    url = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, name, description, url, user_id):
        self.name = name
        self.description = description
        self.url = url
        self.user_id = user_id
    
    def __repr__(self) -> str:
        return f"Photo name: {self.name}"