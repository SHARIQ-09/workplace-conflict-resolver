const ResultsDisplay = ({ result }) => (
  <div className="mt-6 bg-gray-50 p-4 rounded-md border border-gray-300">
    <h2 className="text-xl font-semibold mb-2 text-gray-700">Conflict Analysis Result:</h2>
    <div className="space-y-2">
      <div>
        <span className="font-medium text-gray-600">Conflict Risk:</span>{' '}
        <span className="text-blue-700">{result.conflict_risk}</span>
      </div>
      <div>
        <span className="font-medium text-gray-600">Issues Detected:</span>{' '}
        {result.issues_detected && result.issues_detected.length > 0 ? (
          <ul className="list-disc ml-6 text-gray-700">
            {result.issues_detected.map((issue, index) => (
              <li key={index}>{issue}</li>
            ))}
          </ul>
        ) : (
          'None'
        )}
      </div>
      <div>
        <span className="font-medium text-gray-600">Resolution Choices:</span>
        <ul className="list-disc ml-6 text-gray-700">
          {Object.entries(result.resolution_choices).map(([key, value]) => (
            <li key={key}>
              <strong>{key.toUpperCase()}:</strong> {value}
            </li>
          ))}
        </ul>
      </div>
    </div>
  </div>
);

export default ResultsDisplay;
