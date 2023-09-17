from sqlalchemy import create_engine,text,insert


db_connection_string= "mysql+pymysql://gio5el1n64q1lqtac0ea:pscale_pw_bH58oQddosjpZS17q3AsI8FA9VNhNzeqcpWPUjn7q61@aws.connect.psdb.cloud/utkarshflaskdb?charset=utf8mb4"

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
       query = text("INSERT INTO rules (triger, cond, act) VALUES (:triger, :cond, :act)")

       conn.execute(query,
                    {
                        "triger":data['triger'],
                        "cond": data['cond'],
                        "act": data['act'] 
                    })
    
    




        
                     



   

