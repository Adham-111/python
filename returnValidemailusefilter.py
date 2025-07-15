import emailvalidation11 as em
emails=["adham@gmial.com","ahmednasser@yahoo.com","ali@","alimohamed@hot.com","ebrahimali@gov.com","asdfdsf","ahmed,com"]
def filterLIstOFemails (x):
    filtered = filter(lambda emails: em.validemail(emails),x)
    return list(filtered)

print(filterLIstOFemails(emails))
