from sqlalchemy import and_
from models import scl_session
from models.school_db import Student


def get_students(class_id, sec_id):
        # get users of a repo
    data = scl_session.query(Student).filter(and_(class_id=class_id, section_id=sec_id)).all()

    stu_data = []
    if data:
        print(data)
        for d in data:
            stu_data.append({
                'stu_id': d.id,
                'name': d.name,
                'section': d.section_id,
                'class': d.class_id,
                'address': d.address
            })

    return stu_data
