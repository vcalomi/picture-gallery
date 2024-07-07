from models.User import User
from config import db
from service.photo_service import _serialize_photo
from models.Photo import Photo


def create_photo(username, data):
    
    user = User.query.filter_by(username=username).first()

    if not user:
        raise Exception("A user that doesn't exist can't upload a photo")

    if not data or not "name" in data or not "url" in data:
        raise Exception("Missing fields")
    
    name = data["name"]
    url = data["url"]
    description = data.get("description", "")

    new_photo = Photo(name, description, url, user.id)
    db.session.add(new_photo)
    db.session.commit()

def delete_photo(user_id, photo_id):
    user = User.query.get(user_id)

    if not user:
        raise Exception("A user that doesn't exist can't delete a photo")

    photo = Photo.query.get(photo_id)

    if not photo:
       raise Exception("The photo doesn't exist")
    
    db.session.delete(photo)
    db.session.commit()
    
def _serialize_photo(photo):
    return {
        "id": photo.id,
        "name": photo.name,
        "description": photo.description,
        "url": photo.url,
        "created_at": photo.created_at.strftime("%Y-%m-%d %H:%M")
    }