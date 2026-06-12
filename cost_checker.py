import boto3
from datetime import datetime, timedelta

def get_aws_cost():
    client = boto3.client('ce', region_name='us-east-1')
    end = datetime.today().strftime('%Y-%m-%d')
    start = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    response = client.get_cost_and_usage(
        TimePeriod={'Start': start, 'End': end},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )
    amount = float(response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount'])
    unit = response['ResultsByTime'][0]['Total']['UnblendedCost']['Unit']
    print(f"AWS Cost (Last 30 days): {amount:.2f} {unit}")
    return amount

def check_threshold(cost, threshold=10.0):
    if cost > threshold:
        print(f"ALERT: Cost ${cost:.2f} exceeded threshold ${threshold:.2f}")
        return True
    else:
        print(f"OK: Cost ${cost:.2f} is within limit ${threshold:.2f}")
        return False

if __name__ == "__main__":
    cost = get_aws_cost()
    check_threshold(cost)