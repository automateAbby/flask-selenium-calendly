import asyncio
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
def home():
    return 'Hello, World!'

@app.route('/schedule/', methods=['POST'])
async def automate():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            url = str(request.form.get('url'))

            await asyncio.sleep(0)  # Allow other tasks to run (if any)

            browser.get(url)
            inputEl = browser.find_element_by_id('full_name_input').send_keys(name)
            inputEl = browser.find_element_by_id('email_input').send_keys(email)
            inputEl.submit()
            await asyncio.sleep(0)  # Allow time for the submission to complete (if necessary)
            return format(browser.title)
        finally:
            browser.quit()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.ensure_future(app.run(debug=True)))
