from typing import List
from .models import *
from .db_utils import *
from . import db

def add_tag_category(**kwargs) -> Apartment:
    category = TagCategory.query.filter_by(**kwargs).first()
    if category:
        return category
    
    category = TagCategory(**kwargs)
    db.session.add(category)

    db.session.commit()

    return category 
    
def filter_tag_category_by_name(**kwargs) -> Apartment:
    return Tag.query.filter_by(**kwargs)

def add_tag(**kwargs) -> Apartment:
    # check if tag exists
    tag = Tag.query.filter_by(**kwargs).first()
    if tag:
        return tag

    # check if category exists
    category_id = kwargs.get('category_id', None)
    category = TagCategory.query.filter_by(id=category_id).first()
    if not category:
        return None

    new_tag = Tag(**kwargs)

    db.session.add(new_tag)
    db.session.commit()
    return new_tag

def add_house(**kwargs):
    house = House.query.filter_by(**kwargs).first()
    if house:
        return house
    
    thumbnail = kwargs.pop('thumbnail', None)
    if thumbnail:
        kwargs['thumbnail_id'] = cast_to_model(thumbnail, Image).id
    
    new_house = House(**kwargs)
    db.session.add(new_house)
    images = kwargs.pop('images', None)
    if images:
        for img in images:
            img = cast_to_model(img, Image)
            new_house.images.append(img)  

    db.session.commit()

    return new_house


def add_apartment(**kwargs) -> Apartment:

    house = kwargs.pop('house')
    kwargs['house_id'] = cast_to_model(house, House).id

    thumbnail = kwargs.pop('thumbnail', None)
    if thumbnail:
        kwargs['thumbnail_id'] = cast_to_model(thumbnail, Image).id
    
    tags = kwargs.pop('tags', None)
    images = kwargs.pop('images', None)

    apartment = Apartment.query.filter_by(**kwargs).first()
    if apartment:
        return apartment
    
    new_apartment = Apartment(**kwargs)
    db.session.add(new_apartment)
    
    if tags:
        for tag in tags:
            tag = cast_to_model(tag, Tag)

            new_apartment.tags.append(tag)

    if images:
        for img in images:
            img = cast_to_model(img, Image)
            new_apartment.images.append(img)  

    db.session.commit()

    return new_apartment



def add_image(**kwargs):
    img = Image.query.filter_by(**kwargs).first()
    if img:
        return img
    
    img = Image(**kwargs)
    db.session.add(img)

    db.session.commit()

    return img
