import { render, screen, fireEvent } from '@testing-library/react';
import AuthForm from '../components/AuthForm';

test('reders login form', () => {
    render(<AuthForm type="login" onAuth={() => {}} />);
    expect(screen.getByText(/Login/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Username')).toBeInTheDocument();
    expect(screen.getByPlaceholderText('Password')).toBeInTheDocument();
});