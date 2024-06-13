from flask import Flask
from api.akun.endpoints import akun_endpoints
from api.data_wisata.endpoints import data_wisata_endpoints
from api.kategori.endpoints import kategori_endpoints
from api.kategori.endpoints import profile_endpoints
from api.ulasan.endpoints import ulasan_endpoints
from api.wisata_favorit.endpoints import wisata_favorit_endpoints

app = Flask(__name__)

app.register_blueprint(akun_endpoints, url_prefix='/akun')
app.register_blueprint(data_wisata_endpoints, url_prefix='/data_wisata')
app.register_blueprint(kategori_endpoints, url_prefix='/kategori')
app.register_blueprint(profile_endpoints, url_prefix='/profile')
app.register_blueprint(ulasan_endpoints, url_prefix='/ulasan')
app.register_blueprint(wisata_favorit_endpoints, url_prefix='/wisata_favorit')

if __name__ == '__main__':
    app.run()
