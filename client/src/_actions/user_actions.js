import axios from 'axios';
import { LOGIN_USER, REGISTER_USER } from './types';
import { SERVER } from 'Config.js';

export function loginUser(dataToSubmit) {
  const request = axios
    .post(`http://localhost:8000/accounts/login/`, dataToSubmit)
    .then(res => res.data)
    .catch(err => console.log(err));
  return {
    type: LOGIN_USER,
  };
}
export function registerUser(dataToSubmit) {
  const request = axios
    .post(`${SERVER}accounts/signup/`, dataToSubmit)
    .then(response => response.data);

  return {
    type: REGISTER_USER,
    payload: request,
  };
}
