import React, { useState } from 'react';
import { detectConflict, generateEmailDraft } from '../api/ConflictApi';
import TextArea from './TextArea';
import AnalyzeButton from './AnalyzeButton';
import ResultsDisplay from './ResultsDisplay';

const ConflictDetector = () => {
  const [conversation, setConversation] = useState('');
  const [result, setResult] = useState(null);
  const [emailDraft, setEmailDraft] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const analyzeConversation = async () => {
    setLoading(true);
    setError('');
    setEmailDraft('');
    try {
      const res = await detectConflict(conversation);
      setResult(res);
    } catch {
      setError('Failed to analyze conversation.');
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateEmail = async () => {
    try {
      const res = await generateEmailDraft(result);
      setEmailDraft(res.email_draft);
    } catch {
      setError('Failed to generate email.');
    }
  };

  return (
    <div className="max-w-2xl mx-auto mt-10 p-6 bg-white shadow-lg rounded-xl">
      <h1 className="text-2xl font-semibold mb-4">Workplace Conflict Resolver</h1>
      <TextArea conversation={conversation} onChange={(e) => setConversation(e.target.value)} />
      <AnalyzeButton onClick={analyzeConversation} loading={loading} />
      {error && <p className="mt-4 text-red-600">{error}</p>}
      {result && (
        <>
          <ResultsDisplay result={result} />
          <button
            className="mt-4 w-full bg-green-600 text-white py-2 rounded hover:bg-green-700"
            onClick={handleGenerateEmail}
          >
            Generate Email Draft
          </button>
        </>
      )}
      {emailDraft && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <h2 className="text-lg font-semibold mb-2">Generated Email Draft:</h2>
          <pre className="whitespace-pre-wrap text-gray-800">{emailDraft}</pre>
        </div>
      )}
    </div>
  );
};

export default ConflictDetector;
