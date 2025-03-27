# 🧠 Fitness AI App 💪

An intelligent fitness plan recommendation web app powered by AI and real-time personalized user input. This full-stack application suggests workout plans based on user's physiological data, fitness level, and goals.

## 📌 What does this app do?

- Accepts user input such as age, gender, weight, height, heart rate data, BMI, experience level, and fitness goals.
- Uses a machine learning model trained on gym member exercise data to recommend a personalized workout type.
- Stores recommendation history in a MariaDB database for analysis and tracking.
- Provides authentication system for login and registration.
- Tracks and displays recommendation history per user (in progress).

---

## ⚙️ Technologies Used

### 💻 Frontend
- **React**
- **CSS (custom styling + AuthForm design refresh)**
- **React Router DOM**
- **Jest + Testing Library** for unit tests

### 🔙 Backend
- **Flask**
- **Flask-CORS**
- **Flask-SQLAlchemy**
- **Flask-Migrate** (Alembic)
- **Gunicorn**
- **Joblib** (for loading trained ML models)
- **Scikit-learn**, **NumPy**
- **MariaDB** + **PyMySQL**

### 🐳 Dockerized Environment
- Docker
- Docker Compose

---

## ✅ Features Implemented

- [x] ML model for workout prediction
- [x] Backend API for handling predictions
- [x] Frontend form for user data input
- [x] Docker setup for frontend and backend
- [x] Database logging of user inputs & results
- [x] Authentication system (register & login)
- [x] Form switching based on route (`/login`, `/register`)
- [x] Unit tests for AuthForm, RecommendationForm, and fetch calls
- [x] Custom CSS styles for both forms

---

## 🔧 To Be Implemented

### Backend:
- [ ] Endpoints to fetch user prediction history
- [ ] Admin dashboard for viewing statistics
- [ ] More unit tests and validation logic

### Frontend:
- [ ] Show recommendation history per user
- [ ] Real-time validation for form inputs
- [ ] Theme switcher (dark/light mode)
- [ ] Design improvements with Tailwind or Material UI (in progress)

---

## 🔮 Planned Integrations

- CI/CD with GitHub Actions
- Nginx for production reverse proxy
- Kubernetes deployment
- AI improvements (regression/classification toggle)
- Real-time metrics tracking via charts

---

## 🛠️ Local Development & Setup

> You need: `Git`, `Docker`, and `Docker Compose` installed on your machine.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fitness-ai-app.git
cd fitness-ai-app
```

### 2. Build and start the containers

```bash
docker-compose build --no-cache
docker-compose up
```

- Frontend will be available at: [http://localhost:3000](http://localhost:3000)  
- Backend API will be available at: [http://localhost:5001/api/recommend](http://localhost:5001/api/recommend)

> Auth system routes:
> - [http://localhost:3000/login](http://localhost:3000/login)  
> - [http://localhost:3000/register](http://localhost:3000/register)

---

### 3. (Optional) Run without Docker

#### 🧠 Backend

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the Flask app
flask run --host=0.0.0.0 --port=5000
```

#### 🎨 Frontend

```bash
cd frontend
npm install
npm start
```

---

## 📁 Folder Structure

```text
fitness-ai-app/
│
├── backend/
│   ├── app.py
│   ├── api/
│   ├── auth.py
│   ├── models.py
│   ├── ai/ (contains .joblib ML models)
│   ├── migrations/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── AuthForm.jsx
│   │   │   ├── RecommendationForm.jsx
│   │   │   └── AuthForm.css
│   │   ├── __tests__/
│   │   │   ├── login.test.jsx
│   │   │   ├── register.test.jsx
│   │   │   ├── fetch.test.jsx
│   │   │   └── RecommendationForm.test.jsx
│   └── package.json
│
├── docker-compose.yml
├── README.md
```

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch  
   `git checkout -b feature/your-feature-name`
3. Commit your changes  
   `git commit -m "Add new feature"`
4. Push to GitHub  
   `git push origin feature/your-feature-name`
5. Open a Pull Request 🚀

---

## 🔬 Dataset

This project uses the [Gym Members Exercise Dataset](https://www.kaggle.com/datasets/ajaypalsinghlo/gym-members-exercise-data) from Kaggle for training the machine learning model.

---

## 📬 Contact

For questions, suggestions, or collaborations, feel free to open an issue or start a discussion in the GitHub repo.

---
