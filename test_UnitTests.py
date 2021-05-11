import unittest
import requests
from triangle import hyp


class TestHyp(unittest.TestCase):
    def test_zero_triangle(self):
        r = hyp(0, 0)
        self.assertEqual(0, r)

    def test_3_4_triangle(self):
        r = hyp(3, 4)
        self.assertEqual(5, r)


class TestBookCreate(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://pulse-rest-testing.herokuapp.com/"

    def test_book_create(self):
        data = {"title":"unittest","author":"Petr"}
        resp = requests.post(self.base_url + "books/", data=data)
        self.assertEqual(201, resp.status_code)
        resp_dict = resp.json()
        self.book_id = resp_dict['id']
        self.assertEqual(data, resp_dict)
        # self.assertEqual(data["title"], resp_dict["title"])
        # self.assertEqual(data["author"], resp_dict["author"])

    def tearDown(self) -> None:
        r = requests.delete(self.base_url + "books/" + str(self.book_id))
        print(r.status_code)




if __name__== "__main__":
    unittest.main()