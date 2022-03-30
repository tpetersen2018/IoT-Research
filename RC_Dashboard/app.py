#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

DISP_LINES = 4

def read_data_files():
    rows1 = open('data/data1.csv').readlines()[-DISP_LINES:]
    rows2 = open('data/data2.csv').readlines()[-DISP_LINES:]
    rows3 = open('data/data3.csv').readlines()[-DISP_LINES:]
    rows4 = open('data/data4.csv').readlines()[-DISP_LINES:]
    rows5 = open('data/data5.csv').readlines()[-DISP_LINES:]
    rows6 = open('data/data6.csv').readlines()[-DISP_LINES:]
    return rows1,rows2,rows3,rows4,rows5,rows6

@app.route('/', methods=['GET'])
def index():
    rows1,rows2,rows3,rows4,rows5,rows6=read_data_files()
    return render_template('index.html',rows1=rows1,rows2=rows2,rows3=rows3,rows4=rows4,rows5=rows5,rows6=rows6)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3333')
