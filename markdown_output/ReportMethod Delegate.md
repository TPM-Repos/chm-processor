       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Sub ReportMethod( _
       ByVal _message_ As String, _
       ByVal _isError_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReportMethod Members](topic10006.md)   
[DriveWorks.GroupMaintenance Namespace](topic9628.md)

©2024 DriveWorks Ltd. All Rights Reserved.
