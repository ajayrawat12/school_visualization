import json
import falcon
from libs.queries import get_students


class Student(object):
    """
            Update the user ratings,
    """

    def on_get(self, req, resp):
        try:
            body = req.params
            class_id = body.get('class_id')
            sec_id = body.get('section_id')

            data = get_students(class_id, sec_id)
            resp.status = falcon.HTTP_201
            status = True
            dump_dict = {'status': status,
                         'message': "successfully saved the ratings",
                         'data': data}
            resp.body = json.dumps(dump_dict)

        except Exception as e:
            print(e)
            pass
