import time
from confluent_kafka.admin import AdminClient, NewTopic

def list_topics(admin_client):
    cluster_metadata = admin_client.list_topics(timeout=10)
    for topic in cluster_metadata.topics.values():
        print(f"Topic: {topic.topic}")
        for partition in topic.partitions.values():
            print(f"  Partition: {partition.id}")
            print(f"    Leader: {partition.leader}")
            print(f"    Replicas: {partition.replicas}")
            print(f"    ISRs: {partition.isrs}")

def list_consumer_groups(admin_client):
    consumer_groups = admin_client.list_consumer_groups()
    for group in consumer_groups:
        print(f"Consumer Group: {group}")

def describe_consumer_groups(admin_client):
    consumer_groups = admin_client.list_consumer_groups(timeout=10)
    for group in consumer_groups:
        group_metadata = admin_client.describe_consumer_groups([group])
        for g in group_metadata:
            print(f"Consumer Group: {g.group}")
            print(f"  State: {g.state}")
            print(f"  Protocol Type: {g.protocol_type}")
            print(f"  Protocol: {g.protocol}")
            print(f"  Members:")
            for member in g.members:
                print(f"    Member ID: {member.id}")
                print(f"      Client ID: {member.client_id}")
                print(f"      Client Host: {member.client_host}")
                print(f"      Assignment:")
                for topic, partitions in member.assignment.topic_partitions.items():
                    print(f"        Topic: {topic}")
                    print(f"        Partitions: {partitions}")

def main():
    admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})

    while True:
        print("\n--- Topics and Partitions ---")
        list_topics(admin_client)

        print("\n--- Consumer Groups ---")
        list_consumer_groups(admin_client)

        print("\n--- Consumer Group Descriptions ---")
        describe_consumer_groups(admin_client)

        time.sleep(10)

if __name__ == "__main__":
    main()
