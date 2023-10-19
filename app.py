from flask import Flask, render_template

app = Flask(__name__)

Clients = [{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone_number": "123-456-7890",
    "client_id": 1,
    "registration_date": "2023-10-12",
    "status": "Active",
    "token": "token1"
}, {
    "first_name": "Alice",
    "last_name": "Smith",
    "email": "alice.smith@example.com",
    "phone_number": "987-654-3210",
    "client_id": 2,
    "registration_date": "2023-09-28",
    "status": "Inactive",
    "token": "token2"
}, {
    "first_name": "Bob",
    "last_name": "Johnson",
    "email": "bob.johnson@example.com",
    "phone_number": "555-123-4567",
    "client_id": 3,
    "registration_date": "2023-11-05",
    "status": "Active",
    "token": "token3"
}, {
    "first_name": "Sarah",
    "last_name": "Davis",
    "email": "sarah.davis@example.com",
    "phone_number": "111-222-3333",
    "client_id": 4,
    "registration_date": "2023-10-18",
    "status": "Active",
    "token": "token4"
}]


@app.route('/')
def hello_world():
  return render_template('home.html',clients=Clients)


if __name__ == "__main__":
  app.run('0.0.0.0', debug=True)
