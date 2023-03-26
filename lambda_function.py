import json
from boto3 import client
import pymysql
import re

def read_file(bucket_name, object_key):
    s3_cient = client('s3')
    print(s3_cient)
    resp = s3_cient.get_object(Bucket=bucket_name, Key=object_key)
    return resp['Body'].read().decode('utf-8').split('\n')

def lambda_handler(event, context):
    rds_endpoint  = "transacao-test.casiscny7uhd.sa-east-1.rds.amazonaws.com"
    username = "admin"
    password = "Essasenha." # RDS Mysql password
    db_name = "shop" # RDS MySQL DB name
    conn = None
    try:
        conn = pymysql.connect(host=rds_endpoint, port=3306, user=username,
                               password=password, database=db_name,
                               cursorclass=pymysql.cursors.DictCursor)
        print("Conection", conn)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")

    print(event)
    # TODO implement
    data = read_file(event['bucket_name'], event['object_key'])
    print('DATA ->',data[0])

    try:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE Companies ( id INT NOT NULL AUTO_INCREMENT,
                      cpf_proprietario varchar(255),
                      cnpj varchar(255),
                      data_inicio DATE,
                      nome_empresa varchar(255),
                      atuacao varchar(255),
                      PRIMARY KEY (id))""")
        conn.commit()
    except:
        pass

    with conn.cursor() as cur:
        for row in data:
            try:
                row_list = row.split(',')
                print("try", row_list[0])
                cur.execute("INSERT INTO Companies (cpf_proprietario, cnpj,\
                             data_inicio, nome_empresa, atuacao) \
                             VALUES ("+re.sub('\W+','', str(row_list[0]))+",\
                             "+re.sub('\W+','', str(row_list[1]))+",\
                             "+re.sub('\W+','', str(row_list[2]))+"\
                             ,'"+row_list[3]+"','"+row_list[4]+"')")
                conn.commit()
            except:
                print(Exception())
    if conn:
        conn.commit()

    return {
        'statusCode': 200,
        'message': json.dumps('CSV was save in DB')
    }
