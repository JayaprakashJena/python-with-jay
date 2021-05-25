import pyodbc                                                                      
def read(conn):
    print ('read')
                                                                                   
    cursor.execute("select * from dummyy")                                           
    for row in cursor:                                                                 
        print()
def create(conn):                                                                    
    print('create')
    cursor=conn.cursor()
    cursor.execute(                                                                  
        'insert into dummyy(a,b) values (?,?);',                                       
        (3232,'catzzz')                                                              

    )                                                                                
    conn.commit()
    read(conn)                                                                        

def update(conn):                                                                         
    print('update')                                                                       
    cursor=conn.cursor()                                                                  
    cursor.execute(                                                                        
    'update dummyy set b=? where a =?;',                                                  
    ('dogzzz',3232)                                                               
    )
    conn.commit()
    read(conn)
def delete(conn):                                                                 
    print('delete')
    cursor=conn.cursor()
    cursor.execute(
    'delete from dummyy where a>5',                                             
    )                                                                           
    conn.commit()
    read(conn)
conn=pyodbc.connect(                                                            
    "Driver= {SQL server};"                                                     
    "server=.;"
    "database=master;"                                                          
    "Trusted_connectioon=yes;"                                                    