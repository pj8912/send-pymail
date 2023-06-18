from mailer import Mailer

mail = Mailer(email='sender_email', password='sender_pwd')
mail.send(receiver='receiver_email', subject='TEST', message='From Python!')

