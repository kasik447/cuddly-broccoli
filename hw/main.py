import os

from lessons.models.database import DATABASE_NAME, Session
import create_database as db_creator

from lessons.models.lesson import Lesson, association_table
from lessons.models.student import Student
from lessons.models.group import Group
from sqlalchemy import and_, or_, not_, desc


if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()
