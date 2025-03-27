import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import AuthForm from '../components/AuthForm';

// Asigură-te că fiecare test are fetch curat
beforeEach(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ message: 'User registered successfully' }),
    })
  );
});

afterEach(() => {
  jest.restoreAllMocks();
});

test('fetch is called on register form submission', async () => {
  const mockOnAuth = jest.fn();

  render(<AuthForm type="register" onAuth={mockOnAuth} />);

  fireEvent.change(screen.getByPlaceholderText('Username'), {
    target: { value: 'testuser' },
  });
  fireEvent.change(screen.getByPlaceholderText('Email'), {
    target: { value: 'test@example.com' },
  });
  fireEvent.change(screen.getByPlaceholderText('Password'), {
    target: { value: 'secret123' },
  });

  fireEvent.click(screen.getByRole('button', { name: /Register/i }));

  await waitFor(() => {
    expect(fetch).toHaveBeenCalledWith(
      'http://localhost:5001/api/register',
      expect.objectContaining({
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: 'test@example.com',
          password: 'secret123',
        }),
      })
    );

    expect(mockOnAuth).toHaveBeenCalledWith({ message: 'User registered successfully' });
  });
});
