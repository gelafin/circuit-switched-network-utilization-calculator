# Author: Mark Mendez
# Date: 01/29/2022


def calculate_utilization_circuit_switched(total_user_count : int, utilization_per_user: list[dict]):
    """
    Calculates total utilization in a circuit-switched network with equal bandwidth share among users
    :param total_user_count: number of users sharing equal bandwidth
    :param utilization_per_user: list of dicts in the following form, where each dict is a group of users who have
                                 the exact same utilization:
                                 {'user_count': int, 'utilization_percent_per_user': int}
    :return: total percent utilization of the network
    """
    # validate user count
    user_count_validation = sum([group['user_count'] for group in utilization_per_user])
    if total_user_count != user_count_validation:
        raise ValueError('check your total user count and per user count; they have to match')

    bandwidth_percent_allocated_per_user = 100 / total_user_count

    total_utilization_decimal = 0
    for user_group in utilization_per_user:
        group_user_count = user_group['user_count']
        group_utilization_multiplier = user_group['utilization_percent_per_user'] / 100
        bandwidth_allocated_per_user_multiplier = bandwidth_percent_allocated_per_user / 100

        total_utilization_decimal += (group_user_count
                                      * group_utilization_multiplier
                                      * bandwidth_allocated_per_user_multiplier
                                      )

    total_utilization_percent = total_utilization_decimal * 100

    return total_utilization_percent


if __name__ == '__main__':
    # test
    total_user_count = 5  # this should match the total per-user user_counts
    utilization_per_user = [
        {'user_count': 2, 'utilization_percent_per_user': 85},
        {'user_count': 2, 'utilization_percent_per_user': 44},
        {'user_count': 1, 'utilization_percent_per_user': 11}
    ]

    result = calculate_utilization_circuit_switched(total_user_count, utilization_per_user)
    print('\nutilization percent: ', result)


