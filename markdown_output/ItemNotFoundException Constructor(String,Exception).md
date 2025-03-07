Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ItemNotFoundException Constructor(String,Exception)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ItemNotFoundException Class](topic3571.md) > [ItemNotFoundException Constructor](topic3577.md) : ItemNotFoundException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    The message which describes the error.

_innerException_
    The inner exception.

Glossary Item Box

Initializes a new instance of the [ItemNotFoundException](topic3571.md) class with a specified error message. 

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
     
    Dim instance As New [ItemNotFoundException](topic3571.md)(message, innerException)  
  
C#|   
---|---  
      
    
    public ItemNotFoundException( 
       string _message_ ,
       Exception _innerException_
    )  
  
#### Parameters

 _message_
    The message which describes the error.
_innerException_
    The inner exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ItemNotFoundException Class](topic3571.md)   
[ItemNotFoundException Members](topic3572.md)   
[Overload List](topic3577.md)


