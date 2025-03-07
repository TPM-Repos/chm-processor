Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandNotRegisteredException Constructor(String,Exception)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [CommandNotRegisteredException Class](topic709.md) > [CommandNotRegisteredException Constructor](topic715.md) : CommandNotRegisteredException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    

_inner_
    

Glossary Item Box

Creates a new instance of the [CommandNotRegisteredException](topic709.md) class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _commandName_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim commandName As String
    Dim inner As Exception
     
    Dim instance As New [CommandNotRegisteredException](topic709.md)(commandName, inner)  
  
C#|   
---|---  
      
    
    public CommandNotRegisteredException( 
       string _commandName_ ,
       Exception _inner_
    )  
  
#### Parameters

 _commandName_
    
_inner_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CommandNotRegisteredException Class](topic709.md)   
[CommandNotRegisteredException Members](topic710.md)   
[Overload List](topic715.md)


