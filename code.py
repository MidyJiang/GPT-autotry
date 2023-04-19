import csv,time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

# 函数: 发送邮件
def send_email(to_email):
    # 配置邮件参数
    sender_email = '782568799@qq.com'  # 发件人
    sender_password = 'svkjzmjipaczbehc' # 授权码，邮箱设置
    subject = 'code.py中，发送邮件'
    text = 'Attached please find the CSV file.'

    # 添加附件
    directory = '/github/workspace'
    filename = 'exchange_rate.csv'
    filepath = os.path.join(directory, filename)
    with open(filepath, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='csv')
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)

    # 创建邮件内容
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(text))
    message.attach(attachment)

    # 发送邮件
    try:
        server = smtplib.SMTP('smtp.qq.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())
        server.quit()
        print('Email sent')
    except Exception as e:
        print('Error:', e)

last_send_time = None
# 主程序
while True:
    # 记录时间并写入 CSV 文件中
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    print(current_time,end='.')
    with open('/github/workspace/exchange_rate.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([current_time])

    def print_tree(path, level=0):
        # 获取当前目录下的所有子文件夹和文件
        dir_list = os.listdir(path)

        for i in range(len(dir_list)):
            # 获取当前文件或文件夹的全路径
            file_path = os.path.join(path, dir_list[i])

            # 判断是否为文件夹
            if os.path.isdir(file_path):
                # 如果是文件夹，先以树状结构输出文件夹名并缩进
                print("|   " * level + "|--" + dir_list[i] + "/")

                # 递归调用函数，输出子文件夹和文件
                print_tree(file_path, level+1)
            else:
                # 如果是文件，输出文件名并缩进
                print("|   " * level + "|--" + dir_list[i])

    # 指定要遍历的路径
    path = os.path.abspath("")

    # 调用函数，以树状结构输出目录结构
    print_tree(path)
  
        
      
    # 每 15 分钟发送一次邮件
    if last_send_time is None or (time.time() - last_send_time) > 300:



        send_email('782568799@qq.com')
        last_send_time = time.time()

    # 等待 15 秒钟继续循环
    time.sleep(15)
