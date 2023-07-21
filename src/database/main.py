from db_connection import execute_query, create_connection
import psycopg2


#CREATE
def create_hero():
    name = input("What is your superhero name? ")
    about_me = input("Tell us a little about you: ")
    biography = input("Give us an in depth bio about you. How did you get your powers? ")
    query = """
        INSERT INTO heroes (name, about_me, biography)
        VALUES (%s, %s, %s)
        """
    execute_query(query,(name, about_me, biography))

create_hero()


#READ
def show_all_heros():
    heros = []
    query = """
        SELECT * from heroes
        ORDER BY id;
"""
    
    data = execute_query(query)
    for hero in data:
        heros.append(hero[1])
    print(heros)

show_all_heros()

#UPDATE

def update_about_me(id, new_about_me):
    update_query = """
    UPDATE heroes SET about_me = %s WHERE id = %s;
    """
    params = (new_about_me, id)
    execute_query(update_query, params)

update_about_me(3, "I have heat vision, super strength, and can fly" )

#DELETE

def delete_hero(hero_id):
    delete_query = """
    DELETE FROM heroes WHERE id = %s;
    """
    execute_query(delete_query, hero_id)

 
