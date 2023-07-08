


from flask import Flask, render_template, request
import random
import string
import requests

app = Flask(__name__)

def fuzz_url(url):
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    fuzzed_url = url.replace("{{FUZZ}}", random_str)
    return fuzzed_url
  
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        target_url = request.form['target_url']
        num_requests = int(request.form['num_requests'])
        response_log = []
        for _ in range(num_requests):
            fuzzed_url = fuzz_url(target_url)
            response = requests.get(fuzzed_url)
            response_log.append(fuzzed_url + ' => ' + str(response.status_code))
        return render_template('results.html', response_log=response_log)
    return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug=True)


