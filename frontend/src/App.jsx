// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import AuthForm from './components/AuthForm';
import RecommendationForm from './components/RecommandationForm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<AuthForm mode="login" />} />
        <Route path="/register" element={<AuthForm mode="register" />} />
        <Route path="/recommendation" element={<RecommendationForm />} />
      </Routes>
    </Router>
  );
}

export default App;
