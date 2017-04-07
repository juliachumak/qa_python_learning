import requests

base_url = "http://pulse-rest-testing.herokuapp.com"
roles_url = base_url + "/roles/"
books_url = base_url + "/books/"

def particular_role_url(id):
    return roles_url + str(id) + "/"

def particular_book_url(id):
    return books_url + str(id) + "/"



roles = requests.get(roles_url)
print(roles.text)

books = requests.get(books_url)
print(books.text)

role_3 = requests.get(particular_role_url(3))
print(role_3.text)

book_4 = requests.get(particular_book_url(4))
print(book_4.text)

book_list = requests.get(books_url).json()
for book in book_list:
    print(book['title'])


# new_role = requests.post(roles_url, data={"name": "Owl", "type": "Animal", "Level": 7, "book": 1})
# print(new_role.text)

# print(requests.get(particular_role_url(57)).text)

# updated_role = requests.put(particular_role_url(57), data={"book": 2, "level": 11})
#
# print(requests.get(particular_role_url(57)).text)
#
# requests.delete(particular_role_url(57))



# new_role = requests.post(roles_url, data={"name": "Owl", "type": "Animal", "Level": 7, "book": 1})
# # print(new_role.text)
#
# new_role_id = new_role.json()['id']
#
# print(requests.get(particular_role_url(new_role_id)).text)
#
# requests.delete(particular_role_url(new_role_id))
#
# print(requests.get(particular_role_url(new_role_id)).text)



