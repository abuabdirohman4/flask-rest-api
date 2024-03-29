from flask import Flask, jsonify, request, Markup

app = Flask(__name__)

@app.route('/API/get_surah/<surah_number>')
def get_surah(surah_number):

    ini = {
            "id": 23,
            "product_name": "ARIELLA",
            "barcode_id": "3CM7OCBVM395",
            "variant": "CARDIGAN",
            "colour": "Wine",
            "size": "XL",
            "hpp": 20000,
            "sell_price": 50000,
            "created_at": "2022-12-31T08:58:35.210568+07:00",
            "updated_at": "2022-12-31T08:58:35.210577+07:00",
            "tenant": "41659928-be62-4878-b5d2-297082a43cda",
            "product_id": 4
        },
    data = jsonify(ini)
    return data

@app.route('/API/save_project/', methods=['post'])
def save_project():
    request_data = request.get_json()
    # print(request_data['id'])
    request_data = request_data['size']
    return Markup(request_data)
    # return "success"
    

if __name__ == '__main__':
    app.run(port=5010, debug=True)