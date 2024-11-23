from datetime import datetime

from .database import Database


class KinoDatabase(Database):
    def create_table_kino(self):
        sql="""
            CREATE TABLE IF NOT EXISTS Kino(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                post_id BIGINT NOT NULL UNIQUE,
                file_id VARCHAR(2000) NOT NULL,
                caption TEXT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME
                ); 
            """
        self.execute(sql,commit=True)

    def add_kino(self,post_id:int,file_id:str,caption:str):
        sql="""
            INSERT INTO Kino(post_id,file_id,caption,created_at,updated_at)
            VALUES(?,?,?,?,?)
            """
        timestamp=datetime.now().isoformat()
        self.execute(sql,parameters=(post_id,file_id,caption,timestamp,timestamp),commit=True)

    def update_kino_caption(self,new_caption:str,post_id:int):
        sql="""
            UPDATE Kino
            SET caption=?,updated_at=?,
            WHERE post_id=?
        
            """
        updated_time=datetime.now().isoformat()
        self.execute(sql,parameters=(new_caption,updated_time,post_id),commit=True)

    def get_kino_by_post_id(self,post_id:int):
        sql="""
            SELECT file_id,caption FROM Kino
            WHERE post_id=?
            """
        result=self.execute(sql,parameters=(post_id,),fetchone=True)
        return {'file_id':result[0],'caption':result[1] if result else None}

    def delete_kino_by_postid(self,post_id:int):
        sql="""
            DELETE FROM Kino WHERE post_id=?    
        """
        self.execute(sql,parameters=(post_id,),commit=True)

    def get_movies_hafta(self):
        sql = """
            SELECT name FROM Kino
            WHERE DATE(created_at) >= DATE('now', '-7 days')
        """
        return self.execute(sql, fetchall=True)

    def get_movies_oy(self):
        sql = """
             SELECT name FROM Kino
             WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
         """
        return self.execute(sql, fetchall=True)

    def get_movies_bugun(self):
        sql = """
            SELECT name FROM Kino
            WHERE DATE(created_at) = DATE('now')
        """
        return self.execute(sql, fetchall=True)
    def count_kino(self):
        sql = """
            SELECT COUNT(*) FROM Kino
        """
        result = self.execute(sql, fetchone=True)
        return result[0] if result else 0

    def count_users(self):
        sql="""
            SELECT COUNT(*) FROM Users
            """
        self.execute(sql,fetchone=True)

    def get_movie_by_post_id(self, post_id: int):
        sql = """
            SELECT file_id, caption FROM Kino
            WHERE post_id=?
        """
        result = self.execute(sql, parameters=(post_id,), fetchone=True)
        if result:
            return {
                'file_id': result[0],
                'caption': result[1]
            }
        return None