import unittest

from word_count import word_count


class WordCountTests(unittest.TestCase):

    def test_count_one_word(self):
        self.assertEqual(
            {'word': 1},
            word_count('word')
        )

    def test_count_one_of_each(self):
        self.assertEqual(
            {'one': 1, 'of': 1, 'each': 1},
            word_count('one of each')
        )

    def test_count_multiple_occurences(self):
        self.assertEqual(
            {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1},
            word_count('one fish two fish red fish blue fish')
        )


    def test_include_numbers(self):
        self.assertEqual(
            {'testing': 2, '1': 1, '2': 1},
            word_count('testing 1 2 testing')
        )

    def test_mixed_case(self):
        self.assertEqual(
            [2, 3],
            sorted(list(word_count('go Go GO Stop stop').values()))
        )


if __name__ == '__main__':
    unittest.main()
