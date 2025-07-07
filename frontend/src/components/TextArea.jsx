const TextArea = ({ conversation, onChange }) => (
  <textarea
    className="w-full h-40 p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-400 resize-none"
    placeholder="Describe the conflict situation here..."
    value={conversation}
    onChange={onChange}
  />
);
export default TextArea;