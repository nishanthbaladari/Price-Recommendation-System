{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyOWaVfhyjFRLrXzK2KbVaUE"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","source":["from google.colab import drive\n","drive.mount('/content/drive')\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"69pQVi6Cc8dr","executionInfo":{"status":"ok","timestamp":1713653490106,"user_tz":300,"elapsed":26917,"user":{"displayName":"Prathyusha Rekapalli","userId":"13935086091395680628"}},"outputId":"4b21fa73-7a42-451d-b913-20909187ee4a"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stdout","text":["Mounted at /content/drive\n"]}]},{"cell_type":"code","source":["file_path = \"/content/drive/MyDrive/G1/dataset_b1.csv\"\n"],"metadata":{"id":"jEuGA75wdrmo"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["model_path = \"/content/drive/My Drive/G1/b_classifier/artifacts/svm_model.pkl\""],"metadata":{"id":"SLeo1tQydvoK"},"execution_count":null,"outputs":[]},{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"OXr_wajzb5eq","executionInfo":{"status":"ok","timestamp":1713653582194,"user_tz":300,"elapsed":480,"user":{"displayName":"Prathyusha Rekapalli","userId":"13935086091395680628"}},"outputId":"13960df8-90ab-4e8e-9ef6-9be7e0000414"},"outputs":[{"output_type":"stream","name":"stdout","text":["Accuracy: 99.85000000000001 %\n"]}],"source":["import pandas as pd\n","from sklearn.metrics import accuracy_score\n","import joblib\n","import warnings\n","warnings.filterwarnings(\"ignore\")\n","\n","\n","# Load the dataset\n","data = pd.read_csv(file_path,names=[\"class\",\"values\"])\n","\n","# Load the trained SVM model\n","svm_model = joblib.load(model_path)\n","\n","def classify_b(value):\n","    # Predict the class for the input value\n","    class_label = svm_model.predict([[value]])[0]\n","    return class_label\n","\n","# Test the classify_b function and calculate accuracy\n","predicted_classes = [classify_b(value) for value in data['values']]\n","accuracy = accuracy_score(data['class'], predicted_classes) * 100\n","\n","# Print the accuracy\n","print(\"Accuracy:\", accuracy, \"%\")\n"]}]}