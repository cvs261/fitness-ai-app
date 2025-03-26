import { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('...loading');

  useEffect(() => {
    fetch('http://localhost:5001/api/hello')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => setMessage("Backend offline"));
  }, []);

  return (
    <div>
      <h1>Fitness AI App</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
