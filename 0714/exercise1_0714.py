#[실습4]

time = 32140
hours = time//3600
mins = (time - (hours*3600))//60
secs = time-(hours*3600)-(mins*60)

print(hours, "시간 ", mins, "분 ", secs, "초", sep='')