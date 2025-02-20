from flask import Flask, redirect, url_for, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Google OAuth Config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='YOUR_GOOGLE_CLIENT_ID',
    client_secret='YOUR_GOOGLE_CLIENT_SECRET',
    access_token_url='https://oauth2.googleapis.com/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'email profile'}
)

# Admin Login Route
@app.route('/admin_login')
def admin_login():
    return google.authorize_redirect(url_for('admin_callback', _external=True))

# Google Callback
@app.route('/admin_callback')
def admin_callback():
    token = google.authorize_access_token()
    user_info = google.get('userinfo').json()
    
    # Check if admin email is allowed
    if user_info['email'] not in ['admin@example.com']:
        return "Unauthorized Access", 403
    
    session['admin'] = user_info
    return redirect(url_for('admin_dashboard'))

# Admin Dashboard
@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin' not in session:
        return redirect(url_for('admin_login'))
    
    return f"Welcome Admin {session['admin']['name']}"

# Admin Logout
@app.route('/admin_logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
