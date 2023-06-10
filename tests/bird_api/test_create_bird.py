from datetime import datetime

import testit as testit

from constants import CodeConstants
from framework.assert_steps import assert_objects_are_equal

BIRD_NAME_DEFAULT = 'не задан'
CRE_USER_DEFAULT = 1


def check_response(workplace, resp, curr_date, **kwargs):
    bird_row = workplace.db.get_bird_by_id(bird_id=resp.message.split("=")[1])
    bird_description_row = workplace.db.get_bird_by_id(bird_id=resp.message.split("=")[1])

    data = {'code': [resp.code, CodeConstants.CODE_SUCCESS], 'curr_date': [bird_row.cre_date > curr_date],
            'bird_name': [bird_row.bird_name, kwargs.get('bird_name', BIRD_NAME_DEFAULT)],
            'cre_user': [bird_row.cre_user, kwargs.get('cre_user', CRE_USER_DEFAULT)],
            'del_date': [bird_row.del_date is None],
            'del_user': [bird_row.del_user is None],
            'bird_type': [bird_description_row.bird_type, kwargs.get('bird_type')],
            'bird_color': [bird_description_row.bird_color, kwargs.get('bird_color')],
            'flight_distance': [bird_description_row.flight_distance, kwargs.get('flight_distance')]}

    assert_objects_are_equal(data)

class TestCreateBird:

    @testit.workItemIds(123)
    def test_create_bird_default(self, workplace):
        with testit.step("Отправка запроса createBird"):
            curr_date = datetime.now()
            resp = workplace.bird_api.send_create_bird()

        with testit.step("Проверка"):
            check_response(workplace=workplace, resp=resp, curr_date=curr_date)

    @testit.workItemIds(124)
    def test_create_bird_default(self, workplace):
        with testit.step("Отправка запроса createBird"):
            curr_date = datetime.now()
            resp = workplace.bird_api.send_create_bird(bird_name="Kovalski",
                                                       bird_type=2,
                                                       bird_color=5,
                                                       flight_distance=544)

        with testit.step("Проверка"):
            check_response(workplace=workplace, resp=resp, curr_date=curr_date, bird_name="Kovalski",
                           bird_type=2, bird_color=5, flight_distance=544)
