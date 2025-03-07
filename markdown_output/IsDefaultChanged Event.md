Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDefaultChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationFlowDefinition Class](topic11387.md) : IsDefaultChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the IsDefault property is changed after the specification flow is customized from default or is reset back to default. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event IsDefaultChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationFlowDefinition](topic11387.md)
    Dim handler As EventHandler
     
    AddHandler instance.IsDefaultChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler IsDefaultChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationFlowDefinition Class](topic11387.md)   
[SpecificationFlowDefinition Members](topic11388.md)


