import unittest
import common


class TestCommon(unittest.TestCase):
    def test_Oracle(self):
        self.assertEqual(common.replaceAll("Oracle"),"Oracle©")

    def test_Google(self):
        self.assertEqual(common.replaceAll("Google"),"Google©")
    
    def test_Oracle_And_Google_Together(self):
        self.assertEqual(common.replaceAll("Oracle and Google"),"Oracle© and Google©")

    #oracle should not get converted as the mapping is for Oracle and not oracle
    def test_oracle(self):
        self.assertNotEqual(common.replaceAll("oracle"),"Oracle©")

    def test_All_combine(self):
        self.assertEqual(common.replaceAll("Oracle Google Microsoft Amazon Deloitte"), "Oracle© Google© Microsoft© Amazon© Deloitte©")

    #Google is one word and GoogleTrademark is a different word should not replace the value of GoogleTrademark
    def test_GoogleTrademark(self):
        result = common.replaceAll("This is Google and it have a GoogleTrademark")
        self.assertEqual(result,"This is Google© and it have a GoogleTrademark")

if __name__ == '__main__':
    unittest.main()