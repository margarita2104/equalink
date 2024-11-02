import { useState } from "react";
import { AxiosWritingAssistant } from "../../axios/Axios";

const WritingAssistant = () => {
  const [inputText, setInputText] = useState("");
  const [responseData, setResponseData] = useState(null);
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
      console.log("API Response:", response.data);
      setResponseData(response.data);
    } catch (err) {
      setError("An error occurred while processing your request.");
      console.error(err);
    }
  };

  const getSuggestions = () => {
    if (responseData && responseData.combined_feedback) {
      try {
        console.log("Raw combined_feedback:", responseData.combined_feedback);

        const feedback = JSON.parse(responseData.combined_feedback);
        console.log("Parsed Feedback:", feedback);

        return feedback.suggestions || [];
      } catch (error) {
        console.error("Error parsing combined_feedback:", error);
        setError(
          "Error processing suggestions. Please check the input or try again."
        );
        return [];
      }
    }
    return [];
  };

  const suggestions = getSuggestions();

  return (
    <div className="w-2/3 pt-5 px-10">
      <p className="mb-5">
        Writing Assistant analyses your text for potential biases and offers
        thoughtful suggestions for inclusive language. From subtle tone shifts
        to specific word choices, this tool helps refine your writing for
        clarity, fairness, and impact. Write confidently, knowing every sentence
        supports balanced storytelling.
      </p>
      <h2 className="text-2xl font-bold mb-5">Input your text here:</h2>
      <p className="mb-5 text-sm">
        Please, paste your text as a single paragraph.
      </p>

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
      {suggestions.length > 0 ? (
        <div className="mt-5">
          <h2 className="text-xl font-bold mb-5">Suggestions:</h2>
          {suggestions.map((suggestion, index) => (
            <div key={index} className="mb-4 p-3 border rounded-md shadow">
              <p>
                <strong>Original sentence:</strong>{" "}
                {suggestion.original_sentence}
              </p>
              <p>
                <strong>Suggested correction:</strong>{" "}
                {suggestion.suggested_correction}
              </p>
              <p>
                <strong>Explanation:</strong> {suggestion.explanation}
              </p>
            </div>
          ))}
        </div>
      ) : (
        <p>No suggestions available.</p>
      )}
    </div>
  );
};

export default WritingAssistant;
