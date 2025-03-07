Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateMessage Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectMessages Class](topic4627.md) : CreateMessage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_code_
    

Glossary Item Box

Creates and returns a new message. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Function CreateMessage( _
       ByVal _code_ As Integer _
    ) As [ProjectMessage](topic4601.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectMessages](topic4627.md)
    Dim code As Integer
    Dim value As [ProjectMessage](topic4601.md)
     
    value = instance.CreateMessage(code)  
  
C#|   
---|---  
      
    
    public abstract [ProjectMessage](topic4601.md) CreateMessage( 
       int _code_
    )  
  
#### Parameters

 _code_
    

#### Return Value

The newly created message.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectMessages Class](topic4627.md)   
[ProjectMessages Members](topic4628.md)


