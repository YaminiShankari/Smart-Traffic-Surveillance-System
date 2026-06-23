from supabase import create_client

SUPABASE_URL = "https://wqgsqmxtlyljqevlnyfs.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndxZ3NxbXh0bHlsanFldmxueWZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE5NTI5NTQsImV4cCI6MjA5NzUyODk1NH0.64svAUsFBebpgQkFWvbV2aCemBY8_V7v2iVJw2jMIIc"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

response = (
    supabase
    .table("vehicles")
    .select("*")
    .execute()
)

print(response.data)