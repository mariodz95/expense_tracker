from app import config as uut


def test_Config(config_dict):
    actual = uut.Config(**config_dict)

    assert actual == config_dict


def test_get_config(config_dict):
    actual = uut.get_config()

    assert actual.model_dump() == config_dict
