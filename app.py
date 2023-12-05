from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def format_output(output):
    # Replace newline characters with <> tags
    return output.replace('\n', '<br>')

@app.route('/start', methods=['POST'])
def start():
    try:
        result = subprocess.run(['python', 'in-weihu.py', 'start'], text=True, capture_output=True, check=True)
        return f"Start operation initiated. Output: <pre>{format_output(result.stdout)}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Error: {format_output(e.stdout)}"

@app.route('/stop', methods=['POST'])
def stop():
    try:
        result = subprocess.run(['python', 'in-weihu.py', 'stop'], text=True, capture_output=True, check=True)
        return f"Stop operation initiated. Output: <pre>{format_output(result.stdout)}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Error: {format_output(e.stdout)}"

@app.route('/test', methods=['POST'])
def test():
    try:
        result = subprocess.run(['python', 'in-weihu.py', 'test'], text=True, capture_output=True, check=True)
        return f"Test operation initiated. Output: <pre>{format_output(result.stdout)}</pre>"
    except subprocess.CalledProcessError as e:
        return f"Error: {format_output(e.stdout)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
