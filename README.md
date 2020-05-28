# Blank Flask API

Blank Microservices Template for a small API 

Using:
- Flask
- Flask CORS
- Flask SQLAlchemy

## Usage

Create an env / source it / run it

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

## Docker

```bash
docker build . -t YOUR_TAG
docker run -d -p 5000:5000 YOUR_TAG
```

## Contributing
Pull requests are welcome. 
For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)