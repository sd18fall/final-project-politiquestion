from flask import Flask
app = Flask(__name__)

from flask import render_template
from flask import redirect, url_for, request
ZIPcode=0
@app.route('/')
def zipentry():
    return render_template('zipcode3.html')
    
@app.route('/ZIP', methods =['POST', 'GET'])
def ZIP():
    Zip = request.form['ZIP'] 
    global ZIPcode
    ZIPcode = Zip
    return redirect(url_for('questions'))

@app.route('/questions', methods = ['POST'])
def questions():
    Votes=['test question', 'happy days', 'yellow']
    Vote1=Votes[0]
    Vote2=Votes[1]
    Vote3=Votes[2]
    return render_template('ZIPquestionaire2.html', Vote1=Vote1, Vote2=Vote2, Vote3=Vote3)
    
@app.route('/results', methods = ['POST'])
def results():
    Q1 = request.form['Q1']
    
    Q2 = request.form['happy']
    
    Q3 = request.form['sad']
    
    Score = "input variable here"
    
    return render_template('Results2.html', Score=Score, UserScore1=Q1, RepScore1="yes", 
                           UserScore2=Q2, RepScore2= "no",UserScore3=Q3, RepScore3="yes")

zipsaved=0
if __name__ == '__main__':
    app.run()