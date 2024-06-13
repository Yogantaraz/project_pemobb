import os
from flask import Blueprint, jsonify, request
from helper.db_helper import get_connection
from helper.form_validation import get_form_data

kategori_endpoints = Blueprint('kategori', __name__)

@kategori_endpoints.route('/read', methods=['GET'])
def read():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    select_query = "SELECT * FROM kategori"
    cursor.execute(select_query)
    results = cursor.fetchall()
    cursor.close()
    return jsonify({"message": "OK", "datas": results}), 200

@kategori_endpoints.route('/create', methods=['POST'])
def create():
    required = get_form_data(["nama_kategori"])
    if isinstance(required, dict) and 'error' in required:
       return required

    nama_kategori = required["nama_kategori"]

    connection = get_connection()
    cursor = connection.cursor()
    insert_query = "INSERT INTO kategori (nama_kategori) VALUES (%s)"
    request_insert = (nama_kategori,)
    cursor.execute(insert_query, request_insert)
    connection.commit()
    new_id = cursor.lastrowid
    cursor.close()

    if new_id:
        return jsonify({"nama_kategori": nama_kategori, "message": "Inserted", "id_kategori": new_id}), 201
    return jsonify({"message": "Cant Insert Data"}), 500

@kategori_endpoints.route('/update/<id_kategori>', methods=['PUT'])
def update(id_kategori):
    nama_kategori = request.form['nama_kategori']

    connection = get_connection()
    cursor = connection.cursor()
    update_query = "UPDATE kategori SET nama_kategori=%s WHERE id_kategori=%s"
    update_request = (nama_kategori, id_kategori)
    cursor.execute(update_query, update_request)
    connection.commit()
    cursor.close()
    return jsonify({"message": "updated", "id_kategori": id_kategori}), 200

@kategori_endpoints.route('/delete/<id_kategori>', methods=['DELETE'])
def delete(id_kategori):
    connection = get_connection()
    cursor = connection.cursor()
    delete_query = "DELETE FROM kategori WHERE id_kategori = %s"
    cursor.execute(delete_query, (id_kategori,))
    connection.commit()
    cursor.close()
    return jsonify({"message": "Data deleted", "id_kategori": id_kategori})