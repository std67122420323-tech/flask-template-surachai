from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  title = 'Home Page' 
  return render_template('index.html',title=title)

@app.route('/about')
def about():
  title = 'About Page'
  name = 'Surachai Namsang'
  gmail = 'std.67122420323@ubru.ac.th'
  mobile = '0815673245'
  age = 21
  return render_template('about.html', title=title, name=name, gmail=gmail, mobile=mobile, age=age)

@app.route('/favorite/foods')
def favorite_foods():
  title = 'Favorite Foods Page'
  foods = ['ข้าวต้ม', 'กะเพราไก่', 'หมูทอดกระเทียม', 'ข้าวไข่เจียว', 'ส้มตำ']
  return render_template('favorite_foods.html', title=title, foods=foods)

@app.route('/favorite/sport')
def favorite_sport():
  title = 'Favorite Sport Page'
  sport = ['ฟุตบอล', 'ฟุตซอล', 'ว่ายน้ำ']
  return render_template('favorite_sport.html', title=title, sport=sport)

@app.route('/favorite/movies')
def favorite_movies():
  title = 'Favorite Movies Page'
  movies = ['ไอรอนแมน', 'ผู้กล้าโล่', 'ผู้กล้าสายฮีล','คมแฝก', 'แบทแมน']
  return render_template('favorite_movies.html', title=title, movies=movies)