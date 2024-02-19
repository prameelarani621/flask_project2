from flask import Flask,render_template


FAI=Flask(__name__)


@FAI.route('/send_html')

def send_html():
    return render_template('send_html.html',name='prameela')

@FAI.route('/send')

def send():
    return render_template('send.html')




if __name__=='__main__':
    FAI.run(debug=True)
