trials = 6

inputs = [0, 1, 0, 0, 0, 1, 0]
weights = [0, 0, 0, 0, 0, 0, 0]
desired_result = 1
learning_rate = 0.20


def eval_neural_network(input_vector, weight_vector):
    result = 0
    weight_index = 0
    for input_value in input_vector:
        layer_value = input_value * weight_vector[weight_index]
        weight_index += 1
        result += layer_value

    return round(result, 2)


def eval_neural_net_error(desired, actual):
    return desired - actual


def learn(input_vector, weight_vector):
    index = 0
    for weight in weight_vector:
        if input_vector[index] > 0:
            weights[index] = weight + learning_rate
        index += 1


def print_all(result, error):
    print(result)
    print(error)
    print(weights)
    print()


def train(trials):
    i = 0
    while i < trials:
        neural_net_result = eval_neural_network(inputs, weights)
        neural_net_error = eval_neural_net_error(desired_result, neural_net_result)
        print_all(neural_net_result, neural_net_error)
        learn(inputs, weights)
        i += 1
    print_all(neural_net_result, neural_net_error)


train(trials)
