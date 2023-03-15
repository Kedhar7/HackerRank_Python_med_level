from datetime import datetime, timezone

def get_time_diff(t1, t2):
    dt1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')

    dt1_utc = dt1.astimezone(timezone.utc)
    dt2_utc = dt2.astimezone(timezone.utc)

    diff = abs(int((dt1_utc - dt2_utc).total_seconds()))

    return diff

T = int(input())

for i in range(T):
    t1 = input().strip()
    t2 = input().strip()
    diff = get_time_diff(t1, t2)
    print(diff)
