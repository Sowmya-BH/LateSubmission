# src/financial_document_analyzer_sub/tools/pdf_ingestion_tool.py

from crewai_tools import FileReadTool
from crewai.tools import BaseTool
import os


class PDFIngestionTool(BaseTool):
    """
    Custom tool to read a financial document (PDF) and return its raw text.
    """
    name: str = "pdf_ingestion_tool"
    description: str = (
        "Reads and extracts text from a PDF document. "
        "Input must be a valid path to a PDF file."
    )

    def _run(self, pdf_path: str) -> str:
        """
        Input: Absolute or relative PDF path.
        Returns: Extracted text content.
        """
        try:
            if not os.path.exists(pdf_path):
                return f"Error: File not found at path: {pdf_path}"

            file_reader = FileReadTool(file_path=pdf_path)
            content = file_reader.run()

            if not content:
                return "Error: No readable content extracted from the file."

            return f"PDF Content Extracted Successfully:\n\n{content[:2000]}..."  # trim for readability

        except Exception as e:
            return f"Error during PDF ingestion: {e}"
