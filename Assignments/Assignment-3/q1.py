import numpy as np

class NeuralNetwork:
    def __init__(self, layer_sizes):
        """
        Initialize the neural network with given layer sizes.
        
        Parameters:
        layer_sizes (list): A list containing the number of neurons in each layer
        """
        self.layer_sizes = layer_sizes
        self.parameters = self.initialize_parameters()

    def initialize_parameters(self):
        """
        Initialize the parameters (weights and biases) for each layer.
        
        Returns:
        dict: A dictionary containing weights and biases for each layer
        """
        # TODO: Initialize weights and biases for each layer
        # Loop through each layer, except the last one
        # Initialize weights with small random values and biases with zeros
        pass

    def forward_propagation(self, X):
        """
        Perform forward propagation to compute the activations of all layers.
        
        Parameters:
        X (numpy array): The input data of shape (n_features, m_samples)
        
        Returns:
        dict: A dictionary containing activations for each layer
        """
        activations = {'A0': X}
        L = len(self.layer_sizes) - 1  # Number of layers

        # TODO: Implement forward propagation logic
        pass
        
        return activations

    def sigmoid(self, Z):
        """
        Compute the sigmoid activation function.
        
        Parameters:
        Z (numpy array): The input to the sigmoid function
        
        Returns:
        numpy array: The result of applying sigmoid to Z
        """
        # TODO: Implement the sigmoid function
        pass

    def sigmoid_derivative(self, A):
        """
        Compute the derivative of the sigmoid function.
        
        Parameters:
        A (numpy array): The activation values (output of the sigmoid)
        
        Returns:
        numpy array: The derivative of the sigmoid function
        """
        # TODO: Implement the derivative of the sigmoid function
        pass

    def compute_cost(self, Y, A_L):
        """
        Compute the cost using binary cross-entropy loss.
        
        Parameters:
        Y (numpy array): True labels (1 for positive class, 0 for negative class)
        A_L (numpy array): Predicted outputs from the last layer
        
        Returns:
        float: The computed cost
        """
        # TODO: Implement the binary cross-entropy cost function
        pass

    def backward_propagation(self, X, Y, activations):
        """
        Perform backward propagation to compute the gradients of the cost function with respect to parameters.
        
        Parameters:
        X (numpy array): The input data
        Y (numpy array): True labels
        activations (dict): A dictionary containing activations from forward propagation
        
        Returns:
        dict: A dictionary containing gradients for each layer
        """
        gradients = {}
        L = len(self.layer_sizes) - 1  # Number of layers
        m = X.shape[1]  # Number of samples

        # TODO: Implement backward propagation logic
        pass

        return gradients

    def update_parameters(self, gradients, learning_rate):
        """
        Update the parameters using gradient descent.
        
        Parameters:
        gradients (dict): A dictionary containing gradients for each layer
        learning_rate (float): The learning rate for the update
        """
        L = len(self.layer_sizes) - 1  # Number of layers

        # TODO: Implement parameter updates using gradient descent
        pass

    def train(self, X, Y, learning_rate, epochs):
        """
        Train the neural network using forward and backward propagation.
        
        Parameters:
        X (numpy array): The input data
        Y (numpy array): True labels
        learning_rate (float): The learning rate for training
        epochs (int): The number of epochs for training
        """
        for i in range(epochs):
            activations = self.forward_propagation(X)
            cost = self.compute_cost(Y, activations['A' + str(len(self.layer_sizes) - 1)])
            gradients = self.backward_propagation(X, Y, activations)
            self.update_parameters(gradients, learning_rate)

            if i % 100 == 0:  # Print the cost every 100 iterations
                print(f"Cost after epoch {i}: {cost}")

    def predict(self, X):
        """
        Predict the output using the trained network.
        
        Parameters:
        X (numpy array): The input data
        
        Returns:
        numpy array: The predicted output
        """
        activations = self.forward_propagation(X)
        probabilities = activations['A' + str(len(self.layer_sizes) - 1)]
        
        predictions = []
        for prob in probabilities:
            if prob>0.5:
                predictions.append(1)
            else:
                predictions.append(0)
                
        return predictions


def generate_data():
    """
    Generate a synthetic dataset with 50 samples and 1 feature.
    The labels are generated using a linear function y = m * x + c with added Gaussian noise.

    Returns:
    tuple: X (features) and Y (labels)
    """
    np.random.seed(0)  # For reproducibility

    # Generate 500 samples, each with 2 features (random values)
    X = np.random.randn(500, 2)  # 500 samples, 2 features

    # Define the linear function parameters
    m = np.array([1,2])  # Slope
    c = 1  # Intercept

    # Generate labels (Y) based on the linear function y = m * x + c
    Y = np.dot(X , m) + c

    # Add Gaussian noise with mean=0 and std=0.5 to simulate real-world data
    noise = np.random.normal(0, 0.5, Y.shape)  # Gaussian noise
    Y = Y + noise
    Y = 1/(1 + np.exp(-Y))
    
    Z = []
    for y in Y :
        if y>0.5:
            Z.append(1)
        else:
            Z.append(0)

    return X, Z



def main():
    """
    Main function to test the neural network.
    """
    # Generate the dataset
    X, Y = generate_data()

    # Define layer sizes (input layer 2 features, 5 hidden neurons, output layer 1 neuron)
    layer_sizes = [2, 5, 1]  # Example architecture

    # Create the neural network
    nn = NeuralNetwork(layer_sizes)

    # Train the neural network
    nn.train(X, Y, learning_rate=0.01, epochs=1000)

    # Predict on the dataset
    predictions = nn.predict(X)
    print("Predictions:")
    print(predictions)


if __name__ == "__main__":
    main()
