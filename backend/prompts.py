SCHEMA_DESCRIPTION = """
Database Schema:

Table: projects
Columns:
id, customer_name, project_code, project_name,
project_type, project_manager, start_date,
end_date, created_at, updated_at


Table: project_sites
Columns:
id, project_id, project_name, site_name,
city, state, status, site_readiness,
created_at, updated_at

Status meanings:
status → Pending / Completed / In Progress
site_readiness → Ready / Not Ready / Partially Ready


Table: activities
Columns:
id, project_id, site_name, activity_category,
remarks, status, created_at

Status meanings:
status → Open / Closed / In Progress


Table: project_supplies
Columns:
id, project_id, item_name,
required_qty, delivered_qty, remarks


Relationships:
projects.id = project_sites.project_id
projects.id = activities.project_id
projects.id = project_supplies.project_id


Rules:
- Generate ONLY SELECT queries.
- NEVER use SELECT *
- Use DISTINCT whenever duplicates may occur.
- Use GROUP BY for counting.
- Use JOINs when data spans multiple tables.
- If user asks about cities → use project_sites.city
- If user asks about supplies → use project_supplies
- If user asks about activities → use activities
- If user asks about site readiness → use project_sites.site_readiness
- If user asks about project/site status → use project_sites.status
- If user asks about activity status → use activities.status
- Return ONLY the SQL query.
"""
