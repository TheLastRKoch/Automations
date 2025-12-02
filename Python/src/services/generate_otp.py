import pyotp


class ServiceGenerateOTP:

    def run(self):

        otp_secret = input("Please type the OTP secret\n")
        totp = pyotp.TOTP(otp_secret)
        print("Current OTP:", totp.now())
