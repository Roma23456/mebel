from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def a():
    return render_template('index.html')



@app.route("/miaki_mebli")
def a1():
    return render_template('miaki_mebli.html')

@app.route("/divan")
def a14():
    return render_template('divan.html')

@app.route("/krislo")
def a15():
    return render_template('krislo.html')

@app.route("/puf")
def a13():
    return render_template('puf.html')

@app.route("/kushetka")
def a16():
    return render_template('kushetka.html')



@app.route("/korpus_mebli")
def a2():
    return render_template('korpus_mebli.html')

@app.route("/shafa")
def a455():
    return render_template('shafa.html')

@app.route("/komoda")
def a454():
    return render_template('komoda.html')

@app.route("/stelaj")
def a44():
    return render_template('stelaj.html')

@app.route("/polochka")
def a4409():
    return render_template('polochka.html')



@app.route("/stoli_stoliki")
def a3():
    return render_template('stoli_stoliki.html')

@app.route("/obidniy_stil")
def a367():
    return render_template('obidniy_stil.html')

@app.route("/jurnal_stolik")
def a3670():
    return render_template('jurnal_stolik.html')

@app.route("/pismoviy_stil")
def a3679():
    return render_template('pismoviy_stil.html')

@app.route("/tualetniy_stolik")
def a365():
    return render_template('tualetniy_stolik.html')



@app.route("/stiltsi_krisla")
def a4():
    return render_template('stiltsi_krisla.html')

@app.route("/stiltsi")
def a468():
    return render_template('stiltsi.html')

@app.route("/barni_stiltsi")
def a46128():
    return render_template('barni_stiltsi.html')

@app.route("/ofisni_krisla")
def a46845():
    return render_template('ofisni_krisla.html')

@app.route("/kuhonni_tabureti")
def a46788():
    return render_template('kuhonni_tabureti.html')



@app.route("/mebli_spalnia")
def a5():
    return render_template('mebli_spalnia.html')

@app.route("/lijko")
def a46467():
    return render_template('lijko.html')

@app.route("/tumbochki")
def a46125668():
    return render_template('tumbochki.html')

@app.route("/zerkalo")
def a4684655():
    return render_template('zerkalo.html')

@app.route("/tumbi_vzuttia")
def a4546788():
    return render_template('tumbi_vzuttia.html')


if __name__ == "__main__":
    app.run(port=45999)