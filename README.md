# facial-recognition-system-project
The objective is to make a facial detection based entry system. Which will first detect a face of person and then look for the same face in it's database. If match is found it will return the name and other information about that person and also record the  attendance with date and time
Steps in brief:
-encode the images of users
-encoding data gathered by webcam
-find the mathch of pic collected by webcam
-If match found than record the attendence 

BUSINESS BENEFITS

Error-free and accurate- 
The Facial Recognition attendance system delivers accurate data with minimal human intervention.
Fast processing nature and doesn’t need any contact with users-
With current identity verification methods, users have to remember passwords, show I.D. cards, and faces other inconveniences. One possible solution is biometric identification via facial recognition technology.
No loopholes-
humans may become less attentive but it's harder to cheat a Machine.
More advanced security features-
Only the user whose face has been authorized to log into a system can gain access to it and it is almost impossible to hack.
Faster payment options -
Rather than entering their card details or e-wallet details, payment gateways can simply use an individual’s facial features to successfully complete a transaction.
Monitoring employee productivity-
Employees do not have to scan their fingerprints or ID cards to clock hours, the system will automatically identify when they come in and leave and log their hours accordingly

Assumptions

-Data of Allowed people is known to system 
-One person at a time is allowed to enter 
-No person is wearing masks or anything which cover the face
-The images are stored by the names of the employees.

Advice of using face recognition system (This improves accuracy)
-stay straight in front of camera
-good illumination is required 
-users are advised to submit their latest pic 
-also it is advised to users to give a good resolution pic

ISSUES WITH SOLUTION

May not recognize person
Solution:  have a backup entry system based on login credentials
May allow the wrong person
Solution: SMS alerts using python on entry/exit

