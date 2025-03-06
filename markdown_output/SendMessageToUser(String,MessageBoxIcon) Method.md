![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SendMessageToUser(String,MessageBoxIcon) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic330.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IInteraction Interface](topic321.md) > [SendMessageToUser Method](topic329.md) : SendMessageToUser(String,MessageBoxIcon) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message to send.

_icon_
    The icon shown in the message box.

Glossary Item Box

Sends a message to the user of the application. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Sub SendMessageToUser( _
       ByVal _message_ As String, _
       ByVal _icon_ As MessageBoxIcon _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IInteraction](topic321.md)
    Dim message As String
    Dim icon As MessageBoxIcon
     
    instance.SendMessageToUser(message, icon)  
  
C#|   
---|---  
      
    
    void SendMessageToUser( 
       string _message_ ,
       MessageBoxIcon _icon_
    )  
  
#### Parameters

 _message_
    The message to send.
_icon_
    The icon shown in the message box.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IInteraction Interface](topic321.md)   
[IInteraction Members](topic322.md)   
[Overload List](topic329.md)

©2024 DriveWorks Ltd. All Rights Reserved.
