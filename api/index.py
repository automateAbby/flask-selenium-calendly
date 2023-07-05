from flask import Flask
from flask import request
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello! If this api wont work, contact me at automate.abby@gmail.com'

@app.route('/schedule/', methods = ['POST'])
def automate():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            url = str(request.form.get('url'))
            browser.get('https://calendly.com/automate-abby/meeting-appointment/2023-07-05T00:00:00Z')
            inputEl = browser.find_element_by_id('full_name_input').send_keys(name)
            inputEl = browser.find_element_by_id('email_input').send_keys(email)
            inputEl.submit()
            return format(browser.title)
        finally:
            browser.quit()
