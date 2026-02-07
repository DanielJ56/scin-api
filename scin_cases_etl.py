from google.cloud import bigquery
import pandas as pd
import ast

client = bigquery.Client.from_service_account_json("service_account.json")

query = "select * from scinattempt2.scin.scin_data;"
df = client.query(query).to_dataframe()
outcomes = df[["case_id",
               "weighted_skin_condition_label","sex_at_birth","age_group","fitzpatrick_skin_type",
               "textures_raised_or_bumpy","textures_flat","textures_rough_or_flaky","textures_fluid_filled",
               "body_parts_head_or_neck","body_parts_arm","body_parts_palm","body_parts_back_of_hand","body_parts_torso_front",
               "body_parts_torso_back","body_parts_genitalia_or_groin","body_parts_buttocks","body_parts_leg",
               "body_parts_foot_top_or_side","body_parts_foot_sole","body_parts_other","condition_symptoms_bothersome_appearance",
               "condition_symptoms_bleeding","condition_symptoms_increasing_size","condition_symptoms_darkening",
               "condition_symptoms_itching","condition_symptoms_burning","condition_symptoms_pain",
               "condition_symptoms_no_relevant_experience","other_symptoms_fever","other_symptoms_chills","other_symptoms_fatigue",
               "other_symptoms_joint_pain","other_symptoms_mouth_sores","other_symptoms_shortness_of_breath",
               "other_symptoms_no_relevant_symptoms","related_category","condition_duration","image_1_path","image_2_path","image_3_path",
               "dermatologist_skin_condition_confidence","dermatologist_skin_condition_on_label_name"]]

diagnosis = [["case_id","Diagnosis"]]
diag_header = ["case_id","Diagnosis"]
undiagnosed_cases = []
for i,(idx,row) in enumerate(outcomes.iterrows()):
    diagnoses = ast.literal_eval(row["weighted_skin_condition_label"])
    if (diagnoses == {}):

        undiagnosed_cases.append(row["case_id"])
    else:
        diagnosis.append([row["case_id"],max(diagnoses,key=diagnoses.get)])

diagnosis_df = pd.DataFrame(diagnosis,columns=diag_header)
outcomes = outcomes[~outcomes["case_id"].isin(undiagnosed_cases)]
outcomes_final = pd.merge(outcomes,diagnosis_df, on="case_id")

table_id = "scinattempt2.scin.transformed_data"
job = client.load_table_from_dataframe(
    outcomes_final,
    table_id,
    job_config=bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
)

print("Loaded")