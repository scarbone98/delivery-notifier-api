from flask import Flask, request, jsonify
from database_helper import check_zip_store_exists, add_new_store
from time import time

app = Flask(__name__)

cache = {}


@app.route('/getAddress')
def get_time_slots():
    zip_code = request.args.get('zipCode')

    # Pull from cache if it has been in the last 5 minutes
    if zip_code in cache and cache['updated_at'] - time() < 60 * 5:
        return cache[zip_code], 200

    store_info = check_zip_store_exists(zip_code)

    # If the store data isn't present in the database then fetch it
    if not store_info['time_slots']:
        store_info = add_new_store(zip_code)

    if not store_info['error_message']:
        cache[zip_code] = store_info
        cache['updated_at'] = time()

    return store_info, 500 if store_info["error_message"] else 200


if __name__ == '__main__':
    app.run(debug=True)
