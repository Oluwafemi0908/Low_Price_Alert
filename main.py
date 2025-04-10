from online_store import OnlineStore
from send_mail import SendMail

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
store = OnlineStore(url)
send_mail = SendMail()
condition = store.compare_price(100)
send_mail.send_to(condition, store.subject, store.body)
