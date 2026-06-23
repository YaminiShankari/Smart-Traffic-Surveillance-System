from flask import Flask, request, jsonify
from flask_cors import CORS

from detection import detect_plate
from database import check_vehicle
from challan_generator import generate_challan

import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = r"D:\Yams\College\Sem_7\CV\uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/detect", methods=["POST"])
def detect():

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded"
        })

    image = request.files["image"]

    path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(path)

    plate_number = detect_plate(path)

    if plate_number:
        plate_number = plate_number.replace(
            " ",
            ""
        )

    print("Detected Plate:", plate_number)

    vehicle = check_vehicle(
        plate_number
    )

    alert = False

    owner_name = "Unknown"

    status = "Not Found"

    violation = "None"

    fine_amount = 0

    challan_generated = False

    challan_path = ""

    if vehicle:

        vehicle = vehicle[0]

        owner_name = vehicle.get(
            "owner_name",
            "Unknown"
        )

        status = vehicle.get(
            "status",
            "Unknown"
        )

        violation = vehicle.get(
            "violation",
            "None"
        )

        fine_amount = vehicle.get(
            "fine_amount",
            0
        )

        if status.lower() == "stolen":
            alert = True

        if violation and violation != "None":

            challan_path = generate_challan(
                plate_number,
                owner_name,
                violation,
                fine_amount
            )

            challan_generated = True

    return jsonify({

        "plate_number": plate_number,

        "owner_name": owner_name,

        "status": status,

        "violation": violation,

        "fine_amount": fine_amount,

        "alert": alert,

        "challan_generated": challan_generated,

        "challan_path": challan_path

    })


if __name__ == "__main__":
    app.run(debug=True)