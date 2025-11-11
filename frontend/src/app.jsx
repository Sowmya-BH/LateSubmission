// src/App.jsx
import React, { useState } from 'react';
import UploadSection from './components/UploadSection';
import QueryInput from './components/QueryInput';
import AnalysisResult from './components/AnalysisResult';
import Loader from './components/Loader';
import { analyzeDocument } from './api/analyzerApi';

export default function App() {
  const [file, setFile] = useState(null);
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!file || !query) {
      alert('Please upload a PDF and enter a query');
      return;
    }
    setLoading(true);
    setError(null);
    try {
      const res = await analyzeDocument(file, query);
      setResult(res.result);
    } catch (err) {
      setError('Analysis failed. Check backend logs.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-3xl font-bold text-center mb-8 text-blue-700">
        Financial Document Analyzer
      </h1>
      <div className="max-w-2xl mx-auto bg-white rounded-2xl shadow-lg p-6 space-y-6">
        <UploadSection setFile={setFile} />
        <QueryInput query={query} setQuery={setQuery} />
        <button
          onClick={handleAnalyze}
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2 rounded-xl transition"
        >
          Analyze Document
        </button>
        {loading && <Loader />}
        {error && <p className="text-red-500 text-center">{error}</p>}
        {result && <AnalysisResult result={result} />}
      </div>
    </div>
  );
}

// src/components/UploadSection.jsx
import React from 'react';
export default function UploadSection({ setFile }) {
  return (
    <div className="border-2 border-dashed border-gray-300 rounded-xl p-6 text-center">
      <input
        type="file"
        accept="application/pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="hidden"
        id="pdf-upload"
      />
      <label
        htmlFor="pdf-upload"
        className="cursor-pointer text-blue-600 font-semibold"
      >
        Click to upload a PDF document
      </label>
    </div>
  );
}

// src/components/QueryInput.jsx
import React from 'react';
export default function QueryInput({ query, setQuery }) {
  return (
    <textarea
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      placeholder="Enter your financial analysis query..."
      className="w-full border border-gray-300 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
      rows={3}
    />
  );
}

// src/components/AnalysisResult.jsx
import React from 'react';
export default function AnalysisResult({ result }) {
  return (
    <div className="bg-gray-100 rounded-xl p-4">
      <h2 className="text-xl font-semibold mb-2 text-gray-700">Analysis Result:</h2>
      <pre className="whitespace-pre-wrap text-gray-800 text-sm">{result}</pre>
    </div>
  );
}

// src/components/Loader.jsx
import React from 'react';
export default function Loader() {
  return (
    <div className="flex justify-center">
      <div className="animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-blue-600"></div>
    </div>
  );
}

// src/api/analyzerApi.js
export async function analyzeDocument(file, query) {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('query', query);

  const res = await fetch('http://localhost:8000/analyze', {
    method: 'POST',
    body: formData,
  });

  if (!res.ok) throw new Error('Network response was not ok');
  return await res.json();
}

