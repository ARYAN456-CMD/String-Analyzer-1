from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import re
from collections import Counter

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Simple user database (in production, use a real database)
users = {
    'demo': generate_password_hash('demo123')
}

def analyze_string(text):
    """Analyze the input string and return various metrics"""
    if not text:
        return None
    
    analysis = {
        'original': text,
        'length': len(text),
        'char_count': len(text),
        'word_count': len(text.split()),
        'line_count': len(text.splitlines()),
        'uppercase_count': sum(1 for c in text if c.isupper()),
        'lowercase_count': sum(1 for c in text if c.islower()),
        'digit_count': sum(1 for c in text if c.isdigit()),
        'space_count': sum(1 for c in text if c.isspace()),
        'special_char_count': sum(1 for c in text if not c.isalnum() and not c.isspace()),
        'vowel_count': sum(1 for c in text.lower() if c in 'aeiou'),
        'consonant_count': sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou'),
        'reversed': text[::-1],
        'uppercase': text.upper(),
        'lowercase': text.lower(),
        'title_case': text.title(),
        'word_frequency': dict(Counter(text.lower().split()).most_common(10)),
        'char_frequency': dict(Counter(text).most_common(10)),
        'is_palindrome': text.replace(' ', '').lower() == text.replace(' ', '').lower()[::-1],
        'starts_with': text[0] if text else '',
        'ends_with': text[-1] if text else '',
    }
    
    return analysis

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('analyzer'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('analyzer'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if username in users:
            flash('Username already exists', 'error')
        elif password != confirm_password:
            flash('Passwords do not match', 'error')
        elif len(password) < 6:
            flash('Password must be at least 6 characters', 'error')
        else:
            users[username] = generate_password_hash(password)
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/analyzer', methods=['GET', 'POST'])
def analyzer():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    analysis_result = None
    input_text = ''
    
    if request.method == 'POST':
        input_text = request.form.get('input_text', '')
        if input_text:
            analysis_result = analyze_string(input_text)
    
    return render_template('analyzer.html', 
                         username=session['username'],
                         analysis=analysis_result,
                         input_text=input_text)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
