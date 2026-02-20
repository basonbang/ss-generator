import unittest 
from generatepage import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        basic_md = "# This is a title\nThis is some content"
        empty_md = "\n\n\n"
        no_title_md = "This is some content without a title\n## This is a subtitle\nThis is more content"

        self.assertEqual(extract_title(basic_md), "This is a title")
        self.assertRaises(ValueError, extract_title, empty_md)
        self.assertRaises(ValueError, extract_title, no_title_md)
        