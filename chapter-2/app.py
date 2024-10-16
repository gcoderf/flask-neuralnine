from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/fayza', methods=['GET', 'POST']) # Mendeklarasikan method yang diperbolehkan
def fayza():
    if request.method == 'GET':
        return 'You are using GET'
    elif request.method == 'POST':
        return 'You are using POST'
    else:
        return 'Never seen'

@app.route('/hello')
def hello():
    response = make_response('Hello, World!') # Membuat response
    response.status_code = 202 # Mengubah status code
    response.headers['content-type'] = 'text/plain' # Menambahkan header
    return response # Mengembalikan response


@app.route('/user/<name>')
def user(name):
    return f'Hello, {name}!'

@app.route('/add/<int:num1>/<int:num2>') # Mendeklarasikan variabel num1 dan num2 sebagai integer
def add(num1, num2):

    # Mendeklarasikan variabel num1 dan num2 sebagai integer
    #num1 = int(num1)
    #num2 = int(num2)
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/handle_url_params') # http://127.0.0.1:5555/handle_url_params?name=mike&greeting=helo
def handle_url_params():
    if 'greeting' in request.args and 'name' in request.args: # Mengecek apakah ada greeting dan name di URL
        greeting = request.args['greeting'] # Mengambil nilai dari greeting
        name = request.args.get('name') # Mengambil nilai dari name
        return f'{greeting}, {name}!' # Mengembalikan nilai
    else:
        return 'No greeting or name provided'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555, debug=True) # Menjalankan aplikasi Flask pada host


