# Testing and Setting up Gmail.

## Setting up Gmail to allow unsecure apps to use googles system.

### Google won't allow regular passwords to be used on scripts like this die to security so they have another way called an App Password. This is needed for the script to email you the transcript and audio recordings.

1. This is easy to setup, it might take a few minutes as google has lots of pages and options.
2. To use Gmail's SMTP server, you need to generate an App Password.
3. This is a 16-character password that you provide instead of your regular email password.
4. This provides a more secure login.

### Here are the steps to generate an App Password:

1. Go to your Google Account.
2. Select Security.
3. Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because:
   - 2-Step Verification is not set up for your account.
   - 2-Step Verification is only set up for security keys.
   - Your account is through work, school, or other organization.
   - You turned on Advanced Protection.
4. At the bottom, choose Select app and choose the app you using and then Select device and choose the device you’re using and then Generate.
5. Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device.
6. Select Done.

Once you have generated the App Password, you can use it in your script where you need to provide the Gmail password.

### Remember, do not share this App Password with anyone else. Google will never ask for this information.

## Run python gmail.py

python .\gmail.py

The options given.

Enter the recipient's email address: Add here the email you want to send to
Enter your Gmail address: Your email address
Enter your Gmail password: The none secure password is needed here
