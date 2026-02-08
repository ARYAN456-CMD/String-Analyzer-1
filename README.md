# 🔍 String Analyzer Tool

A beautiful, modern Flask-based web application for analyzing strings with detailed metrics and transformations.

## ✨ Features

- **Secure Authentication System**
  - User login and registration
  - Password hashing with Werkzeug
  - Session management

- **Comprehensive String Analysis**
  - Character count and statistics
  - Word and line counting
  - Uppercase/lowercase/digit/special character analysis
  - Vowel and consonant counting
  - Palindrome detection
  - Word and character frequency analysis
  - Multiple text transformations (uppercase, lowercase, title case, reverse)

- **Modern UI/UX**
  - Responsive design
  - Beautiful gradient backgrounds
  - Animated cards and transitions
  - Mobile-friendly interface

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Flask==3.0.0 Werkzeug==3.0.1
```

### Step 2: Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

## 🔐 Default Login Credentials

**Username:** demo  
**Password:** demo123

## 📁 Project Structure

```
string-analyzer/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── templates/             # HTML templates
│   ├── base.html         # Base template
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   └── analyzer.html     # Main analyzer page
└── static/               # Static files
    └── css/
        └── style.css     # CSS styling
```

## 🎯 How to Use

1. **Register or Login**
   - Navigate to the login page
   - Use demo credentials or create a new account
   - Click "Login" or "Register"

2. **Analyze Your String**
   - Enter any text in the textarea
   - Click "Analyze String" button
   - View comprehensive analysis results

3. **View Results**
   - Basic statistics (characters, words, lines)
   - Character analysis (uppercase, lowercase, digits, etc.)
   - Letter analysis (vowels, consonants, palindrome check)
   - Text transformations
   - Frequency analysis

## 🛠️ Customization

### Change Secret Key
In `app.py`, update the secret key for production:
```python
app.secret_key = 'your-secure-secret-key-here'
```

### Add More Users
In `app.py`, modify the users dictionary or implement a database:
```python
users = {
    'demo': generate_password_hash('demo123'),
    'newuser': generate_password_hash('password123')
}
```

### Customize Styling
Edit `static/css/style.css` to change colors, fonts, and layout.

## 📊 Analysis Features

- **Total Characters:** Overall character count
- **Word Count:** Number of words in the text
- **Line Count:** Number of lines
- **Case Analysis:** Uppercase and lowercase character counts
- **Digit Count:** Number of numeric characters
- **Special Characters:** Count of non-alphanumeric characters
- **Vowel/Consonant Count:** Letter analysis
- **Palindrome Check:** Determines if text is a palindrome
- **Word Frequency:** Top 10 most common words
- **Character Frequency:** Top 10 most common characters
- **Text Transformations:** Uppercase, lowercase, title case, and reversed text

## 🔒 Security Notes

- Passwords are hashed using Werkzeug's security functions
- Session management for authenticated users
- CSRF protection (add Flask-WTF for production)
- For production, use a proper database instead of in-memory user storage

## 🚀 Production Deployment

For production deployment:
1. Use a proper database (PostgreSQL, MySQL, or SQLite)
2. Set `debug=False` in app.py
3. Use environment variables for secret keys
4. Implement HTTPS
5. Add rate limiting
6. Use a production WSGI server (gunicorn, uWSGI)

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and submit pull requests!

## 📧 Support

For issues or questions, please create an issue in the repository.

---

**Enjoy analyzing your strings! 🎉**
