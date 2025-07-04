import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/detect-abuse';

export const detectAbuse = async (conversation) => {
  try {
    const response = await axios.post(API_URL, {
      conversation: conversation,
    });
    return response.data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};
