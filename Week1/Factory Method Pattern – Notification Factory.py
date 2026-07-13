from abc import ABC, abstractmethod


# Product Interface
class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


# Concrete Products
class EmailNotification(Notification):

    def send(self, message):
        print(f"Email Sent: {message}")


class SMSNotification(Notification):

    def send(self, message):
        print(f"SMS Sent: {message}")


class PushNotification(Notification):

    def send(self, message):
        print(f"Push Notification: {message}")


# Factory
class NotificationFactory:

    @staticmethod
    def create_notification(notification_type):

        if notification_type.lower() == "email":
            return EmailNotification()

        elif notification_type.lower() == "sms":
            return SMSNotification()

        elif notification_type.lower() == "push":
            return PushNotification()

        else:
            raise ValueError("Invalid Notification Type")


# Client Code
notification = NotificationFactory.create_notification("email")
notification.send("Welcome to the application!")

notification = NotificationFactory.create_notification("sms")
notification.send("OTP: 123456")

notification = NotificationFactory.create_notification("push")
notification.send("Your order has been shipped.")