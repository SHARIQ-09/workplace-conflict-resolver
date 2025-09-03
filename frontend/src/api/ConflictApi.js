import axios from 'axios';

const API_URL = 'https://workplace-abuse.onrender.com/api'

//https://workplace-abuse.onrender.com/api';
// Backend URL (change if deployed)
//const API_URL = 'http://localhost:8000/api';

console.log("API URL Being Used:", `${API_URL}/detect-conflict`);

export const detectConflict = async (conversation) => {
  try {
    const response = await axios.post(`${API_URL}/detect-conflict`, {
      conversation: conversation,
    });
    return response.data;
  } catch (error) {
    console.error('API Error (Conflict Detection):', error);
    throw error;
  }
};

// ✅ New API for Email Draft Generator
export const generateEmailDraft = async (conflictResolutionResponse) => {
  try {
    const response = await axios.post(`${API_URL}/generate-email`, conflictResolutionResponse);
    return response.data;
  } catch (error) {
    console.error('API Error (Email Draft Generation):', error);
    throw error;
  }
};
