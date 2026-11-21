
def parse_ticket_id(ticket_id):
    if not isinstance(ticket_id, str):
        return None

    parts = ticket_id.strip().split('-')

    if len(parts) != 3:
        return None

    prefix, year, serial = parts

    if not prefix.isalnum() or not year.isdigit() or not serial.isdigit():
        return None

    return prefix.upper(), int(year), int(serial)


def total_fines(amounts_csv):
    if not isinstance(amounts_csv, str):
        return 0

    if not amounts_csv.strip():
        return 0

    try:
        amounts = [int(a.strip()) for a in amounts_csv.split(',')]

        if any(amount < 0 for amount in amounts):
            return 0

        total = sum(amounts)

        return min(total, 10000)

    except ValueError:
        return 0


def speed_excess(reading):
    if not isinstance(reading, str):
        return None

    parts = reading.strip().split('/')

    if len(parts) != 2:
        return None

    speed, limit = parts

    try:
        speed = int(speed.strip())
        limit = int(limit.strip())

        if speed < 0 or limit <= 0:
            return None

        return (speed - limit) * 100 // limit

    except ValueError:
        return None


def main():
    print("==== Running parse_ticket_id ====")
    user_input = input("Enter a ticket ID (e.g. TF-2024-0456): ")
    result = parse_ticket_id(user_input)
    print("Ticket Prefix, Year and Serial:", result)

    print("\n==== Running total_fines ====")
    user_input = input("Enter fine amounts as CSV (e.g. 500,1200,300): ")
    result = total_fines(user_input)
    print("Total Fines:", result)

    print("\n==== Running speed_excess ====")
    user_input = input("Enter speed/limit (e.g. 72/60): ")
    result = speed_excess(user_input)
    print("Percent Over Limit:", result)


if __name__ == "__main__":
    main()
