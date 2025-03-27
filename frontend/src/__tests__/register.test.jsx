// src/__tests__/register.test.jsx
import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import AuthForm from '../components/AuthForm';

global.fetch = jest.fn(() =>
  Promise.resolve({ json: () => Promise.resolve({ message: 'User registered' }) })
);

test('renders register form and submits', async () => {
  const mockOnAuth = jest.fn();

  render(<AuthForm type="register" onAuth={mockOnAuth} />);

  fireEvent.change(screen.getByPlaceholderText('Username'), { target: { value: 'testuser' } });
  fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'test@example.com' } });
  fireEvent.change(screen.getByPlaceholderText('Password'), { target: { value: 'secret123' } });

  fireEvent.click(screen.getByRole('button', { name: /Register/i }));

  await waitFor(() => {
    expect(mockOnAuth).toHaveBeenCalled();
  });
});
