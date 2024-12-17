from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "sdfghfsdjhghoidfghoidf54981542sd---__--(-(()))" 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookshelf.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Model User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

# Model Book
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    year_published = db.Column(db.Integer)
    status = db.Column(db.String(50), nullable=False)
    review = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Routes
@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')  # Use Bcrypt to hash the password

        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
            return redirect(url_for('signup'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.check_password_hash(user.password, password):  # Use Bcrypt to check the password
            flash("Invalid username or password", "danger")
            return redirect(url_for('login'))

        session['user_id'] = user.id
        session['username'] = user.username
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for('login'))
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    # Handle the search query
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)

    # Query the books table and apply the search filter
    books_query = Book.query.filter(Book.title.contains(search_query) | Book.author.contains(search_query))

    # Paginate the books
    books = books_query.paginate(page=page, per_page=5, error_out=False)

    return render_template('dashboard.html', books=books, search_query=search_query)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year_published = request.form['year_published']
        status = request.form['status']
        review = request.form['review']

        new_book = Book(
            title=title,
            author=author,
            genre=genre,
            year_published=year_published,
            status=status,
            review=review,
            user_id=session['user_id']
        )
        db.session.add(new_book)
        db.session.commit()
        flash("Book added successfully!", "success")
        return redirect(url_for('dashboard'))

    return render_template('add_book.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    book = Book.query.get_or_404(book_id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.year_published = request.form['year_published']
        book.status = request.form['status']
        book.review = request.form['review']

        db.session.commit()
        flash("Book updated successfully!", "success")
        return redirect(url_for('dashboard'))

    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:book_id>')
def delete_book(book_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    flash("Book deleted successfully!", "success")
    return redirect(url_for('dashboard'))
# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)