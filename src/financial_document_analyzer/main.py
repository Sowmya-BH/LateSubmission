# from pathlib import Path
import sys
from pathlib import Path

# Add project root to Python path dynamically
ROOT_DIR = Path(__file__).resolve().parents[3]
sys.path.append(str(ROOT_DIR))


from crew import FinancialDocumentAnalysisCrew, DOCUMENT_PATH

def main():
    print("🚀 Starting Financial Document Analysis...\n")
    # crew = FinancialDocumentAnalysisCrew()
    inputs = {
        "document_path": str(DOCUMENT_PATH),
        "initial_analysis_query": "Extract and analyze key financial metrics from Tesla’s Q2 2025 update."
    }

    result = FinancialDocumentAnalysisCrew().crew().kickoff(inputs=inputs)


    print("\n✅ Final Crew Output:\n")
    print(result)


if __name__ == "__main__":
    main()
#
#
#
# # # #!/usr/bin/env python
# # # import sys
# # # import warnings
# # #
# import warnings
# from cryptography.utils import CryptographyDeprecationWarning
#
# warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)
# from crew import FinancialDocumentAnalysisCrew
#
# def main():
#     # Example task run requires inputs (e.g., document_path)
#     # The crew initiation should now be fixed due to the alias
#     try:
#         crew = FinancialDocumentAnalysisCrew()
#         print("🚀 Running Financial Document Analysis Crew...\n")
#
#         inputs = {
#             "document_path": str(DOCUMENT_PATH),
#             "initial_analysis_query": "Summarize key financial highlights and management discussion"
#         }
#
#         result = crew.crew().kickoff(inputs=inputs)
#         print("\n✅ Final Crew Output:\n", result)
#
#         #
#         # runtime_inputs = {
#         #     "document_path": "knowledge/TSLA-Q2-2025-Update.pdf",
#         #     "initial_analysis_query": "Extract the Executive Summary, GAAP Net Income, Operational Cash Flow, and strategic outlook for the next quarter."
#         # }
#         # # You would typically call:
#         # result = crew.crew().kickoff(inputs=runtime_inputs)
#         # print("Crew initialized successfully (KeyError fixed). Ready to run.")
#     except Exception as e:
#         print(f"Error during crew initialization: {e}")
#
# if __name__ == '__main__':
#     main()
#
# # # from datetime import datetime
# # from crew import FinancialDocumentAnalysisCrew
# # from tools.custom_tool import InvestmentTool, RiskAssessmentTool, StatsTool, CalculatorTool #CalculatorTools
# # from crewai_tools import ScrapeWebsiteTool, WebsiteSearchTool, DirectoryReadTool, SerperDevTool
# #
# # import os
# # from pathlib import Path
# #
# #
# # # -------------------------
# # # TOOL INSTANCES
# # # -------------------------
# # investment_tool = InvestmentTool()
# # risk_assessment_tool = RiskAssessmentTool()
# stats_tool = StatsTool()
# calculator_tool = CalculatorTool()
# # Instantiate tools
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# KNOWLEDGE_DIR = os.path.join(BASE_DIR, "knowledge")
#
# directory_reader = DirectoryReadTool(directory=KNOWLEDGE_DIR)
# # file_reader = FileReadTool()
# search_tool = SerperDevTool()
# scrape_tool = ScrapeWebsiteTool()
#
#
# def main():
#     """
#     Entry point for running the Financial Document Analysis Crew workflow.
#     """
#
#     # Initialize the Crew
#     crew = FinancialDocumentAnalysisCrew()
#
#     # Kick off the workflow — runs all tasks in sequential order
#     result = crew.crew().run()
#
#     # Print or save the final structured result
#     print("\n\n################################################")
#     print("📊 FINAL FINANCIAL ANALYSIS RESULT:")
#     print("################################################\n")
#     print(result)
#
# if __name__ == "__main__":
#     main()
#
# # from financial_document_analyzer.crew import FinancialDocumentAnalyzer
# #
# # warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
# #
# # # This main file is intended to be a way for you to run your
# # # crew locally, so refrain from adding unnecessary logic into this file.
# # # Replace with inputs you want to test with, it will automatically
# # # interpolate any tasks and agents information
# #
# # GROQ_API_KEY = "YOUR_GROQ_API_KEY"
# #
# # llm_llama70b = ChatGroq(model_name="llama-3.1-70b-versatile", groq_api_key=GROQ_API_KEY)
# #
# #
# #
# #
# # def run():
# #     """
# #     Run the crew.
# #     """
# #     inputs = {
# #         'topic': 'AI LLMs',
# #         'current_year': str(datetime.now().year)
# #     }
# #
# #     try:
# #         FinancialDocumentAnalyzer().crew().kickoff(inputs=inputs)
# #     except Exception as e:
# #         raise Exception(f"An error occurred while running the crew: {e}")
# #
# #
# # def train():
# #     """
# #     Train the crew for a given number of iterations.
# #     """
# #     inputs = {
# #         "topic": "AI LLMs",
# #         'current_year': str(datetime.now().year)
# #     }
# #     try:
# #         FinancialDocumentAnalyzer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
# #
# #     except Exception as e:
# #         raise Exception(f"An error occurred while training the crew: {e}")
# #
# # def replay():
# #     """
# #     Replay the crew execution from a specific task.
# #     """
# #     try:
# #         FinancialDocumentAnalyzer().crew().replay(task_id=sys.argv[1])
# #
# #     except Exception as e:
# #         raise Exception(f"An error occurred while replaying the crew: {e}")
# #
# # def test():
# #     """
# #     Test the crew execution and returns the results.
# #     """
# #     inputs = {
# #         "topic": "AI LLMs",
# #         "current_year": str(datetime.now().year)
# #     }
# #
# #     try:
# #         FinancialDocumentAnalyzer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
# #
# #     except Exception as e:
# #         raise Exception(f"An error occurred while testing the crew: {e}")
