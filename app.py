from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('Database_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)

    def __repr__(self):
        return f"Message('{self.name}', '{self.email}', '{self.subject}', '{self.date_sent}')"

app.config['SECRET_KEY'] = os.getenv('Secret_key')

@app.route('/')
def home():
    return render_template('home.html')  # this file extends base.html

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
    
        if not name or not email or not message:
            flash('Please fill in all required fields (Name, Email, Message).', 'danger')
            return render_template('contact.html', active_page='contact')

        try:
            # Save message to database
            new_message = ContactMessage(name=name, email=email, subject=subject, message=message)
            db.session.add(new_message)
            db.session.commit()

            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('contact')) # Redirect to prevent resubmission on refresh
        except Exception as e:
            db.session.rollback() # Rollback in case of error
            print(f"Error processing contact form: {e}")
            flash('There was an error sending your message. Please try again later.', 'danger')
            return render_template('contact.html', active_page='contact')

    return render_template('contact.html', active_page='contact')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
