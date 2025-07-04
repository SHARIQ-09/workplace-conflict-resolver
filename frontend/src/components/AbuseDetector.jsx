import React, { useState } from 'react';
import axios from 'axios';
import TextArea from './TextArea';
import AnalyzeButton from './AnalyzeButton';
import ResultsDisplay from './ResultsDisplay';

const AbuseDetector = () => {
  const [conversation, setConversation] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const analyzeConversation = async () => {
    setLoading(true);
    setError('');
    try {
      const response = await axios.post('http://127.0.0.1:8000/detect-abuse', { conversation });
      setResult(response.data);
    } catch (err) {
      setError('Failed to analyze conversation.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto mt-10 p-6 bg-white shadow-lg rounded-xl border border-gray-200">
      <h1 className="text-2xl font-semibold text-gray-800 mb-4">Workplace Abuse Detector</h1>
      <TextArea conversation={conversation} onChange={(e) => setConversation(e.target.value)} />
      <AnalyzeButton onClick={analyzeConversation} loading={loading} />
      {error && <p className="mt-4 text-red-600 font-medium">{error}</p>}
      {result && <ResultsDisplay result={result} />}
    </div>
  );
};

export default AbuseDetector;
