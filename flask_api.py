# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,request, render_template
import pyscreenshot

app = Flask(__name__)



@app.route("/")
def index():
    try:
        # To capture the screen
        image = pyscreenshot.grab()
          
        # To display the captured screenshot
        image.show()
          
        # To save the screenshot
        # image.save(r"C:\Users\tapan.gupta\Desktop\t1.png")


    except:
        print('Screenshot saved successfully')



if __name__ == '__main__':
    app.run()
    
