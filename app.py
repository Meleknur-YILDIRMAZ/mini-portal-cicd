from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# En kolay hali: RAM’de tutuyoruz (deploy olunca sıfırlanır)
appointments = [
    {"id": 1, "name": "Sude", "doctor": "Dahiliye", "date": "2026-02-28", "time": "14:30"},
]

def next_id():
    return max([a["id"] for a in appointments], default=0) + 1

@app.get("/")
def home():
    return render_template("index.html", appointments=appointments)

@app.post("/add")
def add():
    name = request.form.get("name", "").strip()
    doctor = request.form.get("doctor", "").strip()
    date = request.form.get("date", "").strip()
    time = request.form.get("time", "").strip()

    # Basit doğrulama
    if name and doctor and date and time:
        appointments.append({
            "id": next_id(),
            "name": name,
            "doctor": doctor,
            "date": date,
            "time": time
        })

    return redirect(url_for("home"))

@app.post("/delete/<int:aid>")
def delete(aid):
    global appointments
    appointments = [a for a in appointments if a["id"] != aid]
    return redirect(url_for("home"))

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)