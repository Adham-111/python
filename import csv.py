import csv
import emailvalidation11 as em
import domain_part as dp
emails=[]
file=open("C:\\Users\\2025\\Downloads\\employees.csv","r",newline="")
read=csv.reader(file)
for row in read :
    if len(row)> 2:
        email=row[1]
        emails.append(email)
valid_emails=filter(em.validemail,emails)
valid_emails=list(valid_emails)
domain_list=dp.domain(valid_emails)
unique_domain=set(domain_list)
print(unique_domain)

print(valid_emails)