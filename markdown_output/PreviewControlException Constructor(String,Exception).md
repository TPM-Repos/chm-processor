Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreviewControlException Constructor(String,Exception)   
  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _innerException_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[PreviewControlException Class](topic3801.md)   
[PreviewControlException Members](topic3802.md)   
[Overload List](topic3807.md)


