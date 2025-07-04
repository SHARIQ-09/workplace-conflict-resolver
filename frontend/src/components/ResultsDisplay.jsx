const ResultsDisplay = ({ result }) => (
  <div className="mt-6 bg-gray-50 p-4 rounded-md border border-gray-300">
    <h2 className="text-xl font-semibold mb-2 text-gray-700">Analysis Result:</h2>
    <div className="space-y-2">
      <div>
        <span className="font-medium text-gray-600">Abuse Detected:</span>{' '}
        <span className={result.abuse_detected ? 'text-red-600' : 'text-green-600'}>
          {result.abuse_detected ? 'Yes' : 'No'}
        </span>
      </div>
      <div>
        <span className="font-medium text-gray-600">Abuse Types:</span>{' '}
        {result.types.length > 0 ? result.types.join(', ') : 'None'}
      </div>
      <div>
        <span className="font-medium text-gray-600">Severity Score:</span>{' '}
        {result.severity_score}
      </div>
      <div>
        <span className="font-medium text-gray-600">Explanation:</span>
        <p className="mt-1 text-gray-700">{result.explanation}</p>
      </div>
    </div>
  </div>
);
export default ResultsDisplay;
