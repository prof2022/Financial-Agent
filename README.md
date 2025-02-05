# Financial AI Multi-Agent System

## Overview
This project is a **Financial AI Multi-Agent System** designed to provide a comprehensive suite of financial services through collaborative subagents. Each subagent specializes in a specific financial domain, such as budgeting, financial planning, transaction management, investment advice, and tax calculations. The agents utilize advanced AI models and tools to deliver accurate, actionable insights and assist users in managing their finances efficiently.

## Features
### Subagents
1. **Budgeting Agent**:
   - Role: Assists users in creating and managing budgets.
   - Key Features:
     - Define budgets for different categories (e.g., food, rent, utilities).
     - Provide insights and strategies for effective budgeting.

2. **Financial Planning Agent**:
   - Role: Helps users set and achieve long-term financial goals.
   - Key Features:
     - Create plans for retirement, education, or large purchases.
     - Provide projections and detailed goal-based strategies.

3. **Transaction Management Agent**:
   - Role: Analyzes and manages user transactions.
   - Key Features:
     - Track and categorize financial transactions.
     - Detect anomalies, duplicates, and suspicious transactions.

4. **Investment Advice Agent**:
   - Role: Offers personalized investment advice.
   - Key Features:
     - Analyze stock data, fundamentals, and analyst recommendations.
     - Provide actionable investment strategies and news insights.

5. **Tax Calculator Agent**:
   - Role: Estimates and plans taxes for users.
   - Key Features:
     - Calculate tax liabilities based on income and deductions.
     - Suggest tax-saving strategies and provide filing assistance.

### Multi-Agent Collaboration
A **Multi-Agent System** integrates these subagents to provide users with seamless, collaborative financial assistance. Global instructions ensure consistent, high-quality responses, and data is presented in user-friendly formats (e.g., tables).

## Architecture
The project uses the following technologies:
- **Phi Framework**: Manages agent creation, tool integration, and communication.
- **Groq Model**: An advanced AI model for processing and reasoning.
- **Tools**:
  - `DuckDuckGo`: Provides web search capabilities for real-time information retrieval.
  - `YFinanceTools`: Fetches financial data, including stock prices, fundamentals, and analyst recommendations.
- **Python**: Core programming language.
- **dotenv**: Securely manages environment variables, such as API keys.

### Subagent Design
Each subagent is implemented as an instance of the `Agent` class, with:
- A **role** describing its primary purpose.
- A **model** (e.g., Groq) configured for its specific tasks.
- **Tools** to enhance functionality, such as data fetching or web search.
- **Instructions** guiding behavior and response formatting.

### Multi-Agent System
The multi-agent system (`multi_ai_agent`) coordinates the subagents to:
1. Delegate queries to the appropriate agent.
2. Aggregate responses from multiple agents when necessary.
3. Format outputs as user-friendly tables with clear, actionable insights.

## Installation
### Prerequisites
1. Python 3.8+
2. `pip` (Python package manager)
3. API keys for external services (e.g., OpenAI, YFinance).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/financial-ai-multi-agent.git
   cd financial-ai-multi-agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

4. Run the project:
   ```bash
   python main.py
   ```

## Usage
### Example Commands
1. **Budgeting**:
   ```text
   Create a budget plan for food, rent, and utilities with $2000 income.
   ```

2. **Financial Planning**:
   ```text
   Help me plan for retirement in 20 years with an annual savings of $10,000.
   ```

3. **Transaction Management**:
   ```text
   Analyze recent transactions and identify any anomalies.
   ```

4. **Investment Advice**:
   ```text
   What are the investment recommendations for NVDA?
   ```

5. **Tax Calculation**:
   ```text
   Estimate taxes for $50,000 annual income with $10,000 deductions.
   ```

## File Structure
```
.
├── main.py                        # Entry point for the application
├── src/
│   ├── financial_agent/
│   │   ├── main_agent.py          # Multi-agent system coordination
│   │   ├── agents/
│   │   │   ├── budgeting_agent.py
│   │   │   ├── financial_planning_agent.py
│   │   │   ├── transaction_management_agent.py
│   │   │   ├── investment_advice_agent.py
│   │   │   └── tax_calculator_agent.py
│   │   └── agent_config.json      # Configuration for subagents
├── tests/
│   └── test_agents.py             # Unit tests for subagents
├── requirements.txt               # Python dependencies
├── .env                           # Environment variables
└── README.md                      # Project documentation
```

## Testing
Run unit tests to validate the functionality of each subagent:
```bash
python -m unittest discover tests/
```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Submit a pull request with a clear description of changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Future Enhancements
- Add support for additional financial tools and APIs.
- Enable multi-language support for global users.
- Incorporate machine learning models for personalized recommendations.
