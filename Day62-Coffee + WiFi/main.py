from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL(require_tld=True, message=None)])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5.30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_strength = SelectField('WiFi Strength Rating', choices=["✘", "📡", "📡📡", "📡📡📡", "📡📡📡📡", "📡📡📡📡📡"], validators=[DataRequired()])
    power_sockets = SelectField('Power Socket Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])

    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    cafe_form = CafeForm()
    if cafe_form.validate_on_submit():
        with open('cafe-data.csv', mode="a", encoding="utf8") as cafe_csv:
            cafe_csv.write(f"\n{cafe_form.cafe.data},"
                           f"{cafe_form.url.data},"
                           f"{cafe_form.opening_time.data},"
                           f"{cafe_form.closing_time.data},"
                           f"{cafe_form.coffee_rating.data},"
                           f"{cafe_form.wifi_strength.data},"
                           f"{cafe_form.power_sockets.data}")
        return redirect(url_for("cafes"))
    return render_template('add.html', form=cafe_form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
