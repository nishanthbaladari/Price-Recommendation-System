{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPK1HtBAbGd/72odWnKZoop"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"MB489RJMxFcl","executionInfo":{"status":"ok","timestamp":1713654690121,"user_tz":300,"elapsed":170496,"user":{"displayName":"Prathyusha Rekapalli","userId":"13935086091395680628"}},"outputId":"728167b8-7efc-4497-bcf8-5149909c9653"},"outputs":[{"output_type":"stream","name":"stdout","text":["Mounted at /content/drive\n"]}],"source":["from google.colab import drive\n","drive.mount('/content/drive')\n"]},{"cell_type":"code","source":["file_path = \"/content/drive/MyDrive/G1/dataset_o1.csv\"\n"],"metadata":{"id":"jbaGscBaxIG_"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["model_path = \"/content/drive/My Drive/G1/o_classifier/artifacts/svm_model_o1.pkl\""],"metadata":{"id":"CZBi-TZrxLAE"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["import pandas as pd\n","import joblib\n","from sklearn.metrics import accuracy_score\n","import numpy as np\n","\n","# Load the dataset\n","data = pd.read_csv(file_path, header=None)\n","# Replace column names with more descriptive names\n","data.columns = ['ID', 'Feature_1', 'Feature_2', 'Feature_3', 'Feature_4', 'Feature_5', 'Feature_6', 'Feature_7', 'Feature_8']\n","\n","# Load the trained SVM model\n","clf = joblib.load(model_path)\n","\n","# Classification function for all features\n","def classify_o(values_vector):\n","    class_label = clf.predict(np.array(values_vector).reshape(1, -1))[0]\n","    return class_label\n","\n","# Prepare the data\n","X = data.iloc[:, 1:].values\n","y = data['ID'].values\n","\n","# Predict the class labels for the dataset using classify_o\n","y_pred = [classify_o(row) for index, row in data.iloc[:, 1:].iterrows()]\n","\n","# Calculate and print the accuracy\n","accuracy = accuracy_score(y, y_pred) * 100\n","print(\"Accuracy:\", accuracy)\n"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"TXjtvkpHx-pp","executionInfo":{"status":"ok","timestamp":1713657969377,"user_tz":300,"elapsed":540,"user":{"displayName":"Prathyusha Rekapalli","userId":"13935086091395680628"}},"outputId":"620bfb1b-2005-490f-d256-97a83d3173f1"},"execution_count":8,"outputs":[{"output_type":"stream","name":"stdout","text":["Accuracy: 99.7\n"]}]}]}