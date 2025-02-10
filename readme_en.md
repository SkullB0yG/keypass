# KeyPass

KeyPass is a project designed to manage and store your passwords securely. This README will guide you through the installation, configuration, and usage of the project.

## Installation

1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/your-username/keypass.git
    cd keypass
    ```

2. Make sure you have Python installed. You can check with:
    ```sh
    python --version
    ```

3. Install the necessary dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

To integrate KeyPass with your shell, you need to add some lines to your `.zshrc` or `.bashrc` configuration file.

### Zsh

1. Open your `.zshrc` file:
    ```sh
    nano ~/.zshrc
    ```

2. Add the following line at the end of the file:
    ```sh
    source /path/to/keypass/keypass.zsh
    ```

3. Save and close the file, then reload the configuration:
    ```sh
    source ~/.zshrc
    ```

### Bash

1. Open your `.bashrc` file:
    ```sh
    nano ~/.bashrc
    ```

2. Add the following line at the end of the file:
    ```sh
    source /path/to/keypass/keypass.bash
    ```

3. Save and close the file, then reload the configuration:
    ```sh
    source ~/.bashrc
    ```

## Usage

Once you have configured KeyPass, you can use it directly from your terminal.

### Basic Commands

- **Add a password**:
    ```sh
    keypass add <name> <password>
    ```

- **Get a password**:
    ```sh
    keypass get <name>
    ```

- **Delete a password**:
    ```sh
    keypass delete <name>
    ```

## Contributing

If you want to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your changes (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or suggestions, please open an issue in the repository or contact the project maintainer.