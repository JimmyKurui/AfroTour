from flask import Blueprint, request, jsonify

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return "Hello"

@views.route('/destinations', methods=['GET', 'POST'])
def destinations():
    if request.method == 'GET':
        # Handle GET request to retrieve destinations
        destinations = db.session.query(
            Destination.id,
            Destination.Country,
            Destination.area,
            Destination.Attraction,
            Destination.Accommodations,
            Destination.Activities,
            Destination.Travel_Tips,
            Destination.Transportation,
            WKTElement(Destination.Geographic_Information).ST_AsText().label('Geographic_Information')
        ).all()

        destination_list = []
        for destination in destinations:
            destination_data = {
                'id': destination.id,
                'Country': destination.Country,
                'area': destination.area,
                'attraction': destination.Attraction,
                'Accommodations': destination.Accommodations,
                'Activities': destination.Activities,
                'Travel_Tips': destination.Travel_Tips,
                'Transportation': destination.Transportation,
                'Geographic_Information': destination.Geographic_Information,
            }
            destination_list.append(destination_data)
        return jsonify(destination_list)
    elif request.method == 'POST':
        # Handle POST request to create a new destination
        data = request.json  # Assuming JSON data is sent in the request body
        new_destination = Destination(
            Country=data.get('Country'),
            area=data.get('area'),
            Geographic_Information=WKTElement(data.get('Geographic_Information')),
            Attraction=data.get('attraction'),
            Accommodations=data.get('Accommodations'),
            Activities=data.get('Activities'),
            Travel_Tips=data.get('Travel_Tips'),
            Transportation=data.get('Transportation')
        )

        db.session.add(new_destination)
        db.session.commit()
        return jsonify({'message': 'Destination created successfully'}), 201


@views.route('/destinations/<int:id>', methods=['GET'])
def get_destination(id):
    destination = Destination.query.get(id)
    if destination:
        destination_data = {
            'id': destination.id,
            'Country': destination.Country,
            'area': destination.area,
            'Attraction': destination.Attraction,
            'Accommodations': destination.Accommodations,
            'Activities': destination.Activities,
            'Travel_Tips': destination.Travel_Tips,
            'Transportation': destination.Transportation,
            'Geometry': destination.Geometry
        }
        return jsonify(destination_data)
    return jsonify({'message': 'Destination not found'}), 404