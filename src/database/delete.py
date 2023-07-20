from db_connection import execute_query, create_connection
import psycopg2

def delete_hero(hero_id):
    delete_query = """
    DELETE FROM heroes WHERE id = %s;
    """
    params = (hero_id,)
    execute_query(delete_query, params)

delete_hero(1)