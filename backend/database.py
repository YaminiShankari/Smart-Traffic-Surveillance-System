from supabase import create_client

SUPABASE_URL = "ENTER_YOUR_SUPABASE_URL"
SUPABASE_KEY = "ENTER_YOUR_SUPABASE_KEY"

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

def check_vehicle(plate_number):

    response = (
        supabase
        .table("vehicles")
        .select("*")
        .eq("plate_number", plate_number)
        .execute()
    )

    return response.data
