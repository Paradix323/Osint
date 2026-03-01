# Clone the repository
git clone https://github.com/your-org/modular-osint-investigator.git
cd modular-osint-investigator

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Launch the application
python frontend_logic.py
