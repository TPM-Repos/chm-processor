ReportMethod Delegate   
  
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


