Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddInput Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectChildSpecificationProjectDef Class](topic4067.md) : AddInput Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_constantName_
    The constant name to bind.

Glossary Item Box

Adds a new input binging to this project definition. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function AddInput( _
       ByVal _constantName_ As String _
    ) As [ProjectChildSpecificationInputDef](topic4047.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectChildSpecificationProjectDef](topic4067.md)
    Dim constantName As String
    Dim value As [ProjectChildSpecificationInputDef](topic4047.md)
     
    value = instance.AddInput(constantName)  
  
C#|   
---|---  
      
    
    public [ProjectChildSpecificationInputDef](topic4047.md) AddInput( 
       string _constantName_
    )  
  
#### Parameters

 _constantName_
    The constant name to bind.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectChildSpecificationProjectDef Class](topic4067.md)   
[ProjectChildSpecificationProjectDef Members](topic4068.md)


