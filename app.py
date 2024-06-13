#this will be a resource management app for your real life
#it can be used to manage your resources like books, movies, food, money, etc

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import spacy

app = Flask(__name__)
api = Api(app) 
