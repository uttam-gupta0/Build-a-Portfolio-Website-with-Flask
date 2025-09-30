from flask import Flask, render_template, request

app = Flask(__name__)

# Resume data 
resume_data = {
    "name": "Uttam Kumar Gupta",
    "contact": {
        "phone": "7483767904",
        "email": "Vguptauttam499@gmail.com",
        "linkedin": "https://www.linkedin.com/in/uttam-gupta-79889834a/"
    },
    "career_objective": "A final-year ECE student passionate about software engineering, eager to develop as a developer and create original solutions.",
    "education": [
        {"degree": "B.E in Electronics & Communication Engineering", "institute": "Sambhram Institute of Technology, VTU", "year": "2022", "cgpa": "8.22/10 (till 6th Sem)"},
        {"degree": "12th (PUC)", "institute": "Xavier International College, Kathmandu, Nepal", "year": "2022", "gpa": "3.09/4"},
        {"degree": "10th (SSLC)", "institute": "Shanti Shikchha Mandir MA VI, Nepal", "year": "2020", "gpa": "3.7/4"}
    ],
    "skills": ["C++", "C", "Python", "Verilog", "HTML", "CSS", "MATLAB", "VS Code", "Arduino", "Raspberry Pi", "ThingSpeak", "Blynk"],
    "projects": [
        {"title": "IoT Based Real-Time Health Monitoring System", 
         "desc": "Used IoT sensors to monitor health data (temperature, heart rate) and alert users on abnormalities."}
    ],
    "certifications": [
        "AI Fundamentals – DataCamp (Feb 2025)",
        "Presented paper: HeatEye AQ at ESHAM-2025",
        "Robotics and Its Applications Workshop (2024)",
        "BEL–IETE Symposium on AI, Cyber Security, IoT, Aerial Vehicles (2024)",
        "Skill Development: IoT Ecosystem with ESP32 (2024)",
        "VLSI Design to Tapeout Workshop (2024)"
    ],
    "languages": ["Nepali", "Hindi", "English", "Kannada"]
}

@app.route("/")
def home():
    return render_template("index.html", data=resume_data)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now, just print the message (later you can add email/DB)
        print(f"Message from {name} ({email}): {message}")

        return render_template("contact.html", success=True)

    return render_template("contact.html", success=False)

if __name__ == "__main__":
    app.run(debug=True)

