document.addEventListener("DOMContentLoaded", () => {

    const detectBtn =
        document.getElementById("detectBtn");

    const imageInput =
        document.getElementById("imageInput");

    imageInput.addEventListener(
        "change",
        previewImage
    );

    detectBtn.addEventListener(
        "click",
        uploadImage
    );
});


function previewImage() {

    const file =
        document.getElementById("imageInput")
        .files[0];

    const preview =
        document.getElementById("preview");

    if(file){

        preview.src =
            URL.createObjectURL(file);

        preview.style.display =
            "block";
    }
}


async function uploadImage() {

    const fileInput =
        document.getElementById("imageInput");

    if(!fileInput.files.length){

        alert("Select an image first.");

        return;
    }

    const formData =
        new FormData();

    formData.append(
        "image",
        fileInput.files[0]
    );

    try{

        document.getElementById("result")
            .innerText =
            "Processing Vehicle...";

        const response =
            await fetch(
                "http://127.0.0.1:5000/detect",
                {
                    method:"POST",
                    body:formData
                }
            );

        const data =
            await response.json();

        let result =

`🚗 Vehicle Number : ${data.plate_number}

👤 Owner : ${data.owner_name}

📌 Status : ${data.status}

⚠ Violation : ${data.violation}

💰 Fine Amount : ₹${data.fine_amount}`;

        if(data.alert){

            result +=

`\n\n🚨 STOLEN VEHICLE DETECTED 🚨`;
        }

        if(data.challan_generated){

            result +=

`\n\n📄 Challan Generated Successfully`;
        }

        document.getElementById("result")
            .innerText = result;

    }

    catch(error){

        console.error(error);

        document.getElementById("result")
            .innerText =
            "Error while processing image.";
    }
}