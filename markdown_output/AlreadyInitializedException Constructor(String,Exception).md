Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AlreadyInitializedException Constructor(String,Exception)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [AlreadyInitializedException Class](topic2403.md) > [AlreadyInitializedException Constructor](topic2409.md) : AlreadyInitializedException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    A message that describes the error.

_inner_
    The inner exception.

Glossary Item Box

Creates an instance of the [AlreadyInitializedException](topic2403.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim message As String
    Dim inner As Exception
     
    Dim instance As New [AlreadyInitializedException](topic2403.md)(message, inner)  
  
C#|   
---|---  
      
    
    public AlreadyInitializedException( 
       string _message_ ,
       Exception _inner_
    )  
  
#### Parameters

 _message_
    A message that describes the error.
_inner_
    The inner exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[AlreadyInitializedException Class](topic2403.md)   
[AlreadyInitializedException Members](topic2404.md)   
[Overload List](topic2409.md)


