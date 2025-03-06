![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UserMessage Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic533.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IUserMessageService Interface](topic526.md) : UserMessage Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a new user message is received. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event UserMessage As EventHandler(Of UserMessageEventArgs)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IUserMessageService](topic526.md)
    Dim handler As EventHandler(Of UserMessageEventArgs)
     
    AddHandler instance.UserMessage, handler  
  
C#|   
---|---  
      
    
    event EventHandler<UserMessageEventArgs> UserMessage  
  
# ![](dotnetimages/collapse.gif)Event Data

The event handler receives an argument of type [UserMessageEventArgs](topic5827.md) containing data related to this event. The following **UserMessageEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Message](topic5833.md)|   
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IUserMessageService Interface](topic526.md)   
[IUserMessageService Members](topic527.md)

©2024 DriveWorks Ltd. All Rights Reserved.
