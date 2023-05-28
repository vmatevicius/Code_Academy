import unittest
from main import Sentence


class TestSentenceMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.sentence = Sentence()

    def test_backwards_method(self):
        self.assertEqual(self.sentence.backwards(), "sanatnA")
        self.assertNotEqual(self.sentence.backwards(), "Antanas")
        self.assertIsInstance(self.sentence.backwards(), str)


# class TestIsLeap(unittest.TestCase):
#     def test_if_returns_true_if_leap_year(self):
#         self.assertEqual(leap.is_leap(2000), False)
#         self.assertTrue(leap.is_leap(2000))

import datetime
from unittest.mock import Mock, patch
import unittest


class TestMock(unittest.TestCase):
    def test_something(self):
        datetime_mock = Mock(wraps=datetime.datetime)
        datetime_mock.now.return_value = datetime.datetime(1999, 1, 1)
        with patch("datetime.datetime", new=datetime_mock):
            assert datetime.datetime.now() == datetime.datetime(1999, 1, 1)
