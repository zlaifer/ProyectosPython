from flask import Flask, request, jsonify
from celery import Celery

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-secret-key'

# Celery configuration
app.config['CELERY_BROKER_URL'] = 'pyamqp://guest@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def add_to_queue(message):
    return f'Message "{message}" has been added to the queue.'

@celery.task
def remove_from_queue():
    return 'No message was found in the queue.'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        result = add_to_queue.delay(message)
        return f'Result: {result.get()}'

    return jsonify({'status': 'success'})

@app.route('/dequeue', methods=['GET', 'POST'])
def dequeue():
    if request.method == 'POST':
        result = remove_from_queue.delay()
        return f'Result: {result.get()}'

    return render_template('dequeue.html')

if __name__ == '__main__':
    app.run(debug=True)