"""
Entry point for local testing.

    pip install -r requirements.txt
    python run.py

Then open http://127.0.0.1:5000/register to create a test account.
"""
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
