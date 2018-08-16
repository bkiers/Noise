from category import Category
from flask import render_template
from flask import Flask


app = Flask(__name__)
categories = Category.list(app)


@app.route("/")
def get_categories():
    return render_template('categories.html', categories=categories)


@app.route("/<category_name>")
def get_subjects(category_name):
    category = [x for x in categories if x.folder_name == category_name][0]
    return render_template('subjects.html', category=category, subjects=category.subjects)


@app.route("/<category_name>/<subject_name>")
def get_sounds(category_name, subject_name):
    category = [x for x in categories if x.folder_name == category_name][0]
    subject = [x for x in category.subjects if x.folder_name == subject_name][0]
    return render_template('sounds.html', subject=subject, sounds=subject.sounds)


if __name__ == '__main__':
    app.run()
