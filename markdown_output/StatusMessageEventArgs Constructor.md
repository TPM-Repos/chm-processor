![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StatusMessageEventArgs Constructor   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9987.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [StatusMessageEventArgs Class](topic9981.md) : StatusMessageEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message for this status event.

_isError_
    Whether or not this message is an error.

Glossary Item Box

Creates a new instance of the [StatusMessageEventArgs](topic9981.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _isError_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim message As String
    Dim isError As Boolean
     
    Dim instance As New [StatusMessageEventArgs](topic9981.md)(message, isError)  
  
C#|   
---|---  
      
    
    public StatusMessageEventArgs( 
       string _message_ ,
       bool _isError_
    )  
  
#### Parameters

 _message_
    The message for this status event.
_isError_
    Whether or not this message is an error.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StatusMessageEventArgs Class](topic9981.md)   
[StatusMessageEventArgs Members](topic9982.md)

©2024 DriveWorks Ltd. All Rights Reserved.
