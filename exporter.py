from flask import Flask, render_template
import humanreadable as hr
import speedtest

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    # Ino lab, IPA
    servers = [6766, 14623]
    threads = None

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    result = s.results.dict()

    data = {
            "download": hr.BitPerSecond(str(result['download']) + ' bit/s').mega_bps,
            "upload": hr.BitPerSecond(str(result['upload']) + ' bit/s').mega_bps,
            }

    return render_template('metric.html', result=data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
