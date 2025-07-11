import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://localhost:5000',
});

export const register = data => api.post('/auth/register', data);
export const login = data => api.post('/auth/login', data);
export const sendMessage = (token, content) =>
  api.post('/chat/send', { content }, {
    headers: { Authorization: `Bearer ${token}` }
  });
export const getHistory = token =>
  api.get('/chat/history', {
    headers: { Authorization: `Bearer ${token}` }
  });
