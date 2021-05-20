import unittest
import requests
from triangle import hyp
from HtmlTestRunner import HTMLTestRunner


class TestBookCreate(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.data = {"title": "unittest", "author": "ivvol"}

    def test_book_create(self):
        resp = requests.post(self.base_url + "books/", data=self.data)
        self.assertEqual(resp.status_code, 201)
        resp_dict = resp.json()
        self.assertIn('id', resp_dict)
        self.data['id'] = resp_dict['id']

    def tearDown(self):
        r = requests.delete(self.base_url + "books/" + str(self.data['id']))
        print(r.status_code)

class TestBookRead(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.data = {"title": "unittest", "author": "ivvol"}
        self.book_post = requests.post(self.base_url + "books/", data=self.data)
        resp_dict = self.book_post.json()
        self.data['id'] = resp_dict['id']

    def test_book_read(self):
        resp = requests.get(self.base_url + "books/" + str(self.data['id']))
        self.assertEqual(resp.status_code, 200)
        resp_1 = self.book_post.json()
        resp_2 = resp.json()
        self.assertDictEqual(resp_1, resp_2)

    def tearDown(self):
        r = requests.delete(self.base_url + "books/" + str(self.data['id']))
        print(r.status_code)


class TestBookUpdate(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.data = {"title": "unittest", "author": "ivvol"}
        self.resp = requests.post(self.base_url + "books/", data=self.data)
        resp_dict = self.resp.json()
        self.data['id'] = resp_dict['id']

    def test_book_update(self):
        resp = requests.put(self.base_url + 'books/' + str(self.data['id']), data={'title': 'edit book'})
        self.assertEqual(resp.status_code, 200)
        # resp_dict = resp.json()

    def tearDown(self):
        r = requests.delete(self.base_url + "books/" + str(self.data['id']))
        print(r.status_code)


class TestBookDelete(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"
        self.data = {"title": "unittest", "author": "ivvol"}
        self.resp = requests.post(self.base_url + "books/", data=self.data)
        resp_dict = self.resp.json()
        self.data['id'] = resp_dict['id']

    def test_book_delete(self):
        resp_0 = requests.delete(self.base_url + "books/" + str(self.data['id']))
        self.assertEqual(resp_0.status_code, 204)

    def tearDown(self):
        r = requests.delete(self.base_url + "books/" + str(self.data['id']))
        print(r.status_code)



if __name__== "__main__":
    unittest.main(testRunner=HTMLTestRunner(output=r'C:\Users\ivvol\Desktop\Git bash'))
    # test1 = TestHyp('test_zero_triangle')
    # test2 = TestHyp('test_3_4_triangle')
    # test3 = TestHyp('test_3_4_triangle')
    # result1 = test1.run()
    # print(result1)
    # result2 = test2.run()
    # print(result2)
    #
    # suite = unittest.TestSuite([test1, test2]) #обьеденить тесты в suite
    # suite.addTest(test3)
    # result = unittest.TestResult()
    # suite.run(result)
    # print(result)