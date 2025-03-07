Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CopyGroupOptionsSerializerException Constructor(String,Exception)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [CopyGroupOptionsSerializerException Class](topic2615.md) > [CopyGroupOptionsSerializerException Constructor](topic2621.md) : CopyGroupOptionsSerializerException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message for this exception.

_innerException_
    The inner error.

Glossary Item Box

Creates a new instance of the [CopyGroupOptionsSerializerException](topic2615.md) class. 

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
     
    Dim instance As New [CopyGroupOptionsSerializerException](topic2615.md)(message, innerException)  
  
C#|   
---|---  
      
    
    public CopyGroupOptionsSerializerException( 
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

[CopyGroupOptionsSerializerException Class](topic2615.md)   
[CopyGroupOptionsSerializerException Members](topic2616.md)   
[Overload List](topic2621.md)


