Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandInvocationException Constructor(String,Exception)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [CommandInvocationException Class](topic681.md) > [CommandInvocationException Constructor](topic687.md) : CommandInvocationException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_errorMessage_
    

_inner_
    

Glossary Item Box

Creates a new instance of the [CommandInvocationException](topic681.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _errorMessage_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim errorMessage As String
    Dim inner As Exception
     
    Dim instance As New [CommandInvocationException](topic681.md)(errorMessage, inner)  
  
C#|   
---|---  
      
    
    public CommandInvocationException( 
       string _errorMessage_ ,
       Exception _inner_
    )  
  
#### Parameters

 _errorMessage_
    
_inner_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CommandInvocationException Class](topic681.md)   
[CommandInvocationException Members](topic682.md)   
[Overload List](topic687.md)


