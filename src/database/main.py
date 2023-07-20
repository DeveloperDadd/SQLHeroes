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
    query = """
        SELECT * from heroes
"""
    data = execute_query(query)
    if data:
        for row in data:
            id, name, about_me, biography = row
            print(f"Hero ID: {id}, Name: {name}, Ability: {about_me}, Bio: {biography}")

show_all_heros()

#UPDATE

def update_about_me(about_me):
    new_about_me = input("Change your about me (if you discovered or lost a power) ")
    query = """
    UPDATE heroes
    SET about_me = %s
    WHERE %s = heroes.name
    """
    execute_query(query, (new_about_me, hero))

update_about_me()

#DELETE

def delete_hero(hero_id):
    delete_query = """
    DELETE FROM heroes WHERE id = %s;
    """
    execute_query(delete_query, hero_id)

 
