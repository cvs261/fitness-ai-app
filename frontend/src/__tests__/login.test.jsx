// frontend/src/__tests__/login.test.jsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom'
import AuthForm from '../components/AuthForm';

beforeEach(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({ json: () => Promise.resolve({ message: 'Logged in' }) })
  );
});

test('renders login form and submits successfully', async () => {
  render(<AuthForm type="login" onAuth={() => {}} />);

  fireEvent.change(screen.getByPlaceholderText('Username'), {
    target: { value: 'user@example.com' },
  });
  fireEvent.change(screen.getByPlaceholderText('Password'), {
    target: { value: 'secret123' },
  });

  fireEvent.click(screen.getByRole('button', { name: /Login/i }));

  expect(await screen.findByRole('heading', { name: /Login/i })).toBeInTheDocument();
  expect(fetch).toHaveBeenCalled();
});