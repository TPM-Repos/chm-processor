![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InvalidAttachmentsException Constructor(String[],String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3512.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [InvalidAttachmentsException Class](topic3504.md) > [InvalidAttachmentsException Constructor](topic3510.md) : InvalidAttachmentsException Constructor(String[],String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_attachments_
    The invalid attachments.

_message_
    The exception message.

Glossary Item Box

Creates a new instance of the [InvalidAttachmentsException](topic3504.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _attachments_() As String, _
       ByVal _message_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim attachments() As String
    Dim message As String
     
    Dim instance As New [InvalidAttachmentsException](topic3504.md)(attachments, message)  
  
C#|   
---|---  
      
    
    public InvalidAttachmentsException( 
       string[] _attachments_ ,
       string _message_
    )  
  
#### Parameters

 _attachments_
    The invalid attachments.
_message_
    The exception message.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[InvalidAttachmentsException Class](topic3504.md)   
[InvalidAttachmentsException Members](topic3505.md)   
[Overload List](topic3510.md)

©2024 DriveWorks Ltd. All Rights Reserved.
