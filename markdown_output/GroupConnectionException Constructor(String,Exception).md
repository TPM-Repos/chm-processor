Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GroupConnectionException Constructor(String,Exception)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupConnectionException Class](topic3049.md) > [GroupConnectionException Constructor](topic3055.md) : GroupConnectionException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    A message that describes the error.

_inner_
    The inner exception.

Glossary Item Box

Creates an instance of the [GroupConnectionException](topic3049.md) class. 

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
     
    Dim instance As New [GroupConnectionException](topic3049.md)(message, inner)  
  
C#|   
---|---  
      
    
    public GroupConnectionException( 
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

[GroupConnectionException Class](topic3049.md)   
[GroupConnectionException Members](topic3050.md)   
[Overload List](topic3055.md)


