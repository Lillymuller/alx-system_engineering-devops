Postmortem

Blog Image Upload Outage Postmortem:
Issue Summary:
On Tuesday between 11:00 EAT and 2:00 EAT, we experienced an outage affecting image uploads on our blogging platform. This prevented users from adding visuals to their blog posts, impacting approximately 30% of our active user base during that time window.

The root cause of the issue was identified as a bug in our recently deployed image resizing service.

  Timeline:
11:00 AM EAT : Our system monitoring tools detected a significant increase in error rates for the image upload functionality.
11:15 AM EAT : An engineer investigating the alert identified a surge in failed image uploads within the newly implemented image resizing service.
11:30 AM EAT : Initial troubleshooting focused on potential network issues between our application and the image resizing service. This path proved to be a dead end.
12:00 AM EAT : The engineering team shifted focus towards the image resizing service code itself. Code review revealed a bug in the logic responsible for handling large image files.
1:00 AM EAT : A hotfix was deployed, disabling the image resizing functionality temporarily and reverting to the original image upload process. This restored image upload functionality for users.
2:00 AM EAT : The image resizing service code was patched to address the identified bug. Rigorous testing confirmed successful image resizing and upload functionality.
2:10 AM EAT : The image resizing service was re-enabled, offering users the image resizing option once again.

Root Cause and Resolution:
The root cause of the outage was a bug in the image resizing service, specifically within the logic handling large image files. This bug caused the service to malfunction and return errors during the upload process.
To resolve the issue, we deployed a hotfix that temporarily disabled the image resizing functionality. This allowed users to continue uploading images without the resizing feature. Subsequently, a permanent fix was implemented through a code patch that addressed the bug in the image resizing logic. Additionally, the image resizing service underwent thorough testing to ensure proper functionality before being re-enabled.
Corrective and Preventative Measures:
Moving forward, we will be implementing the following corrective and preventative measures:

Improved Code Review Process: We will be strengthening our code review process to include a specific focus on edge cases and handling of large data files.
Enhanced Monitoring and Alerting: We will be refining our monitoring and alerting system to provide more granular insights into the performance of the image resizing service. This will enable faster detection of potential issues in the future.
Automated Testing: We will be implementing automated testing specifically designed to validate the image resizing functionality, particularly its ability to handle various image sizes.
Rollback Strategy: We will be establishing a clearer rollback strategy for newly deployed services. This will allow us to quickly revert to a previous stable version in case of unforeseen issues.
By implementing these measures, we aim to minimize the risk of similar outages occurring in the future and ensure a more reliable image upload experience for our users.

