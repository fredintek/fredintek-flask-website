from flask import render_template, url_for, flash, redirect
from fredintek import app, mail
from fredintek.forms import ContactForm
from flask_mail import Message


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/portfolio', methods=['GET', 'POST'])
def portfolio():
    return render_template('portfolio.html', title='Portfolio')


@app.route('/tutorials', methods=['GET', 'POST'])
def tutorials():
    return render_template('tutorials.html', title='Tutorials')


def send_mail(user_info):
    msg = Message('Contact Form From Fredintek.com', recipients=['fredintek@gmail.com'])
    msg.body = f'''
Hello There, 
You just recieved an email from your website!!

        {user_info.get('subject')}

From (Name: {user_info.get('name')}, Email: {user_info.get('email')})

{user_info.get('message')}

'''
    mail.send(msg)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        user_info = dict()
        user_info['name'] = form.username.data
        user_info['email'] = form.email.data
        user_info['subject'] = form.subject.data
        user_info['message'] = form.message.data
        send_mail(user_info)
        flash('You have successfully sent a message to my email', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', title='Contact', form=form)
