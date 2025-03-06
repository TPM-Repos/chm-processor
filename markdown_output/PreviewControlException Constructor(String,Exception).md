![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewControlException Constructor(String,Exception)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3809.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [PreviewControlException Class](topic3801.md) > [PreviewControlException Constructor](topic3807.md) : PreviewControlException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message for this exception.

_innerException_
    The inner error.

Glossary Item Box

Creates a new instance of the [PreviewControlException](topic3801.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _innerException_ As Exception _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim message As String
    Dim innerException As Exception
     
    Dim instance As New [PreviewControlException](topic3801.md)(message, innerException)  
  
C#|   
---|---  
      
    
    public PreviewControlException( 
       string _message_ ,
       Exception _innerException_
    )  
  
#### Parameters

 _message_
    The message for this exception.
_innerException_
    The inner error.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[PreviewControlException Class](topic3801.md)   
[PreviewControlException Members](topic3802.md)   
[Overload List](topic3807.md)

©2024 DriveWorks Ltd. All Rights Reserved.
