from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from chat import get_response

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, Length
from math import ceil
from urllib.parse import urlencode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Temporary data storage (replace this with a database)
hotels = [
    {'id': 1, 'name': 'Summer Suites KLCC','address': 'Mercu Summer Suites, 8, Jalan Cendana, 50250 Kuala Lumpur, Malaysia', 'price': 358, 'description': 'Summer Suites KLCC & Bukit Bintang by Purple Orchid features accommodation within 1.9 km of the centre of Kuala Lumpur.', 'amenities': ['Free Wi-Fi', 'A Kitchen with an oven', 'Room Service'], 'image': 'hotel_a_1.jpg' },
    {'id': 2, 'name': 'Genting Skyworld Hotel','address': 'Resorts World, Genting SkyWorlds, 69000 Genting Highlands, Pahang', 'price': 549, 'description': 'Resorts World Genting - Genting SkyWorlds Hotel is conveniently situated in the Genting Highlands part of Genting Highlands. It is also not far from the SkyAvenue lifestyle mall and SkyCasino.', 'amenities': ['Free Wi-Fi', 'Free Parking', 'Breakfast provided'], 'image': 'hotel_b.jpg'},
    {'id': 3, 'name': 'JonkeRED Heritage Hotel','address': 'Jalan Laksamana, Banda Hilir, 75000 Melaka', 'price': 465, 'description': 'JonkeRED Heritage Hotel is situated in Melaka, within 2.7 km of St Johns Fort and 3.9 km of Melaka Straits Mosque. This property is located a short distance from attractions such as Menara Taming Sari, Cheng Hoon Teng Temple, and Porta de Santiago.', 'amenities': ['Free Wi-Fi', 'Non-smoking rooms', 'Coffee maker in the room', 'Room service'], 'image': 'hotel_c.jpg'},
]

bookings = []
# Number of hotels to display per page
HOTELS_PER_PAGE = 3

class BookingForm(FlaskForm):
    guest_name = StringField('Guest Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=15)])
    checkin_date = DateField('Check-in Date', validators=[DataRequired()])
    checkout_date = DateField('Check-out Date', validators=[DataRequired()])
    special_requests = TextAreaField('Special Requests')
    submit = SubmitField('Book Now')

    def validate_phone_number(self, field):
        # Validate that phone_number contains only digits
        if not field.data.isdigit():
            raise ValidationError('Please enter a valid phone number.')

@app.route('/')
def home():
    # Get the page parameter from the query string
    page = request.args.get('page', 1, type=int)
    
    # Calculate the start and end indices for pagination
    start_idx = (page - 1) * HOTELS_PER_PAGE
    end_idx = start_idx + HOTELS_PER_PAGE

    # Paginate the list of hotels
    paginated_hotels = hotels[start_idx:end_idx]

    # Calculate the total number of pages
    total_pages = ceil(len(hotels) / HOTELS_PER_PAGE)

    return render_template('index.html', hotels=paginated_hotels, page=page, total_pages=total_pages)

@app.route('/hotel/<int:hotel_id>')
def hotel_detail(hotel_id):
    hotel = next((h for h in hotels if h['id'] == hotel_id), None)
    if hotel:
        return render_template('hotel_detail.html', hotel=hotel)
    flash('Hotel not found', 'warning')
    return redirect(url_for('home'))

@app.route('/book/<int:hotel_id>', methods=['GET', 'POST'])
def book(hotel_id):
    hotel = next((h for h in hotels if h['id'] == hotel_id), None)
    if hotel:
        form = BookingForm()

        if form.validate_on_submit():
            guest_name = form.guest_name.data
            email = form.email.data
            phone_number = form.phone_number.data
            checkin_date = form.checkin_date.data
            checkout_date = form.checkout_date.data
            special_requests = form.special_requests.data

            booking = {
                'hotel': hotel,
                'guest_name': guest_name,
                'email': email,
                'phone_number': phone_number,
                'checkin_date': checkin_date,
                'checkout_date': checkout_date,
                'special_requests': special_requests,
            }
            bookings.append(booking)
            flash('Booking successful!', 'success')
            #return redirect(url_for('home'))
            return redirect(url_for('confirmation', booking_id=len(bookings) - 1))

        return render_template('book.html', hotel=hotel, form=form)

    flash('Hotel not found', 'warning')
    return redirect(url_for('home'))

@app.route('/confirmation/<int:booking_id>')
def confirmation(booking_id):
    if 0 <= booking_id < len(bookings):
        booking = bookings[booking_id]
        return render_template('confirmation.html', booking=booking)
    flash('Booking not found', 'warning')
    return redirect(url_for('home'))

@app.route('/booking_history', methods=['GET'])
def booking_history():
    # For now, let's assume 'bookings' is a list containing booking details
    return render_template('booking_history.html', bookings=bookings)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/view_location/<int:hotel_id>')
def view_location(hotel_id):
    hotel = next((h for h in hotels if h['id'] == hotel_id), None)
    
    if hotel and 'address' in hotel:
        return render_template('view_location.html', hotel=hotel)
    
    flash('Location not available', 'warning')
    return redirect(url_for('home'))

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if the text is valid
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    
    app.run(debug=True)