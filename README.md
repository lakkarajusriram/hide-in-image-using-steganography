Hide-in-Image - Image Steganography Tool 🔐
📌 Project Overview
Hide-in-Image is a Flask-based web application that allows users to hide secret messages inside images and later extract them using a secret key. It utilizes Least Significant Bit (LSB) Steganography, where the hidden message is embedded in the pixel values of the image, making it invisible to the naked eye.
This tool ensures secure communication by enabling users to encode confidential messages inside an image and decode them later only if they have the correct secret key.
________________________________________
🚀 Features
✅ Secure Message Hiding – Embed secret messages inside images without visible changes.
✅ Password Protection – Only the correct secret key can reveal the message.
✅ User-Friendly Web Interface – Simple and interactive UI.
✅ Supports Multiple Image Formats – Works with JPG, PNG, etc.
✅ Stealth Communication – The modified image appears identical to the original.
________________________________________
🔧 Technologies Used
✔ Python (Flask Framework) – Backend server
✔ OpenCV – Image processing
✔ NumPy – Handling pixel data
✔ HTML, CSS, JavaScript – Frontend UI
✔ AJAX & Fetch API – Async communication
________________________________________
📌 How It Works?
1️⃣ Encoding (Hiding a Message in an Image)
1.	The user uploads an image (JPG/PNG).
2.	Enters a secret message to hide.
3.	Provides a secret key for added security.
4.	The program converts the message into binary.
5.	The binary data is embedded into the least significant bits (LSB) of image pixels.
6.	The user downloads the encoded image, which looks normal but contains the hidden message.

2️⃣ Decoding (Extracting the Hidden Message from an Image)
1.	The user uploads the encoded image.
2.	Enters the correct secret key.
3.	The program extracts hidden bits from the image.
4.	The binary data is converted back into text.
5.	If the secret key matches, the message is revealed.
6.	If the wrong key is entered, an error is shown ("Invalid Secret Key!").

Usage Guide
🔹 Encoding a Message
1️⃣ Upload an image.
2️⃣ Enter a secret message & key.
3️⃣ Click "Encode & Download".
4️⃣ Save the encoded image.
🔹 Decoding a Message
1️⃣ Upload the encoded image.
2️⃣ Enter the secret key.
3️⃣ Click "Decode".
4️⃣ The hidden message is displayed (if the key is correct).
________________________________________
🛡️ Security Measures
🔒 Secret Key Protection – Only the correct key can decode the message.
🖼️ Stealth Storage – The image remains visually unchanged.
❌ Wrong Key Handling – Prevents unauthorized access.
________________________________________
