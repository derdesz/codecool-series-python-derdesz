from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')



def pa2():
    return data_manager.execute_select("""
    SELECT 
        date_part('year', year)::integer AS year,
        ROUND(AVG(rating),2) AS average_rating,
        COUNT (id) AS show_count
    FROM shows 
    WHERE date_part('year', year) >= 1970 AND date_part('year', year) <= 2010
    GROUP BY year
    ORDER BY year ASC;
    """)
