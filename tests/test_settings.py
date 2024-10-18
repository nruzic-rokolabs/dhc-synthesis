from app.settings import settings

import tests.settings_factory as sf1
import tests.another_settings_factory as sf2


def test_settings_identity():
    assert id(sf1.get_settings()) == id(sf2.get_settings())
    assert id(settings) == id(sf2.get_settings())


def test_settings_application_name():
    assert settings.application_name == "Dark Horse Consulting Synthesis Project Test Application"
