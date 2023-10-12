import sqlite3
conn=sqlite3.connect('assignment2.sqlite')
cur=conn.cursor()
cur.execute('DROP TABLE IF EXISTS counts')
cur.execute('CREATE TABLE counts (email TEXT,count INTEGER)')

fname='dbms.txt'
fh=open(fname)
for line in fh:
    if not line.startswith('From: '):continue
    pieces=line.split();
    email=pieces[1]
    cur.execute('SELECT count FROM counts WHERE email=?',(email,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO counts (email,count) VALUES(?,1)',(email,))
    else:
        cur.execute('UPDATE counts SET count=count+1 WHERE email=?',(email,))
    conn.commit()
sqlstr= 'SELECT email,count FROM counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])