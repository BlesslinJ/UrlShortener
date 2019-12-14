from flask import render_template, redirect, request, Blueprint
from .forms import UrlForm, OutForm
from .models import Urls
from .database import db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
	form = UrlForm()
	return render_template('home.html', legend = 'Shorten Your URL', form=form)


@main.route('/add_link', methods=['POST'])
def add_link():
	original_url = request.form['Original_URL']
	#short_url = request.form['Word']
	url = Urls(original_url=original_url)
	db.session.add(url)
	db.session.commit()
	form = OutForm(Original=url.original_url, New='https://127.0.0.1:5000/'+url.short_url)
	link = 'https://127.0.0.1:5000/'+url.short_url
	return render_template('link_added.html', legend = 'Here you go!Your custom short link is generated...', form = form, link = link)


@main.route('/<short_url>')
def redirect_to_url(short_url):
    url = Urls.query.filter_by(short_url=short_url).first_or_404()
    return redirect(url.original_url)     