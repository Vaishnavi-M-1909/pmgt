# PMGT Assistant – LLM-Powered Text-to-SQL Chatbot

## Overview

PMGT Assistant is an interactive chatbot that converts natural language queries into SQL queries and retrieves structured results from a relational database.

The system uses a Large Language Model (LLM) to dynamically generate SQL queries based on the defined schema. It supports JOINs, aggregations, DISTINCT-safe counting, and structured conversational flow with runtime memory.

This project demonstrates schema-aware text-to-SQL generation with safety constraints and conversational interactivity.

---

## Key Features

* LLM-driven natural language → SQL query generation
* Support for JOINs, GROUP BY, HAVING, ORDER BY, and CTE queries
* DISTINCT-safe aggregation to prevent duplicate counting
* SELECT-only query enforcement for safety
* Runtime conversational memory with user onboarding
* Phone number normalization (international format with country code)
* Email validation
* Graceful error handling (no raw database errors exposed)
* Dynamic handling of out-of-scope city/state queries
* Safety constraints to prevent heavy queries (no `SELECT *`, result size control)

---

## Architecture

```
User Input
    ↓
LangGraph State Node
    ↓
LLM → SQL Generation
    ↓
MySQL Execution (SELECT-only)
    ↓
Structured Response via LLM
```

### Module Structure

* `app.py` → CLI interface and session handling
* `graph.py` → State management, business logic, query flow
* `db.py` → Database connection and secure SQL execution
* `llm.py` → LLM configuration
* `prompts.py` → SQL generation constraints and safety rules
* `meaning.py` → Business interpretation rules

---

## Database Schema

The chatbot operates on the following tables:

* `projects`
* `project_sites`
* `activities`
* `project_supplies`

### Relationships

* `projects.id = project_sites.project_id`
* `projects.id = project_supplies.project_id`
* `project_sites.site_name = activities.site_name`

The system supports multi-table JOIN queries and DISTINCT-safe aggregation to ensure accurate results.

---

## Conversational Capabilities

* User onboarding (name, phone, email capture)
* Runtime memory recall (e.g., “What is my name?”)
* Interactive conversational flow
* Context-aware responses
* Controlled responses for unsupported cities
* Presence handling (“Are you there?”)

---

## Safety & Design Considerations

To reduce system risk and prevent heavy database load:

* Only `SELECT` queries are allowed (no UPDATE/DELETE/DROP).
* `SELECT *` is restricted.
* DISTINCT rules are enforced for aggregation.
* Result size is capped before sending data to the LLM.
* Errors are handled gracefully without exposing raw DB errors.
* Recommended usage with a read-only database user.

This ensures the system remains safe even when handling dynamically generated SQL.

---

## Setup Instructions

### 1. Clone the Repository

```
git clone <repository-url>
cd pmgt-assistant
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file using the provided `.env.example`:

```
OPENROUTER_API_KEY=your_api_key_here
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_NAME=pmgt
```

### 4. Run the Application

```
python app.py
```

The assistant will start in CLI mode.

---

## Example Queries

* How many projects are closed?
* Which sites are not ready?
* How many activities have power issues?
* Which projects start in November?
* Which cities are you currently operating in?
* Are you planning in Jaipur?

---

## Current Scope

* Designed for structured relational queries.
* Uses dummy/sample data for development and testing.
* Optimized for correctness and safety rather than high-volume production deployment.

---

## Future Improvements

* PostgreSQL compatibility layer
* Query cost estimation and optimization
* Pagination for large result sets
* Persistent memory across sessions
* Structured intent classification before SQL generation
* Web interface integration
