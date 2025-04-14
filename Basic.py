from packaging.markers import Operator

# Built in method
# a=1,4,3,5,7,5,9
# print(type(a))

# a=1,4,3,5,7,5,9
# print(len(a))

# a=1,4,3,5,7,5,9
# print(a.index(7))

# a=1,4,3,5,7,5,9
# print(a.count(5))

# a=1,4,3,5,7,5,9
# print(max(a))

# a=1,4,3,5,7,5,9
# print(min(a))

# a=[1,4,3,5,7,5,9]
# print(a.pop())
# print(a)

# a=[1,4,3,5,7,5,9]
# a.append(6)
# print(a)

# a=[1,4,3,5,7,5,9]
# a.insert(3,9)
# print(a)
#
# a=[1,4,3,5,7,5,9]
# a.remove(7)
# print(a)

# a=[1,4,3,5,7,5,9]
# a.reverse()
# print(a)

# a=[1,4,3,5,7,5,9]
# a.sort()
# print(a)

# a=[1,8,3,4,6,9]
# b=[2,9,7,6,1,5]
# a.extend(b)
# print(a)

# a=1,4,3,5,7,5,9
# print(max(a))

# OPERATERS

# 1/- Arithmatic Operaters

# a=10
# b=2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)

# 2/- Comparision Operator
#    i/- Eqality Operater

# a=10
# b=2
# print(a==b)
# print(a!=b)

#   ii/-Relational Operater

# a=10
# b=5
# print(a<b)
# print(a>b)
# print(a>=b)
# print(a<=b)

# 3/-Logical Operater(and,or,not)

# a=4>3 and 8>7
# print(a)

# a=4<3 and 8>7
# print(a)

# a=4>3 or 8<7
# print(a)

# a=4>3 or 8>7
# print(a)
#
# a=4<3 or 8<7
# print(a)

# a=not(2>3)
# print(a)
#
# a=not(2<3)
# print(a)

# 4/- Membership Operater (in , not in)

# a=1,4,2,5,7,9
# print(6 in a)
# print(6 not in a)

# 5/- Identify Operator(is,is not)

# a=10
# b=2
# print(a is b)
# print( a is not b)



# from datetime import date
# today = date.today()
# print("Today's date:", today)


















































































# import requests
#
# BASE_URL = "https://jsonplaceholder.typicode.com/posts"
#
# # 1️⃣ GET Request - Retrieve data
# response = requests.get(BASE_URL)
# print("GET Response:", response.json()[:2])  # Display first 2 results
# print("Status Code:", response.status_code)
#
# # 2️⃣ POST Request - Create new data
# payload = {"title": "New Post", "body": "This is a test post", "userId": 1}
# response = requests.post(BASE_URL, json=payload)
# print("POST Response:", response.json())
#
# # 3️⃣ PUT Request - Update existing data
# update_data = {"title": "Updated Title"}
# response = requests.put(f"{BASE_URL}/1", json=update_data)
# print("PUT Response:", response.json())
#
# # 4️⃣ DELETE Request - Delete a resource
# response = requests.delete(f"{BASE_URL}/1")
# print("DELETE Response Code:", response.status_code)




