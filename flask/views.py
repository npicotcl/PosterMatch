from flaskexample import app
import pandas as pd
from flask import request, redirect
import os
import os.path
from flask import flash
from flask import Flask, url_for
from flask import render_template
from werkzeug.utils import secure_filename
import datetime

##### Import functions that will be called to find nearest neighbors
sys.path.append('$ProjectDir/')

##### Find k-NN for similar Images
import ClosestNeighboorPoster

##### Find k-NN for similar Synopsis
import ClosestNeighboorSynopsis

##### Find k-NN for similar Synopsis
import ClosestNeighboorSynopsisPlusPoster
import ClosestNeighboor2Posters

import gensim

##### Import and load VGG16 and Word2Vec 
from VGG16_PretrainedV1 import VGG16

base_modelImg = VGG16(weights='imagenet')
model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

##### Main page
@app.route('/')
@app.route('/index')
def index():

    ##### Homepage reinitializes input images
    bashCommandrm = "rm -f static/img/Image1.jpg"
    os.system(bashCommandrm)
    bashCommandrm2 = "rm -f static/img/Image2.jpg"
    os.system(bashCommandrm2)
    bashCommandrm3 = "rm -f static/img/Image3.jpg"
    os.system(bashCommandrm3)
    
    return render_template("index.html")

##### Definition of upload folder and allowed file extensions to upload
UPLOAD_FOLDER = '/static/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
##### Define upload function for Image1
@app.route('/index', methods=['GET', 'POST'])
def upload():
    boolupload2=False
    boolupload=False
     
    if request.method == 'POST':
        now = datetime.datetime.now()
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            bashCommand = "mv static/img/%s static/img/Image1.jpg" % filename
            os.system(bashCommand)

            boolupload=True

            return render_template("index.html", boolupload2=boolupload2, boolupload=boolupload, filename='static/img/Image1.jpg?%s%s%s' % (now.hour, now.minute, now.second), filename2='static/img/Image2.jpg?%s%s%s' % (now.hour, now.minute, now.second), filename3='static/img/Image3.jpg?%s%s%s' % (now.hour, now.minute, now.second))

    return render_template('index.html')    

##### Define upload function for Image2
@app.route('/upload2', methods=['GET', 'POST'])
def upload2():
    boolupload2=False
    boolupload=False
    
    print("Upload2")  
    if request.method == 'POST':
        now = datetime.datetime.now()
        # check if the post request has the file part
        if 'file2' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file2 = request.files['file2']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file2 and allowed_file(file2.filename):
            filename2 = secure_filename(file2.filename)
            file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            bashCommand = "mv static/img/%s static/img/Image2.jpg" % filename2
            os.system(bashCommand)

            boolupload2=True

            return render_template("index.html", boolupload2=boolupload2, boolupload=boolupload, filename='static/img/Image1.jpg?%s%s%s' % (now.hour, now.minute, now.second), filename2='static/img/Image2.jpg?%s%s%s' % (now.hour, now.minute, now.second), filename3='static/img/Image3.jpg?%s%s%s' % (now.hour, now.minute, now.second))

    return render_template('index.html')    
    
##### Define upload function for Image3
@app.route('/upload3', methods=['GET', 'POST'])
def upload3():
    boolupload2=False
    boolupload=False
     
    if request.method == 'POST':
        now = datetime.datetime.now()
        # check if the post request has the file part
        if 'file3' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file3 = request.files['file3']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file3.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file3 and allowed_file(file3.filename):
            filename3 = secure_filename(file3.filename)
            file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename3))
            bashCommand = "mv static/img/%s static/img/Image3.jpg" % filename3
            os.system(bashCommand)

            boolupload2=True

            return render_template("index.html", boolupload2=boolupload2, boolupload=boolupload, filename='static/img/Image1.jpg?%s%s%s' % (now.hour, now.minute, now.second), filename2='static/img/Image2.jpg?%s%s%s' % (now.hour, now.minute, now.second), filename3='static/img/Image3.jpg?%s%s%s' % (now.hour, now.minute, now.second))

    return render_template('index.html')        
    
##### Define output which calls the appropriate function to find nearest neighbors of an Image and/or Text inserted by a user
@app.route('/output')
def output():
    
    bool2=False
    bool1=True
    now = datetime.datetime.now()
    genre = request.args.get('genre')
    country = request.args.get('country')
    date2 = request.args.get('date2')
    date1 = request.args.get('date1')
    
    ##### By default date min and max are 2000 and 2017
    if(request.args.get('date1')):
        date1 = request.args.get('date1')
    else:
        date1=2000
    
    if(request.args.get('date2')):
        date2 = request.args.get('date2')
    else:
        date2=2017
    
    ##### By default the production country is US
    if(request.args.get('country')):
        country = request.args.get('country')
    else:
        country='US'
    
    date1=int(date1)
    date2=int(date2)
    pitchbool=False
    
    ############### if pitch inserted by user pitchbool = true:
    if(request.args.get('pitch')):
        pitch=request.args.get('pitch')
        pitchbool=True

    moviepath=""    
    index=""
    moviepath2=""
    index2=""
    movie_poster = "static/img/Image1.jpg"
    
    ##### Call function ClosestNeighboorPoster if only poster uploaded
    if(os.path.isfile(movie_poster) and pitchbool==False):
        moviepath, index=ClosestNeighboorPoster.ShowkNN(movie_poster, genre, country, "Range", date1, date2, base_modelImg)
    
    ##### Call function ClosestNeighboorSynopsisPlusPoster if both poster uploaded and synopsis inserted
    if(os.path.isfile(movie_poster)==True and pitchbool==True):
        moviepath, index=ClosestNeighboorSynopsisPlusPoster.ShowkNN(pitch, movie_poster, genre, country, "Range", date1, date2, base_modelImg, model)
        return render_template("OutputNew.html", bool2=bool2, bool1=bool1, text=True, moviepath = moviepath, index=index, moviepath2 = moviepath2, index2=index2, filename="static/img/Image1.jpg?%s%s%s" % (now.hour, now.minute, now.second))    

    ##### Call function ClosestNeighboorSynopsis if only synopsis inserted
    if(os.path.isfile(movie_poster)==False and pitchbool==True):        
        moviepath, index=ClosestNeighboorSynopsis.ShowkNN(pitch, genre, country, "Range", date1, date2, model)
        return render_template("OutputNew.html", bool2=bool2, bool1=bool1, text=True, moviepath = moviepath, index=index, moviepath2 = moviepath2, index2=index2, filename="static/img/Image1.jpg?%s%s%s" % (now.hour, now.minute, now.second))    
  
    return render_template("OutputNew.html", bool2=bool2, bool1=bool1, moviepath = moviepath, index=index, moviepath2 = moviepath2, index2=index2, filename="static/img/Image1.jpg?%s%s%s" % (now.hour, now.minute, now.second))    
    
##### Define output which calls the function to find nearest neighbors of two convoluted Images inserted by a user    
@app.route('/output2posters')
def output2():
    bool2=True
    bool1=False
    now = datetime.datetime.now()
    genre = request.args.get('genre')
    country = request.args.get('country')
    date2 = request.args.get('date2')
    date1 = request.args.get('date1')
    
    ##### By default date min and max are 2000 and 2017
    if(request.args.get('date1')):
        date1 = request.args.get('date1')
    else:
        date1=2000
    
    if(request.args.get('date2')):
        date2 = request.args.get('date2')
    else:
        date2=2017
    
    ##### By default the production country is US
    if(request.args.get('country')):
        country = request.args.get('country')
    else:
        country='US'
    
    ##### By default the weights are 0.5
    weight2 = request.args.get('weight2')
    
    if(request.args.get('weight2')):
        weight2 = request.args.get('weight2')
    else:
        weight2=0.5

    weight1 = request.args.get('weight1')    
    if(request.args.get('weight1')):
        weight1 = request.args.get('weight1')
    else:
        weight1=0.5
       
    weight2=float(weight2)
    weight1=float(weight1)
    date1=int(date1)
    date2=int(date2)
    moviepath2=""
    index2=""
    moviepath=""
    index=""
    movie_poster2 = "static/img/Image2.jpg"
    movie_poster3 = "static/img/Image3.jpg"
    
    ##### If both posters are uploaded, call function ClosestNeighboor2Posters
    if(os.path.isfile(movie_poster2)==True and os.path.isfile(movie_poster3)==True):
        moviepath2, index2=ClosestNeighboor2Posters.ShowkNN(movie_poster2, movie_poster3, genre, country, "Range", date1, date2, weight1, weight2, base_modelImg)
    
    return render_template("OutputNew.html", bool2=bool2, bool1=bool1, moviepath=moviepath, index=index, moviepath2 = moviepath2, index2=index2, filename2='static/img/Image2.jpg?%s%s%s' % (now.hour, now.minute, now.second), filename3='static/img/Image3.jpg?%s%s%s' % (now.hour, now.minute, now.second)) 
    
    