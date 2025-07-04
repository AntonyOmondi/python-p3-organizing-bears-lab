select_all_female_bears_return_name_and_age = """
    SELECT NAME, AGE FROM bears WHERE SEX = "F";
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT NAME FROM bears ORDER BY NAME ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT NAME, AGE FROM bears WHERE ALIVE = TRUE ORDER BY AGE ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT NAME, AGE FROM bears ORDER BY AGE DESC LIMIT 1;
"""
select_youngest_bear_and_returns_name_and_age = """
    SELECT NAME, AGE FROM bears ORDER BY AGE ASC LIMIT 1;
"""