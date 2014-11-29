from unittest import TestCase


def reverse_words(phrase):
    reversed_list = (''.join(list(reversed(word))) for word in phrase.split())
    return ' '.join(reversed_list)
class ReverseWordTests(TestCase):
    def test(self):
        self.assertEqual('áres euq ?etrever', reverse_words('será que reverte?'))