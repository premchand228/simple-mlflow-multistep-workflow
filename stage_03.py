import mlflow
import datetime

with open("artifacts01.txt", "r") as f:
    text = f.read()


with open("artifacts02.txt", "w") as f:
    text = f.write(text + "added lines")

time_cur=datetime.datetime.now()
mlflow.log_metric("last_text", text)
mlflow.log_metric("time",time_cur)
print("end of stage 03")
print("pipe line is sucessfully ran")