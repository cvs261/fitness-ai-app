import { useState } from 'react'
import './AuthForm.css';

export default function AuthForm ({ type = 'login', onAuth }) {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value});
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        const endpoint = type === 'register' ? '/api/register' : '/api/login';
        const payload = {
            email: formData.email,
            password: formData.password
        };
        if (type === 'register') payload.email = formData.email;

        try{
            const response = await fetch(`http://localhost:5001${endpoint}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            const data = await response.json();
            onAuth(data);
        } catch(err) {
            console.error('Authentication failed', err);
        }
    };

    return(
        <form onSubmit={handleSubmit} className='auth-form'>
            <h2>{type === 'register' ? 'Register' : 'Login'}</h2>
            <input 
                name="username"
                placeholder='Username'
                value={formData.username}
                onChange={handleChange}
                required
            />
            {type === 'register' && (
                <input
                    name='email'
                    type='email'
                    placeholder='Email'
                    value={formData.email}
                    onChange={handleChange}
                    required
                />
            )}
            <input
                name='password'
                type='password'
                placeholder='Password'
                value={formData.password}
                onChange={handleChange}
                required
            />
            <button type='submit'>{type === 'register' ? 'Register' : 'Login'}</button>
        </form>
    );
}