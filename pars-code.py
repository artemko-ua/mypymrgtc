import tkinter as tk
import requests
from bs4 import BeautifulSoup

def get_website_info():
    url = entry.get()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    page = requests.get(url)

    content_type = page.headers.get('Content-Type', 'Тип контенту не знайдено')
    html_code = page.text
    css_code = find_css_code(html_code)
    js_code = find_js_code(html_code)
    technologies = find_technologies(html_code)

    show_result(content_type, html_code, css_code, js_code, technologies)

def find_css_code(html_code):
    css_start = html_code.find("<style>")
    css_end = html_code.find("</style>")
    if css_start != -1 and css_end != -1:
        return html_code[css_start + len("<style>") : css_end]
    else:
        return 'CSS сторінки не знайдено'

def find_js_code(html_code):
    js_start = html_code.find("<script>")
    js_end = html_code.find("</script>")
    if js_start != -1 and js_end != -1:
        return html_code[js_start + len("<script>") : js_end]
    else:
        return 'JavaScript код не знайдено'

def find_technologies(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    technologies = set()
    tags = soup.find_all()
    for tag in tags:
        technologies.add(tag.name)
    return list(technologies)

def show_result(content_type, html_code, css_code, js_code, technologies):
    result_window = tk.Toplevel(root)

    content_type_label = tk.Label(result_window, text="Тип контенту:")
    content_type_label.pack()

    content_type_text = tk.Text(result_window, wrap=tk.WORD, height=3, width=50)
    content_type_text.insert(tk.END, content_type)
    content_type_text.pack()

    html_label = tk.Label(result_window, text="HTML-код:")
    html_label.pack()

    html_text = tk.Text(result_window, wrap=tk.WORD)
    html_text.insert(tk.END, html_code)
    html_text.pack()

    css_label = tk.Label(result_window, text="CSS сторінки:")
    css_label.pack()

    css_text = tk.Text(result_window, wrap=tk.WORD)
    css_text.insert(tk.END, css_code)
    css_text.pack()

    js_label = tk.Label(result_window, text="JavaScript код:")
    js_label.pack()

    js_text = tk.Text(result_window, wrap=tk.WORD)
    js_text.insert(tk.END, js_code)
    js_text.pack()

    technologies_label = tk.Label(result_window, text="Технології:")
    technologies_label.pack()

    technologies_text = tk.Text(result_window, wrap=tk.WORD)
    technologies_text.insert(tk.END, "\n".join(technologies))
    technologies_text.pack()

root = tk.Tk()
root.title("Аналізатор сайту")

label = tk.Label(root, text="Введіть URL сайту:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Аналізувати", command=get_website_info)
button.pack()

root.mainloop()
