Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDefault Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationFlowDefinition Class](topic11387.md) : IsDefault Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets whether the current specification-flow is the default specification-flow. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property IsDefault As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationFlowDefinition](topic11387.md)
    Dim value As Boolean
     
    value = instance.IsDefault  
  
C#|   
---|---  
      
    
    public bool IsDefault {get;}  
  
# Remarks

If the specification flow has not been customized, a default specification-flow is loaded from the Engine.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationFlowDefinition Class](topic11387.md)   
[SpecificationFlowDefinition Members](topic11388.md)


