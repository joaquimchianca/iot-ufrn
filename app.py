from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/receive_data', methods=['POST'])
def receive_data():
    value = request.form['value']
    print("Received value:", value)
    cmd = 'zabbix_sender -vv -z 127.0.0.1 -s "node" -k sound -o ' + str(value)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output = process.communicate()
    print(output)
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083)



