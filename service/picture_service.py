from models.User import User
from config import db
from models.Picture import Picture


def create_picture(username, data):
    
    user = User.query.filter_by(username=username).first()

    if not user:
        raise Exception("A user that doesn't exist can't upload a picture")

    if not data or not "name" in data or not "url" in data:
        raise Exception("Missing fields")
    
    name = data["name"]
    url = data["url"]
    description = data.get("description", "")

    new_picture = Picture(name, description, url, user.id)
    db.session.add(new_picture)
    db.session.commit()

    return _serialize_picture(new_picture)

def delete_picture(username, picture_id):
    user = User.query.filter_by(username=username).first()

    if not user:
        raise Exception("A user that doesn't exist can't delete a picture")

    picture = Picture.query.get(picture_id)

    if not picture:
       raise Exception("The picture doesn't exist")
    
    db.session.delete(picture)
    db.session.commit()

def delete_user_pictures(user_id):
    pictures = Picture.query.filter_by(user_id=user_id).all()
    for picture in pictures:
        db.session.delete(picture)

def _serialize_picture(picture):
    return {
        "id": picture.id,
        "name": picture.name,
        "description": picture.description,
        "url": picture.url,
        "created_at": picture.created_at.strftime("%Y-%m-%d %H:%M")
    }