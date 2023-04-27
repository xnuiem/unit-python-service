from flask import request, jsonify
from apiflask import APIFlask
from src.error import InvalidUsage
from src.config import Config
from src.data import DataSource
from src.logger import Logger


app = APIFlask(__name__, spec_path='/spec')
app.config.from_object(Config)
app.config['SPEC_FORMAT'] = 'yaml'
app.config['AUTO_404_RESPONSE'] = False


logger = Logger(Config).logger
data_obj = DataSource(Config, logger)






@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error_obj):
    response = jsonify(error_obj.to_dict())
    response.status_code = error_obj.status_code
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
