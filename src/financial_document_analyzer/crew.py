import os
from pathlib import Path
from dotenv import load_dotenv
from crewai import Agent, Crew, Task, Process

from crewai.project import CrewBase, agent, task, crew
from crewai import LLM

# Import tools
from tools.pdf_ingestion_tool import PDFIngestionTool
from tools.investment_tool import InvestmentTool
from tools.risk_assessment_tool import RiskAssessmentTool, StatsTool, CalculatorTool
from crewai_tools import PDFSearchTool

load_dotenv()

# ---------------------------------------------------------------------------
# LLM CONFIGURATION
# ---------------------------------------------------------------------------
llm = LLM(
    # provider="groq",
    model="groq/llama-3.1-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
)

# ---------------------------------------------------------------------------
# PATH CONFIGURATION
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
AGENTS_PATH = BASE_DIR / "config" / "agents.yaml"
TASKS_PATH = BASE_DIR / "config" / "tasks.yaml"
DOCUMENT_PATH ="/Users/bhupatiraju/Downloads/financial-document-analyzer-debug/financial_document_analyzer"
#BASE_DIR / "knowledge" / "TSLA-Q2-2025-Update.pdf

# ---------------------------------------------------------------------------
# TOOL INITIALIZATION
# ---------------------------------------------------------------------------
# pdf_ingestion_tool=PDFIngestionTool(document_path=str(DOCUMENT_PATH))
file_read_tool=FileReadTool(file_path=str(DOCUMENT_PATH)),

# ---------------------------------------------------------------------------
# CREW DEFINITION
# ---------------------------------------------------------------------------
@CrewBase
class FinancialDocumentAnalysisCrew:
    """Crew for multi-stage financial document analysis."""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # -----------------------------------------------------------------------
    # Agents
    # -----------------------------------------------------------------------
    @agent
    def financial_analyst(self) -> Agent:
        """Agent responsible for document ingestion and analysis."""
        return Agent(
            config=self.agents_config["financial_analyst"],
            verbose=True,
            llm=llm,
            tools=[
                PDFIngestionTool(document_path=str(DOCUMENT_PATH)),
                InvestmentTool(),
                FileReadTool(file_path=str(DOCUMENT_PATH)),
                CalculatorTool(),
            ],
        )

    @agent
    def risk_assessor(self) -> Agent:
        """Agent responsible for risk detection and classification."""
        return Agent(
            config=self.agents_config["risk_assessor"],
            verbose=True,
            llm=llm,
            tools=[
                RiskAssessmentTool(),
                StatsTool(),
            ],
        )

    @agent
    def verifier(self) -> Agent:
        """Agent responsible for verification and recommendation validation."""
        return Agent(
            config=self.agents_config["verifier"],
            verbose=True,
            llm=llm,
            tools=[
                PDFIngestionTool(document_path=str(DOCUMENT_PATH)),
                RiskAssessmentTool(),
                InvestmentTool(),
                CalculatorTool(),
                file_read_tool,
            ],
        )

    @agent
    def investment_advisor(self) -> Agent:
        """Agent responsible for trade strategy synthesis."""
        return Agent(
            config=self.agents_config["investment_advisor"],
            verbose=True,
            llm=llm,
            tools=[
                PDFIngestionTool(document_path=str(DOCUMENT_PATH)),
                InvestmentTool(),
                RiskAssessmentTool(),
            ],
        )

    # -----------------------------------------------------------------------
    # Tasks
    # -----------------------------------------------------------------------
    @task
    def document_ingestion_and_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["document_ingestion_and_analysis_task"],
            agent=self.financial_analyst(),
        )

    @task
    def detailed_financial_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["detailed_financial_analysis_task"],
            agent=self.financial_analyst(),
        )

    @task
    def extreme_risk_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config["extreme_risk_assessment_task"],
            agent=self.risk_assessor(),
        )

    @task
    def risk_tolerance_verification_task(self) -> Task:
        return Task(
            config=self.tasks_config["risk_tolerance_verification_task"],
            agent=self.verifier(),
        )

    @task
    def optimal_trade_strategy_task(self) -> Task:
        return Task(
            config=self.tasks_config["optimal_trade_strategy_task"],
            agent=self.investment_advisor(),
        )

    @task
    def validate_investment_risk(self) -> Task:
        return Task(
            config=self.tasks_config["validate_investment_risk"],
            agent=self.verifier(),
        )

    # -----------------------------------------------------------------------
    # Crew Assembly
    # -----------------------------------------------------------------------
    @crew
    def crew(self) -> Crew:
        """Creates the Financial Document Analysis Crew."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


# ---------------------------------------------------------------------------
# EXPORTS
# ---------------------------------------------------------------------------
DOCUMENT_PATH = DOCUMENT_PATH

