from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import re

from prompts import SCHEMA_DESCRIPTION


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


SQL_PROMPT = ChatPromptTemplate.from_messages([
    ("system", SCHEMA_DESCRIPTION),
    ("human", "{question}")
])


def generate_sql(question):

    chain = SQL_PROMPT | llm

    response = chain.invoke({"question": question})

    sql = response.content.strip()

    sql = re.sub(r"```sql|```", "", sql).strip()

    if not sql.lower().startswith("select"):
        return None

    return sql
