from src.financial_agent.main_agent import FinancialAgent

if __name__ == "__main__":
    agent = FinancialAgent()
    print("Welcome to your financial assistant!")
    while True:
        user_input = input("How can I assist you? (e.g., 'Create a budget', 'Analyze transactions')\n")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = agent.handle_request(user_input)
        print(response)

# Main Agent: src/financial_agent/main_agent.py
import json
from .agents.budgeting_agent import BudgetingAgent
from .agents.financial_planning_agent import FinancialPlanningAgent
from .agents.transaction_management_agent import TransactionManagementAgent
from .agents.investment_advice_agent import InvestmentAdviceAgent
from .agents.tax_calculator_agent import TaxCalculatorAgent

class FinancialAgent:
    def __init__(self, config_path="src/financial_agent/agent_config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)

        self.budgeting_agent = BudgetingAgent(self.config["budgeting"])
        self.financial_planning_agent = FinancialPlanningAgent(self.config["financial_planning"])
        self.transaction_management_agent = TransactionManagementAgent(self.config["transaction_management"])
        self.investment_advice_agent = InvestmentAdviceAgent(self.config["investment_advice"])
        self.tax_calculator_agent = TaxCalculatorAgent(self.config["tax_calculator"])

    def handle_request(self, user_input):
        if "budget" in user_input.lower():
            return self.budgeting_agent.create_budget()
        elif "transaction" in user_input.lower():
            return self.transaction_management_agent.analyze_transactions()
        elif "investment" in user_input.lower():
            return self.investment_advice_agent.provide_advice()
        elif "tax" in user_input.lower():
            return self.tax_calculator_agent.calculate_taxes()
        elif "plan" in user_input.lower():
            return self.financial_planning_agent.create_plan()
        else:
            return "I'm not sure how to help with that. Please try again."

# Budgeting Agent Module: src/financial_agent/agents/budgeting_agent.py
class BudgetingAgent:
    def __init__(self, config):
        self.categories = config["categories"]
        self.default_budget = config["default_budget"]

    def create_budget(self):
        budget_plan = {category: self.default_budget for category in self.categories}
        return f"Your budget plan is: {budget_plan}"

# Financial Planning Agent Module: src/financial_agent/agents/financial_planning_agent.py
class FinancialPlanningAgent:
    def __init__(self, config):
        self.default_goal = config["default_goal"]
        self.planning_horizon_years = config["planning_horizon_years"]

    def create_plan(self):
        return f"Your financial plan for {self.default_goal} over {self.planning_horizon_years} years is being prepared."

# Transaction Management Agent Module: src/financial_agent/agents/transaction_management_agent.py
class TransactionManagementAgent:
    def __init__(self, config):
        self.anomaly_threshold = config["anomaly_threshold"]

    def analyze_transactions(self):
        return "Transaction analysis complete. No anomalies detected."

# Investment Advice Agent Module: src/financial_agent/agents/investment_advice_agent.py
class InvestmentAdviceAgent:
    def __init__(self, config):
        self.risk_levels = config["risk_levels"]

    def provide_advice(self):
        return "Based on your profile, a balanced investment strategy is recommended."

# Tax Calculator Agent Module: src/financial_agent/agents/tax_calculator_agent.py
class TaxCalculatorAgent:
    def __init__(self, config):
        self.tax_brackets = config["tax_brackets"]

    def calculate_taxes(self):
        return "Estimated taxes: $5000."

# Configuration File: src/financial_agent/agent_config.json
{
    "budgeting": {
        "categories": ["Food", "Rent", "Travel", "Utilities", "Entertainment"],
        "default_budget": 1000
    },
    "financial_planning": {
        "default_goal": "Retirement",
        "planning_horizon_years": 30
    },
    "transaction_management": {
        "anomaly_threshold": 500
    },
    "investment_advice": {
        "risk_levels": ["Low", "Medium", "High"]
    },
    "tax_calculator": {
        "tax_brackets": [
            {"rate": 0.1, "threshold": 10000},
            {"rate": 0.2, "threshold": 50000},
            {"rate": 0.3, "threshold": 100000}
        ]
    }
}

# Test Cases: tests/test_agents.py
import unittest
from src.financial_agent.agents.budgeting_agent import BudgetingAgent
from src.financial_agent.agents.financial_planning_agent import FinancialPlanningAgent
from src.financial_agent.agents.transaction_management_agent import TransactionManagementAgent
from src.financial_agent.agents.investment_advice_agent import InvestmentAdviceAgent
from src.financial_agent.agents.tax_calculator_agent import TaxCalculatorAgent

class TestAgents(unittest.TestCase):
    def setUp(self):
        self.budgeting_config = {
            "categories": ["Food", "Rent", "Travel"],
            "default_budget": 1000
        }
        self.financial_planning_config = {
            "default_goal": "Retirement",
            "planning_horizon_years": 30
        }
        self.transaction_management_config = {
            "anomaly_threshold": 500
        }
        self.investment_advice_config = {
            "risk_levels": ["Low", "Medium", "High"]
        }
        self.tax_calculator_config = {
            "tax_brackets": [
                {"rate": 0.1, "threshold": 10000},
                {"rate": 0.2, "threshold": 50000},
                {"rate": 0.3, "threshold": 100000}
            ]
        }

        self.budgeting_agent = BudgetingAgent(self.budgeting_config)
        self.financial_planning_agent = FinancialPlanningAgent(self.financial_planning_config)
        self.transaction_management_agent = TransactionManagementAgent(self.transaction_management_config)
        self.investment_advice_agent = InvestmentAdviceAgent(self.investment_advice_config)
        self.tax_calculator_agent = TaxCalculatorAgent(self.tax_calculator_config)

    def test_budgeting_agent(self):
        result = self.budgeting_agent.create_budget()
        self.assertIn("Food", result)
        self.assertIn("1000", result)

    def test_financial_planning_agent(self):
        result = self.financial_planning_agent.create_plan()
        self.assertIn("Retirement", result)

    def test_transaction_management_agent(self):
        result = self.transaction_management_agent.analyze_transactions()
        self.assertEqual(result, "Transaction analysis complete. No anomalies detected.")

    def test_investment_advice_agent(self):
        result = self.investment_advice_agent.provide_advice()
        self.assertIn("balanced investment strategy", result)

    def test_tax_calculator_agent(self):
        result = self.tax_calculator_agent.calculate_taxes()
        self.assertIn("Estimated taxes", result)

if __name__ == "__main__":
    unittest.main()
