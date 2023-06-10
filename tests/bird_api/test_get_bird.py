
import testit as testit

from constants import CodeConstants
from framework.assert_steps import assert_objects, assert_error

BIRD_NAME_DEFAULT = 'не задан'
CRE_USER_DEFAULT = 1


def check_response(resp, bird):
    exp_type = type(resp)(
        code=CodeConstants.CODE_SUCCESS,
        cre_date=bird.cre_date,
        bird_name=bird.bird_name,
        cre_user=bird.cre_user,
        del_date=bird.del_date,
        del_user=bird.del_user,
        bird_type=bird.bird_type,
        bird_color=bird.bird_color,
        flight_distance=bird.flight_distance
    )

    assert_objects(expected_object=exp_type, target_object=resp)


class TestGetBird:

    @testit.workItemIds(123)
    def test_get_bird_default_error(self, workplace, create_bird):
        with testit.step("Отправка запроса getBird"):
            resp = workplace.bird_api.send_get_bird(bird_id=0)

        with testit.step("Проверка"):
            assert_error(resp, exp_err_code=CodeConstants.CODE_NO_DATA_FOUND)

    @testit.workItemIds(124)
    def test_get_bird_ok(self, workplace, create_bird):
        with testit.step("Создание птицы"):
            bird = create_bird()

        with testit.step("Отправка запроса getBird"):
            resp = workplace.bird_api.send_get_bird(bird_id=bird.id)

        with testit.step("Проверка"):
            check_response(resp=resp, bird=bird)
