from flask import Flask, jsonify, request, abort
import csv
import os

app = Flask(__name__)

# CSV file to store car data
CSV_FILE = "cars.csv"

# Token for authentication
AUTH_TOKEN = "secret_token"

# Helper function to load the CSV file
def load_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Make", "Model", "Year", "Color"])
    cars = []
    with open(CSV_FILE, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cars.append(row)
    return cars

# Helper function to save the CSV file
def save_csv(cars):
    with open(CSV_FILE, mode="w", newline="") as file:
        fieldnames = ["ID", "Make", "Model", "Year", "Color"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cars)

# Helper function to validate token
def validate_token():
    token = request.headers.get("Authorization")
    if token != AUTH_TOKEN:
        abort(401, description="Unauthorized: Invalid token")

# CRUD Operations

# Create a new car
@app.route("/cars", methods=["POST"])
def create_car():
    validate_token()
    data = request.json
    if not data or not all(key in data for key in ["make", "model", "year", "color"]):
        abort(400, description="Invalid input: Ensure 'make', 'model', 'year', and 'color' are provided.")

    cars = load_csv()
    new_id = len(cars) + 1  # Auto-generate ID
    new_car = {
        "ID": new_id,
        "Make": data["make"],
        "Model": data["model"],
        "Year": data["year"],
        "Color": data["color"]
    }
    cars.append(new_car)
    save_csv(cars)

    return jsonify({"message": "Car created successfully", "id": new_id}), 201

# Read all cars
@app.route("/cars", methods=["GET"])
def get_cars():
    validate_token()
    cars = load_csv()
    return jsonify(cars)

# Read a specific car by ID
@app.route("/cars/<int:car_id>", methods=["GET"])
def get_car(car_id):
    validate_token()
    cars = load_csv()
    for car in cars:
        if int(car["ID"]) == car_id:
            return jsonify(car)
    abort(404, description="Car not found")

# Update a car by ID
@app.route("/cars/<int:car_id>", methods=["PUT"])
def update_car(car_id):
    validate_token()
    data = request.json
    if not data or not any(key in data for key in ["make", "model", "year", "color"]):
        abort(400, description="Invalid input: Provide at least one field to update ('make', 'model', 'year', or 'color').")

    cars = load_csv()
    for car in cars:
        if int(car["ID"]) == car_id:
            if "make" in data:
                car["Make"] = data["make"]
            if "model" in data:
                car["Model"] = data["model"]
            if "year" in data:
                car["Year"] = data["year"]
            if "color" in data:
                car["Color"] = data["color"]
            save_csv(cars)
            return jsonify({"message": "Car updated successfully"})
    abort(404, description="Car not found")

# Delete a car by ID
@app.route("/cars/<int:car_id>", methods=["DELETE"])
def delete_car(car_id):
    validate_token()
    cars = load_csv()
    updated_cars = [car for car in cars if int(car["ID"]) != car_id]
    if len(updated_cars) == len(cars):
        abort(404, description="Car not found")
    save_csv(updated_cars)
    return jsonify({"message": "Car deleted successfully"})

# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": str(error)}), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the server
if __name__ == "__main__":
    app.run(debug=True)