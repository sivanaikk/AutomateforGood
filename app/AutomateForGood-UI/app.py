import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for



app=Flask(__name__)
UPLOAD_FOLDER = r"C:\app\pem"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge'
    response.headers['Cache-Control'] = 'public, max-age=0, no-store'
    return response

@app.route('/')
def home():
        return render_template('index.html')




ALLOWED_EXTENSIONS = { 'pem'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        node_name = request.form['name']
        ip = request.form['ip']
        user_name = request.form['user_name']
        software_name = request.form['software_name']
        file = request.files['file'] 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))          
            ext=file.filename.rsplit('.', 1)[1].lower()
            cmd="/app/pingable.sh"+" "+ip
            decision=os.system(cmd)
            if os.path.isfile(r"/app/decision/pingable"):
                cmd="/app/login.sh"+" "+ip+" "+filename
                if os.path.isfile(r"/app/decision/login"):
                    cmd="/app/configure.sh"+" "+node_name+" "+ip+" "+filename+" "+user_name+" "+software_name
                    os.system(cmd)
                else:
                    return "Unable to login"
            else:
                return "There is a node with this Public IP"      
            
            # if os.path.isfile(r"/app/UI/static/ml/pred.jpg"):
            #     pred="pred.jpg"

            #     return redirect(url_for("final",name="Brain Tumor Predicted",pred=pred))
            
            # else:
            #     pred=file.filename
                # return  redirect(url_for("final",name="You are free from Brain Tumor",pred=pred))
        else:
            return  redirect("/final")
# wrong corresponds to ping , ssh issues
@app.route('/wrong')
def wrong():
    return render_template('index123.html')

#/////////////////// final means wrong file

@app.route('/final')
def final():
    return render_template('about.html')

if __name__ == '_main_':
        app.run(host='0.0.0.0')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# import os
# from flask import Flask, render_template, request, redirect, url_for
# from flask_pymongo import PyMongo
# from werkzeug.utils import secure_filename


# app=Flask(__name__)



# UPLOAD_FOLDER = r"/app/UI/static/ml/"
# @app.after_request
# def add_header(response):
#     """
#     Add headers to both force latest IE rendering engine or Chrome Frame,
#     and also to cache the rendered page for 10 minutes.
#     """
#     response.headers['X-UA-Compatible'] = 'IE=Edge'
#     response.headers['Cache-Control'] = 'public, max-age=0, no-store'
#     return response

# @app.route('/')
# def home():
#         return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if request.method == 'POST':  
#         file = request.files['file']
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
#             ext=file.filename.rsplit('.', 1)[1].lower()       
#             cmd="python3"+" "+r"/app/script.py"+" "+UPLOAD_FOLDER+file.filename
            
#             os.system(cmd)
#             if os.path.isfile(r"/app/UI/static/ml/pred.jpg"):
#                 pred="pred.jpg"

#                 return redirect(url_for("final",name="Brain Tumor Predicted",pred=pred))
#             else:
#                 pred=file.filename
#                 return  redirect(url_for("final",name="You are free from Brain Tumor",pred=pred))
#         else:
#             return  redirect("/wrong")
        


# ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# @app.route('/wrong')
# def wrong():
#     return render_template('wrong.html')
# @app.route('/final')
# def final():
#     name=request.args['name']
#     pred=request.args['pred']
#     return render_template('final.html',variable=name,filepath=pred)








# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

# if __name__ == '_main_':
#         app.run(host='0.0.0.0')