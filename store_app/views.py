from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# from deal_in_v2.middleware import jwtRequired
from deal_in_v2.jwt import JWTAuth
import json
import requests
from pprint import pprint


