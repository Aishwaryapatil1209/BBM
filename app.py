from flask import Flask, request, render_template, render_template_string
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can use them safely
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
# SENDER_EMAIL = "theunexpectedcoder@gmail.com"

# SENDER_PASSWORD = "dnty rwiu yfzp djve"
# RECEIVER_EMAIL = "theunexpectedcoder@gmail.com"

@app.route("/")
def index():
    return render_template("index.html")
from datetime import datetime  # agar upar nahi likha to likhna padega

@app.route("/ping")
def ping():
    return f"App running! Time: {datetime.now()}"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/events")
def events():
    events_list = []  # Empty list to simulate no events
    return render_template("events.html", events=events_list)



@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/gallery')
def gallery():
    images = [
        {'filename': 'gallery1.jpg', 'caption': 'The General Assembly of the Bhartiya Boudh Mahasabha was successfully held under the chairmanship of Bhante Arya Nagarjun Surei Sasai on 25.05.2025 at Ba. Rajabhau Khobragade Hall.'},
        {'filename': 'gallery2.jpg', 'caption': 'Speech delivered by Shri Anand Tukaram Patil, General Secretary of Bhartiya Boudh Mahasabha, during the General Assembly held on 25th May 2025 at Ba. Rajabhau Khobragade Hall.'},
        {'filename': 'gallery3.jpg', 'caption': 'The General Assembly of the Bhartiya Boudh Mahasabha was successfully held under the chairmanship of Bhante Arya Nagarjun Surei Sasai on 25.05.2025 at Ba. Rajabhau Khobragade Hall.'},
        {'filename': 'gallery4.jpg', 'caption': 'Speech delivered by Shri Anand Tukaram Patil, General Secretary of Bhartiya Boudh Mahasabha, during the General Assembly held on 25th May 2025 at Ba. Rajabhau Khobragade Hall.'},
        {'filename': 'gallery5.jpg', 'caption': 'The General Assembly of the Bhartiya Boudh Mahasabha was successfully held under the chairmanship of Bhante Arya Nagarjun Surei Sasai on 25.05.2025 at Ba. Rajabhau Khobragade Hall.'},
        {'filename': 'gallery6.jpg', 'caption': 'Speech delivered by Shri Anand Tukaram Patil, General Secretary of Bhartiya Boudh Mahasabha, during the General Assembly held on 25th May 2025 at Ba. Rajabhau Khobragade Hall.'},
        {'filename': 'gallery7.jpg', 'caption': 'On 23.05.2025, a Buddha Purnima program was organized at 5:00 PM at Tripitaka Smruti, 721, Buddha Nagar. A cultural program was conducted for children, and all members were present and actively participated in the event.'},
        {'filename': 'gallery8.jpg', 'caption': 'On 23.05.2025, a Buddha Purnima program was organized at 5:00 PM at Tripitaka Smruti, 721, Buddha Nagar. A cultural program was conducted for children, and all members were present and actively participated in the event.'},
        {'filename': 'gallery9.jpg', 'caption': 'On 23.05.2025, a Buddha Purnima program was organized at 5:00 PM at Tripitaka Smruti, 721, Buddha Nagar. A cultural program was conducted for children, and all members were present and actively participated in the event.'},
        {'filename': 'gallery10.jpg', 'caption': 'On 23.05.2025, a Buddha Purnima program was organized at 5:00 PM at Tripitaka Smruti, 721, Buddha Nagar. A cultural program was conducted for children, and all members were present and actively participated in the event.'},
        {'filename': 'gallery11.jpg', 'caption': 'On 23.05.2025, a Buddha Purnima program was organized at 5:00 PM at Tripitaka Smruti, 721, Buddha Nagar. A cultural program was conducted for children, and all members were present and actively participated in the event.'},
        {'filename': 'gallery12.jpg', 'caption': 'On 23.05.2025, a Buddha Purnima program was organized at 5:00 PM at Tripitaka Smruti, 721, Buddha Nagar. A cultural program was conducted for children, and all members were present and actively participated in the event.'},
    ]
    return render_template('gallery.html', images=images)



@app.route("/send", methods=["POST"])
def send_email():
    try:
        name = request.form.get("name")
        code = request.form.get("code")
        phone = request.form.get("phone")
        email = request.form.get("email")
        subject = request.form.get("_subject")
        message = request.form.get("message")

        full_message = f"""
        📩 New Contact Request:

        👤 Name: {name}
        ☎️ Phone: {code} {phone}
        📧 Email: {email}
        📝 Subject: {subject}

        ✉️ Message:
        {message}
        """

        msg = EmailMessage()
        msg.set_content(full_message)
        msg["Subject"] = f"New Contact Query: {subject}"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        return render_template_string("<script>alert('Request submitted! We will contact you soon.'); window.location.href='/contact';</script>")

    except Exception as e:
        return f"<h3 style='color:red;'>Something went wrong: {str(e)}</h3>"

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

