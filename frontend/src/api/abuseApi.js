import axios from 'axios';

const API_URL = 'https://workplace-abuse.onrender.com';

export const detectAbuse = async (conversation) => {
  try {
    const response = await axios.post(`${API_URL}/detect-abuse`, {
      conversation: conversation,
    });
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};
