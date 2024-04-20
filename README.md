### URL Shortener

This is a simple URL shortener web application built using Flask. It allows users to shorten long URLs into shorter, more manageable ones.

### Usage

1. Clone this repository:

```bash
git clone https://github.com/syed-ali-jibran-rizvi/URL_Shortener_WebApp.git
```

2. Install the required dependencies:

```bash
pip install flask
```

3. Run the Flask application:

```bash
python app.py
```

### How it works

- When the Flask application is running, you can access it via `http://localhost:5000/`.
- Enter a long URL in the input field on the homepage and click the "Shorten" button.
- The application will generate a short URL for the long URL provided.
- You can then use this short URL to access the original long URL.

### API Endpoints

- **Home**: `/` - Renders the homepage with a form to submit long URLs.
- **Shorten URL**: `/shorten` - Accepts a POST request with a JSON payload containing the long URL. It returns a JSON response with the shortened URL.
- **Expand URL**: `/<short_url>` - Accepts a GET request with the short URL. It redirects to the original long URL if the short URL exists, otherwise returns a JSON response indicating that the short URL was not found.

### Project Structure

- **app.py**: Main Flask application file containing the URL shortening logic.
- **templates/index.html**: HTML template for the homepage.

### Dependencies

- Flask

### Author

Syed Ali Jibran Rizvi
