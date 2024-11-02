import { useState } from "react";
import { AxiosWritingAssistant } from "../../axios/Axios";

const WritingAssistant = () => {
  const [inputText, setInputText] = useState("");
  const [responseText, setResponseText] = useState("");
  const [error, setError] = useState("");
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    try {
      const response = await AxiosWritingAssistant.post(
        "assistant/bias-analysis/",
        {
          article_text: inputText,
        }
      );
      setResponseText(response.data);
    } catch (err) {
      setError("An error occurred while processing your request.");
      console.error(err);
    }
  };
  return (
    <div className="w-2/3 pt-5 px-10">
      <p className="mb-5">
        Writing Assistant analyses your text for potential biases and offers
        thoughtful suggestions for inclusive language. From subtle tone shifts
        to&nbsp;specific word choices, this tool helps refine your writing for
        clarity, fairness, and impact. Write confidently, knowing every sentence
        supports balanced storytelling.
      </p>
      <h2 className="text-2xl font-bold mb-5">Input your text here:</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          rows="6"
          className="w-full mb-5 border rounded-md p-2"
          placeholder="Enter your text here..."
        />
        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Analyze
        </button>
      </form>
      {error && <p className="text-red-500">{error}</p>}
      {responseText && (
        <div className="mt-5">
          <h2 className="text-xl font-bold">Suggestions:</h2>
          {responseText.combined_feedback ? (
            <p>{responseText.combined_feedback}</p> 
          ) : (
            <p>No suggestions available.</p>
          )}
        </div>
      )}
    </div>
  );
};
export default WritingAssistant;
