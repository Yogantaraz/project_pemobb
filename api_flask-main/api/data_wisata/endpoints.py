import os
from flask import Blueprint, jsonify, request
from helper.db_helper import get_connection
from helper.form_validation import get_form_data

data_wisata_endpoints = Blueprint('data_wisata', __name__)

@data_wisata_endpoints.route('/read', methods=['GET'])
def read():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    select_query = "SELECT * FROM data_wisata"
    cursor.execute(select_query)
    results = cursor.fetchall()
    cursor.close()
    return jsonify({"message": "OK", "datas": results}), 200

@data_wisata_endpoints.route('/create', methods=['POST'])
def create():
    required = get_form_data(["nama_wisata", "deskripsi", "gambar", "video", "rating_wisata", "maps", "id_kategori"])
    if isinstance(required, dict) and 'error' in required:
        return required

    nama_wisata = required["nama_wisata"]
    deskripsi = required["deskripsi"]
    gambar = required["gambar"]
    video = required["video"]
    rating_wisata = required["rating_wisata"]
    maps = required["maps"]
    id_kategori = required["id_kategori"]

    connection = get_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO data_wisata (nama_wisata, deskripsi, gambar, video, rating_wisata, maps, id_kategori) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    request_insert = (nama_wisata, deskripsi, gambar, video, rating_wisata, maps, id_kategori)
    cursor.execute(insert_query, request_insert)
    connection.commit()
    new_id = cursor.lastrowid
    cursor.close()

    if new_id:
        return jsonify({"nama_wisata": nama_wisata, "message": "Inserted", "id_wisata": new_id}), 201
    return jsonify({"message": "Cant Insert Data"}), 500

@data_wisata_endpoints.route('/update/<id_wisata>', methods=['PUT'])
def update(id_wisata):
    nama_wisata = request.form['nama_wisata']
    deskripsi = request.form['deskripsi']
    gambar = request.form['gambar']
    video = request.form['video']
    rating_wisata = request.form['rating_wisata']
    maps = request.form['maps']
    id_kategori = request.form['id_kategori']

    connection = get_connection()
    cursor = connection.cursor()
    update_query = "UPDATE data_wisata SET nama_wisata=%s, deskripsi=%s, gambar=%s, video=%s, rating_wisata=%s, maps=%s, id_kategori=%s WHERE id_wisata=%s"
    update_request = (nama_wisata, deskripsi, gambar, video, rating_wisata, maps, id_kategori, id_wisata)
    cursor.execute(update_query, update_request)
    connection.commit()
    cursor.close()
    return jsonify({"message": "updated", "id_wisata": id_wisata}), 200

@data_wisata_endpoints.route('/delete/<id_wisata>', methods=['DELETE'])
def delete(id_wisata):
    connection = get_connection()
    cursor = connection.cursor()
    delete_query = "DELETE FROM data_wisata WHERE id_wisata = %s"
    cursor.execute(delete_query, (id_wisata,))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Data deleted", "id_wisata": id_wisata})
