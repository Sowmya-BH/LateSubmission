# tools/custom_tool.py

import os
import json
import math
from pathlib import Path
from crewai.tools import BaseTool
import crewai_tools
import logging

# src/financial_document_analyzer_sub/tools/__init__.py

# from .pdf_ingestion_tool import PDFIngestionTool
# from .investment_tool import InvestmentTool
# from .risk_assessment_tool import RiskAssessmentTool
# from .calculator_tool import CalculatorTool



logger = logging.getLogger(__name__)

# Base folder for all documents
KNOWLEDGE_DIR = "financial_document_analyzer_sub/knowledge"

# ==========================================================
# ✅ RISK ASSESSMENT TOOL (modernized)
# ==========================================================
class RiskAssessmentTool(BaseTool):
    """
    Lightweight tool that reads a processed financial document and performs a mock risk assessment.
    """
    name: str = "risk_assessment_tool"
    description: str = (
        "Analyzes a document for operational, financial, or regulatory risks based on a query."
    )

    def _run(self, input_string: str) -> str:
        try:
            parts = [p.strip() for p in input_string.split(',', 1)]

            # Either: "DOCUMENT_PATH, QUERY" or just "QUERY"
            document_filter = None
            query = input_string
            if len(parts) == 2:
                document_filter, query = parts

            # Use FileReadTool if document path provided
            if document_filter and Path(document_filter).exists():
                file_tool = FileReadTool(file_path=document_filter)
                content = file_tool.run()
                content_length = len(content)
            else:
                content_length = 0

            # Simulate analysis
            return (
                f"Risk Assessment Completed ⚠️\n"
                f"Query: {query}\n"
                f"Analyzed document: {document_filter or 'N/A'}\n"
                f"Document length analyzed: {content_length} chars\n"
                f"Result: Simulated risk summary (e.g., high debt exposure, supply chain risk, etc.)"
            )

        except Exception as e:
            return f"Risk assessment error: {e}"



# ==========================================================
# ✅ COLLECTION STATS TOOL (modernized)
# ==========================================================
class StatsTool(BaseTool):
    """
    Provides simple statistics about documents stored in the knowledge directory.
    """
    name: str = "collection_stats_tool"
    description: str = "Retrieves basic statistics about available documents in the knowledge directory."

    def _run(self, _: str = "") -> str:
        try:
            base = Path(KNOWLEDGE_DIR)
            if not base.exists():
                return "No knowledge directory found."

            pdf_files = list(base.glob("*.pdf"))
            total_size = sum(f.stat().st_size for f in pdf_files)
            count = len(pdf_files)

            return (
                f"Knowledge Base Stats 📊\n"
                f"Total Documents: {count}\n"
                f"Total Size: {round(total_size / 1024, 2)} KB\n"
                f"Files: {[f.name for f in pdf_files]}"
            )

        except Exception as e:
            return f"StatsTool error: {e}"



# ==========================================================
# ✅ CALCULATOR TOOL
# ==========================================================
class CalculatorTool(BaseTool):
    """
    Simple calculator tool for performing arithmetic or financial computations.
    Example input: 'NPV 10000 0.1 5' or '2 + 3 * 4'
    """
    name: str = "calculator_tool"
    description: str = "Performs simple arithmetic or financial calculations (NPV, ROI, etc.)."

    def _run(self, expression: str) -> str:
        try:
            # Support some keywords
            tokens = expression.strip().split()
            cmd = tokens[0].lower()

            # Financial operations
            if cmd == "npv":
                # Example: NPV cashflow discount_rate years
                if len(tokens) < 4:
                    return "Usage: NPV initial_investment rate years"
                cf, rate, years = float(tokens[1]), float(tokens[2]), int(tokens[3])
                npv = cf / ((1 + rate) ** years)
                return f"NPV after {years} years at {rate*100:.1f}% = {npv:.2f}"

            elif cmd == "roi":
                if len(tokens) < 3:
                    return "Usage: ROI profit cost"
                profit, cost = float(tokens[1]), float(tokens[2])
                roi = ((profit - cost) / cost) * 100
                return f"ROI = {roi:.2f}%"

            # Generic math expression
            result = eval(expression, {"__builtins__": None}, math.__dict__)
            return f"Result: {result}"
        except Exception as e:
            return f"Calculation error: {e}"
