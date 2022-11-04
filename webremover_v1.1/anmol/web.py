import os
from flask import Flask, redirect, url_for, render_template, request
from rembg import remove
from PIL import Image
app = Flask(__name__)



@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        imgInput = request.form["nm"]
        bgrevomer(imgInput)
        return redirect(url_for("image", n=imgInput))
    else:
        return render_template("login.html")



def bgrevomer(input_path):
    baspath = os.path.basename(input_path)
    outputName = baspath.split('.')[0]
    outputName = outputName.replace(" ","-")
    output_path = f'static\image\{outputName}.png'
    input = Image.open(input_path)
    output = remove(input)
    output = output.save(output_path)
    return outputName

@app.route("/<n>")
def image(n):
    baspath = os.path.basename(n)
    outputName = baspath.split('.')[0]
    outputName = outputName.replace(" ","-")
    output_path = f'static\image\{outputName}.png'
    return render_template("image.html",outpath=output_path)

if __name__ == "__main__":
    app.run(debug=True)