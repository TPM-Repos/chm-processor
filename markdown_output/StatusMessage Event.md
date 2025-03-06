![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StatusMessage Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9796.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupProcess Class](topic9776.md) : StatusMessage Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever there is a status message event from the process. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event StatusMessage As EventHandler(Of StatusMessageEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupProcess](topic9776.md)
    Dim handler As EventHandler(Of StatusMessageEventArgs)
     
    AddHandler instance.StatusMessage, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<StatusMessageEventArgs> StatusMessage  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [StatusMessageEventArgs](topic9981.md) containing data related to this event. The following **StatusMessageEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[CreatedAt](topic9988.md)| Gets the creation date of this event in a localized local long time string.   
[CreationTime](topic9989.md)| Gets the creation time of this event in UTC.   
[IsError](topic9990.md)| Whether or not this message is an error.   
[Message](topic9991.md)| Gets the message for this status event.   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CopyGroupProcess Class](topic9776.md)   
[CopyGroupProcess Members](topic9777.md)

©2024 DriveWorks Ltd. All Rights Reserved.
