import psycopg2

conn = psycopg2.connect(
    dbname="youtube_analysis",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

def insert_comment(video_id, comment):
    cursor.execute("INSERT INTO youtube_comments (video_id, comment) VALUES (%s, %s)", (video_id, comment))
    conn.commit()

for item in comment.get("items", []):
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    insert_comment(VIDEO_ID, comment)
