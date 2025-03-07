Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandUnavailableException Constructor(String,Exception)   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [CommandUnavailableException Class](topic719.md) > [CommandUnavailableException Constructor](topic725.md) : CommandUnavailableException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    

_inner_
    

Glossary Item Box

Creates a new instance of the [CommandUnavailableException](topic719.md) class. 

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
     
    Dim instance As New [CommandUnavailableException](topic719.md)(commandName, inner)  
  
C#|   
---|---  
      
    
    public CommandUnavailableException( 
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

[CommandUnavailableException Class](topic719.md)   
[CommandUnavailableException Members](topic720.md)   
[Overload List](topic725.md)


