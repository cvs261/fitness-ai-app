import { render, screen } from '@testing-library/react';
import RecommendationForm from '../components/RecommandationForm';

test('renders recommendation form', () => {
  render(<RecommendationForm />);
  expect(screen.getByText(/Recomandare AI pentru Antrenament/i)).toBeInTheDocument();
  expect(screen.getByText(/Generează plan/i)).toBeInTheDocument();
});
