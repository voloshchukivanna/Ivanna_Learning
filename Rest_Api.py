import requests
import _json

url='http://pulse-rest-testing.herokuapp.com/'
r = requests.get(url)
print(r.status_code)

'''создание книги'''
book_dict = {'title': "new book",'author': "Petr"}
resp = requests.post(url+'books/', data=book_dict)
req_dict = resp.json()
book_id=req_dict['id']

'''редактирование книги'''
resp = requests.put(url+'books/'+str(book_id), data={'title':'edit book'})
req_dict = resp.json()

'''удаление книги'''
del_book = requests.delete(url + 'books/' + str(book_id))

'''создание роли'''
role_dict = {'name':'Ivanna', 'type':'Voloshchuk', 'level':'21'}
role_dict['book'] = book_id
resp_2 = requests.post(url+'roles/', data=role_dict)
req_role = resp_2.json()
role_id=req_role['id']

'''редактирование роли'''
resp_2 = requests.put(url+'roles/'+str(role_id), data={'name':'Nelly'})
req_role = resp_2.json()

'''удаление роли'''
del_role = requests.delete(url+'roles/'+str(role_id))