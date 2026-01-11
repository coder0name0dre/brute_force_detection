from flask import Flask, request, render_template_string
import time

app = Flask(__name__)

# Hardcoded test credentials
valid_username = "admin"
valid_password = "password123"

log_file = "login_attempts.log"

# Simple HTML login form
login_page = """
<form method="POST">
    <input name="username" placeholder="Username">
    <input name="password" placeholder="Password" type="password">
    <button type="submit">Login</button>
</form>
<p>{{ message }}</p>
"""

@app.route("/", methods=["GET", "POST"])

def login():
    message = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Get client IP (localhost for testing)
        ip_address = request.remote_addr
        timestamp = time.strftime("%d-%m-%Y %H:%M:%S")

        # Log every login attempt
        with open(log_file, "a") as log:
            log.write(f"{timestamp} | {ip_address} | {username} | ")

            if username == valid_username and password == valid_password:
                log.write("Success!\n")
                message = "Login successful!"
            else:
                log.write("Failure!\n")
                message = "Login failed!"

    return render_template_string(login_page, message=message)

if __name__ == "__main__":
    app.run(debug=True)