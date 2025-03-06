![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReportMethod Delegate   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic10006.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) : ReportMethod Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message to record.

_isError_
    Whether or not the message is an error.

Glossary Item Box

Signature for a delegate that is used for reporting. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ReportMethod( _
       ByVal _message_ As String, _
       ByVal _isError_ As Boolean _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As New [ReportMethod](topic10006.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate void ReportMethod( 
       string _message_ ,
       bool _isError_
    )  
  
#### Parameters

 _message_
    The message to record.
_isError_
    Whether or not the message is an error.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReportMethod Members](topic10006.md)   
[DriveWorks.GroupMaintenance Namespace](topic9628.md)

©2024 DriveWorks Ltd. All Rights Reserved.
