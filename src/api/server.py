from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from financial_document_analyzer.crew import FinancialDocumentAnalysisCrew
import tempfile
import os

app = FastAPI()

# Allow frontend access (React runs on localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...), query: str = Form(...)):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(await file.read())
            temp_file_path = temp_file.name

        # Initialize Crew and run
        crew = FinancialDocumentAnalysisCrew()
        result = crew.crew().kickoff(inputs={
            "document_path": temp_file_path,
            "initial_analysis_query": query
        })

        # Return structured output
        return {"result": str(result)}

    except Exception as e:
        return {"error": str(e)}

    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

