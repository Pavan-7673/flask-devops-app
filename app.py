from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
        <body style="font-family: Arial; text-align: center; margin-top: 100px;">
            <h1>Welcome to My DevOps App!</h1>
            <p>Deployed with Docker, Kubernetes and Helm</p>
            <p>Built by Pavan Reddy</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
