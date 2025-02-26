# hide-in-image-using-steganography
Hide-in-Image - Image Steganography Tool 🔐
📌** Project Overview**
Hide-in-Image is a Flask-based web application that allows users to hide secret messages inside images and later extract them using a secret key. It utilizes Least Significant Bit (LSB) Steganography, where the hidden message is embedded in the pixel values of the image, making it invisible to the naked eye.

This tool ensures secure communication by enabling users to encode confidential messages inside an image and decode them later only if they have the correct secret key.

**🚀 Features**
✅ Secure Message Hiding – Embed secret messages inside images without visible changes.
✅ Password Protection – Only the correct secret key can reveal the message.
✅ User-Friendly Web Interface – Simple and interactive UI.
✅ Supports Multiple Image Formats – Works with JPG, PNG, etc.
✅ Stealth Communication – The modified image appears identical to the original.

**🔧 Technologies Used**
✔ Python (Flask Framework) – Backend server
✔ OpenCV – Image processing
✔ NumPy – Handling pixel data
✔ HTML, CSS, JavaScript – Frontend UI
✔ AJAX & Fetch API – Async communication

**📌 How It Works?**
1️⃣ Encoding (Hiding a Message in an Image)
The user uploads an image (JPG/PNG).
Enters a secret message to hide.
Provides a secret key for added security.
The program converts the message into binary.
The binary data is embedded into the least significant bits (LSB) of image pixels.
The user downloads the encoded image, which looks normal but contains the hidden message.
2️⃣ Decoding (Extracting the Hidden Message from an Image)
The user uploads the encoded image.
Enters the correct secret key.
The program extracts hidden bits from the image.
The binary data is converted back into text.
If the secret key matches, the message is revealed.
If the wrong key is entered, an error is shown ("Invalid Secret Key!").
