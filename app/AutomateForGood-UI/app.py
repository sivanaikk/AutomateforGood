import os
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for



app=Flask(__name__)
UPLOAD_FOLDER = r"/app/pem"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge'
    response.headers['Cache-Control'] = 'public, max-age=0, no-store'
    return response

#Main Route

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/configure')
def configure():
    return render_template('configure.html')
    
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')


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
            cmd="sudo /app/pingable.sh"+" "+ip
            os.system(cmd)
            if os.path.isfile(r"/app/decision/pingable"):
                cmd="sudo rm -f /app/decision/pingable"
                os.system(cmd)
                cmd="sudo /app/login.sh"+" "+ip+" "+filename+" "+user_name
                os.system(cmd)
                if os.path.isfile(r"/app/decision/login"):
                    cmd="sudo rm -f /app/decision/login"
                    os.system(cmd)
                    cmd="sudo /app/configure.sh"+" "+node_name+" "+ip+" "+filename+" "+user_name+" "+software_name
                    os.system(cmd)
                    cmd="sudo rm /app/pem/"+filename
                    os.system(cmd)
                    return render_template('Thanks.html')
                else:
                    return render_template('oops-login.html')
                    # return  redirect("/nologin")
            else:
                return render_template('oops-ping.html')
                # return  redirect("/unpingable")      
        else:
            return render_template('nofile.html')
            # return  redirect("/final")



# @app.route('/unpingable')
# def unpingable():
#     return render_template('about.html')
# @app.route('/final')
# def final():
#     return render_template('about.html')

if __name__ == '_main_':
        app.run(host='0.0.0.0')
