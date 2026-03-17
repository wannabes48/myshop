### 🛒 MyShop - Simple Django E-commerce<br>

This is a lightweight Django e-commerce project featuring user authentication, a product catalog, a shopping cart, and a simulated M-Pesa checkout. <br>

#### 📋 Prerequisites<br>
Make sure you have the following installed on your machine:<br>
* Python 3.8+<br>
* Git<br>

#### 🚀 Local Setup Instructions<br>

**1. Clone the repository**<br>
Open your terminal and run:<br>
```bash
git clone <paste-your-repository-url-here>
cd <your-repository-folder-name>
```

**2. Activate the virtual environment**<br>
* **Windows:**<br>
  ```bash
  myenv\Scripts\activate
  ```
* **macOS/Linux:**<br>
  ```bash
  source myenv/bin/activate
  ```

**3. Install dependencies**<br>
With your virtual environment active, install Django and any other required packages:
Simply run `pip install django`)<br>

**4. Set up the database**<br>
Run Django's built-in migrations to create the database tables (this project uses SQLite by default):<br>
```bash
python manage.py migrate
```

**5. Run the development server**<br>
Start the local server:<br>
```bash
python manage.py runserver
```

**6. View the project**<br>
Open your web browser and navigate to:<br>
* **Storefront:** `http://127.0.0.1:8000/`<br>
* **Admin Panel:** `http://127.0.0.1:8000/admin/`<br>

***
