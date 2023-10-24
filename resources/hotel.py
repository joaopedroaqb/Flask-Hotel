from flask_restful import Resource, reqparse
from models.hotel import HotelModel

hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrelas': 4.3,
        'diaria': 130.00,
        'cidade': 'Rio de Janeiro'
    },
    {
        'hotel_id': 'beta',
        'nome': 'Beta Hotel',
        'estrelas': 4.4,
        'diaria': 230.00,
        'cidade': 'São Paulo'
    },
    {
        'hotel_id': 'gama',
        'nome': 'Gama Hotel',
        'estrelas': 4.5,
        'diaria': 235.00,
        'cidade': 'Niteroi'
    }
]


class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
    
    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return{'message':'Hotel not found'}, 404 #não encontrado

    def post(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        #novo_hotel = {'hotel_id': hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200 #Ok
        hoteis.append(novo_hotel)
        return novo_hotel, 201 #Criado 

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel ['hotel_id'] != hotel_id]
        return {'message':'Hotel delete'}