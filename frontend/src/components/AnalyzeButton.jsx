const AnalyzeButton = ({ onClick, loading }) => (
  <button
    className="mt-4 w-full bg-blue-600 text-white font-medium py-2 rounded-md hover:bg-blue-700 transition"
    onClick={onClick}
    disabled={loading}
  >
    {loading ? 'Prospective solutions on the way..' : 'Solve my Conflict'}
  </button>
);
export default AnalyzeButton;
