import csv,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os



def write_tree_to_file(path, output_file, level=0):
    with open(output_file, 'w',encoding='utf8') as f:
        dir_list = os.listdir(path)
        for i in range(len(dir_list)):
            file_path = os.path.join(path, dir_list[i])
            if os.path.isdir(file_path):
                f.write("|   " * level + "+---" + dir_list[i] + "/\n")
                write_tree_to_file(file_path, output_file, level+1)
            else:
                f.write("|   " * level + "+---" + dir_list[i] + "\n")

path=os.path.abspath("")
output_file = 'exchange_rate.csv'

write_tree_to_file(path, output_file)

print(9,path)
for a,b,c in os.walk(path):
  print(a,b,c)
