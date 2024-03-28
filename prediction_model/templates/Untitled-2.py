from flight_fare.credentials import *
from flight_fare.utils import transform_and_predict, predict_fare
from flight_fare.logger import logging
from flight_fare.exception import FlightFareException
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd
app = Flask(__name__)