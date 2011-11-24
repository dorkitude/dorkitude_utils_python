# Python standard library imports:
import random
import unittest


# Our imports:
from ..base_test_case import BaseTestCase
from .. import introspection
from .. import hashing
from .. import random_utils
from .. import list_utils
from .. import hashing
from .. import string_utils
from .. import introspection
from ..classproperty import classproperty



class AbstractSomethingNew(object):

    @classproperty
    def my_prop(cls):
        raise NotImplementedError

class SomethingNew(object):

    _my_prop = 'Hello'

    @classproperty
    def my_prop(cls):
        return cls._my_prop


class UtilsTestCase(BaseTestCase):

    def test_classproperty(self):
        cls = SomethingNew
        self.assert_equal(cls.my_prop, cls._my_prop)

        with self.assert_raises(NotImplementedError):
            print AbstractSomethingNew.my_prop

    def test_do_weighted_draw(self):
        draw = random_utils.do_weighted_draw([0,0,0,0,55511])
        self.assert_true(draw == 4)
        draw = random_utils.do_weighted_draw([0,9999,0,0])
        self.assert_true(draw == 1)

    def test_extract_classes(self):
        class Cls1(object):
            pass


        class Cls2(object):
            pass


        class Cls3(Cls1, Cls2):
            pass


        class Cls4(Cls1):
            pass


        class Cls5(Cls4, Cls2):
            pass


        expected_1 = [Cls1]
        self.assert_equal(introspection.extract_classes(Cls1), expected_1)

        expected_2 = [Cls2]
        self.assert_equal(introspection.extract_classes(Cls2), expected_2)

        expected_3 = [Cls3, Cls1, Cls2]
        self.assert_equal(introspection.extract_classes(Cls3), expected_3)

        expected_4 = [Cls4, Cls1]
        self.assert_equal(introspection.extract_classes(Cls4), expected_4)

        expected_5 = [Cls5, Cls4, Cls1, Cls2]
        self.assert_equal(introspection.extract_classes(Cls5), expected_5)

    def test_dedupe_list(self):
        s = [1, 2, 1,2,3,4,5]
        e = [1,2,3,4,5]
        self.assert_equal(list_utils.dedupe_list(s), e)

        s = [1,2,3,4,5, 4, 5, 6, 5]
        e = [1,2,3,4,5, 6]
        self.assert_equal(list_utils.dedupe_list(s), e)

        s = [1,2,"3",4,5, 1, 1, "3", 4, 5, 6, 5]
        e = [1,2,"3",4,5, 6]
        self.assert_equal(list_utils.dedupe_list(s), e)

        s = [1,2,3,4,5]
        e = [1,2,3,4,5]
        self.assert_equal(list_utils.dedupe_list(s), e)

    def test_to_camel(self):
        self.assert_equal(
                string_utils.snake_to_camel("ninjas_are_cool"),
                "NinjasAreCool")
        self.assert_equal(
                string_utils.snake_to_camel("ninjas_are cool"),
                "NinjasAreCool")
        self.assert_equal(
                string_utils.snake_to_camel("ninjas -_  are_cool"), 
                "NinjasAreCool")
        self.assert_equal(
                string_utils.snake_to_camel(",ninjas , are_cool"),
                "NinjasAreCool")
        self.assert_equal(
                string_utils.snake_to_camel(",ninjas 3, are_cool"),
                "Ninjas3AreCool")
        self.assert_equal(
                string_utils.snake_to_camel("1_is_funny3"),
                "1IsFunny3")


        self.assert_equal(
                string_utils.snake_to_camel("AlreadyCamelWord AnotherWord"),
                "AlreadyCamelWordAnotherWord")

    def test_camel_to_snake(self):
        self.assert_equal(
                string_utils.camel_to_snake("ninjas_are_cool"),
                "ninjas_are_cool")
        self.assert_equal(
                string_utils.camel_to_snake("NinjasAreTheBomb"),
                "ninjas_are_the_bomb")
        self.assert_equal(
                string_utils.camel_to_snake("NinjasAre TheBomb"),
                "ninjas_are_the_bomb")
        self.assert_equal(
                string_utils.camel_to_snake("NinjasAre theBomb"),
                "ninjas_arethe_bomb")
        self.assert_equal(
                string_utils.camel_to_snake("i am a cool dude"),
                "iamacooldude")

    def test_snake_to_mixed(self):
        self.assert_equal(string_utils.snake_to_mixed("hello_there"), "helloThere")
        self.assert_equal(string_utils.snake_to_mixed("is_1_funnier_3"), "is1Funnier3")
