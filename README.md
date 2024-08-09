## Bank Note Authentication

### Software and Tools Requirements
1. [GitHub Account](https://github.com)
2. [Docker](https://www.docker.com/)
3. [VS Code IDE](https://code.visualstudio.com/)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

### Create a New Environment
For local development, create a new environment using venv:
```
python -m venv venv
```

### Activate the Environment
On Windows:
```
venv\Scripts\activate
```

On macOS/Linux:
```
source venv/bin/activate
```

### Installation
#### Clone the Repository
```
git clone https://github.com/Github-Hashim/moneyAuthentication.git
```
#### Change the directory
```
cd bank-note-authentication
```

#### Install Dependencies
```
pip install -r requirements.txt
```

### Running Locally
#### Start the Flask Application
```
python app.py
```

#### Access the Application

Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Running with Docker

#### Build the Docker Image
```
docker build -t bank-note-authentication .
```

#### Run the Docker Container
```
docker run -p 5000:5000 bank-note-authentication
```

#### Access the Application
Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

#### Input Features
Enter the values for variance, skewness, curtosis, and entropy.

#### Submit and View Prediction
Click the "Predict" button to see if the banknote is classified as genuine or fake.

### Model Details
The application uses a pre-trained Decision Tree Classifier model saved in `classifier.pkl`. Ensure that the versions of scikit-learn and other dependencies match those used during model training.

### Troubleshooting
#### Port Already Allocated
If you encounter an error related to port allocation: 
Bind for 0.0.0.0:5000 failed: port is already allocated.

You can run the Docker container on a different port:
```
docker run -p 5001:5000 bank-note-authenticationS
```
#### Version Compatibility Issues
For errors related to version compatibility, especially with numpy and scikit-learn, ensure that the versions in `requirements.txt` match those used during model training. Update `requirements.txt` as necessary and rebuild the Docker image.

### License
This project is licensed under the MIT License. See the `LICENSE` file for details.

### Acknowledgements
- [scikit-learn](https://scikit-learn.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Docker](https://www.docker.com/)
