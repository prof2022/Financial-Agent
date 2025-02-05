from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Budgeting Agent
budgeting_agent = Agent(
    name="Budgeting Agent",
    role="Assist users in creating and managing budgets",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[],  # Add any budgeting-specific tools here
    instructions=[
        "Help users define budgets for different categories such as food, rent, utilities.",
        "Provide insights on budgeting strategies.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Financial Planning Agent
financial_planning_agent = Agent(
    name="Financial Planning Agent",
    role="Help users plan their finances for long-term goals",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[],  # Add any financial planning-specific tools here
    instructions=[
        "Assist users in setting financial goals for retirement, education, or large purchases.",
        "Provide a detailed financial plan with projections.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Transaction Management Agent
transaction_management_agent = Agent(
    name="Transaction Management Agent",
    role="Analyze and manage user transactions",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[],  # Add any tools for transaction management (e.g., API integrations)
    instructions=[
        "Help users track and categorize transactions.",
        "Detect anomalies and highlight duplicate or suspicious transactions.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Investment Advice Agent
investment_advice_agent = Agent(
    name="Investment Advice Agent",
    role="Provide personalized investment advice",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=[
        "Analyze stock data and provide investment recommendations.",
        "Summarize analyst recommendations and stock fundamentals.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Tax Calculator Agent
tax_calculator_agent = Agent(
    name="Tax Calculator Agent",
    role="Calculate and plan taxes for the user",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[],  # Add any tax-specific tools here
    instructions=[
        "Help users estimate their tax liabilities based on income and deductions.",
        "Provide tax-saving strategies and advice.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Multi-Agent System
multi_ai_agent = Agent(
    team=[
        budgeting_agent,
        financial_planning_agent,
        transaction_management_agent,
        investment_advice_agent,
        tax_calculator_agent,
    ],
    instructions=[
        "Work collaboratively to provide comprehensive financial assistance.",
        "Use tables to display data and ensure responses are clear and actionable.",
        "Always include sources if external data is used.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Example Usage
multi_ai_agent.print_response(
    "Create a budget plan for food, rent, and utilities with $2000 income.",
    stream=True,
)

multi_ai_agent.print_response(
    "What are the investment recommendations for NVDA?",
    stream=True,
)

multi_ai_agent.print_response(
    "Estimate taxes for $50,000 annual income with $10,000 deductions.",
    stream=True,
)
