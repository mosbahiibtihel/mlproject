import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            print("Before Loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            
            # Debug: print what we're sending to the preprocessor
            print("Features DataFrame columns:", features.columns.tolist())
            print("Features DataFrame:\n", features)
            
            # Check for any None or NaN values
            if features.isnull().any().any():
                print("Warning: Null values found in features")
                print(features[features.isnull().any(axis=1)])
            
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            print(f"Error in predict method: {e}")
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education: str,
        lunch: str,
        test_preparation_course: str,
        reading_score: float,
        writing_score: float
    ):
        # default values if None is passed (handles missing form data)
        self.gender = gender if gender is not None else "male"
        self.race_ethnicity = race_ethnicity if race_ethnicity is not None else "group A"
        self.parental_level_of_education = parental_level_of_education if parental_level_of_education is not None else "some college"
        self.lunch = lunch if lunch is not None else "standard"
        self.test_preparation_course = test_preparation_course if test_preparation_course is not None else "none"
        self.reading_score = reading_score if reading_score is not None else 70.0
        self.writing_score = writing_score if writing_score is not None else 70.0

    def get_data_as_data_frame(self):
        try:
            # Column names must match exactly what the preprocessor expects

            
            custom_data_input_dict = {
                "gender": [self.gender],
                "race/ethnicity": [self.race_ethnicity],
                "parental level of education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test preparation course": [self.test_preparation_course],
                "reading score": [self.reading_score],
                "writing score": [self.writing_score],
            }

            df = pd.DataFrame(custom_data_input_dict)
            print("Created DataFrame with columns:", df.columns.tolist())
            print("DataFrame values:\n", df)
            return df

        except Exception as e:
            raise CustomException(e, sys)