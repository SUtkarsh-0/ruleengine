from sqlalchemy import create_engine,text,insert


db_connection_string = "mysql+pymysql://k7wbyj4eh117ddkjctni:pscale_pw_FylCMlLpehAsNo4kZiSoJ3zByC2vImqW1ezBIcsljct@aws.connect.psdb.cloud/utkarshflaskdb?charset=utf8mb4"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl":{
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    } )

def load_rules_from_db():
     with engine.connect() as conn:
        result = conn.execute(text("select * from rules")) #sql query executor
        rules = []
        for row in result.all():
            rules.append(row._asdict())
        return rules
     
def add_rule_to_db(data):
    with engine.connect() as conn:
       query = text("INSERT INTO rules (triger, cond, act, val) VALUES (:triger, :cond, :act, :val)")

       conn.execute(query,
                    {
                        "triger":data['triger'],
                        "cond": data['cond'],
                        "act": data['act'],
                        "val": data['val'],

                    })
    
    
def delete_rule_from_db(id):
    with engine.connect() as conn:
        query= text("delete from rules where rules.id = :id")

        conn.execute(query,
                     {
                         "id":id
                     })




        
                     



   

