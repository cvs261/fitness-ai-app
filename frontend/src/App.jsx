import { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    Age: '',
    Gender: 'Male',
    Goal: 'Muscle Gain',
    Body_Type: 'Ectomorph',
    "Weight (kg)": '',
    "Height (m)": '',
    BMI: '',
    Fat_Percentage: '',
    "Experience_Level": '',
    "Workout_Frequency (days/week)": '',
    "Session_Duration (hours)": '',
    Calories_Burned: '',
    Max_BPM: '',
    Avg_BPM: '',
    Resting_BPM: '',
    "Water_Intake (liters)": ''
  });

  const [result, setResult] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/api/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      const data = await response.json();
      if (data.recommended_workout) {
        setResult(data.recommended_workout);
      } else {
        setResult('Eroare: ' + JSON.stringify(data));
      }
    } catch (err) {
      setResult('Eroare la comunicare cu backend-ul');
    }
  };

  return (
    <div className="container">
      <h1>Recomandare AI pentru Antrenament</h1>
      <form onSubmit={handleSubmit}>
        {Object.entries(formData).map(([key, value]) => (
          <div key={key}>
            <label>{key}</label>
            {key === 'Gender' ? (
              <select name={key} value={value} onChange={handleChange}>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
              </select>
            ) : key === 'Goal' ? (
              <select name={key} value={value} onChange={handleChange}>
                <option value="Muscle Gain">Muscle Gain</option>
                <option value="Fat Loss">Fat Loss</option>
                <option value="Endurance">Endurance</option>
              </select>
            ) : key === 'Body_Type' ? (
              <select name={key} value={value} onChange={handleChange}>
                <option value="Ectomorph">Ectomorph</option>
                <option value="Mesomorph">Mesomorph</option>
                <option value="Endomorph">Endomorph</option>
              </select>
            ) : (
              <input type="text" name={key} value={value} onChange={handleChange} />
            )}
          </div>
        ))}
        <button type="submit">Generează plan</button>
      </form>
      {result && <div className="result">Plan recomandat: <strong>{result}</strong></div>}
    </div>
  );
}

export default App;
