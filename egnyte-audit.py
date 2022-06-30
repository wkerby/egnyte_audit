import pandas as pd
#create dfs for the egnyte user spreadsheet and smartsheet user spreadsheet
egnyte_df = pd.read_excel(r'Z:\\Users\\WKerby\\My Computer\\Documents\\Egnyte External Power Users 05-06-2022.xlsx')
ss_df = pd.read_excel(r'Z:\\Users\\WKerby\\My Computer\\Documents\\Smartsheet-Egnyte External Power Users 05-06-2022.xlsx')

#obtain list of emails from egnyte user spreadsheet and smartsheet user spreadsheet
ss_emails = list(ss_df.loc[:, "Email"].loc[ss_df["User Type"] == "power"])
egnyte_emails = list(egnyte_df.loc[:, "Email"])

#clean the emails so that they are not case sensitive
lower_egnyte_emails = []
lower_ss_emails = []
for email in ss_emails:
	lower_ss_emails.append(email.lower())
for email in egnyte_emails:
	lower_egnyte_emails.append(email.lower())

#left outer join
add_emails = []
for email in lower_egnyte_emails:
	if email not in lower_ss_emails: 
		add_emails.append(email)

add_emails_dict = {"Email":add_emails}
add_emails_df = pd.DataFrame(add_emails_dict)
add_emails_df.to_excel(r"Z:\\Users\\WKerby\\My Computer\\Documents\\Egnyte External Power Users Add.xlsx", index = False)




