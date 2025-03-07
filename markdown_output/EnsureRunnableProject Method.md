Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnsureRunnableProject Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : EnsureRunnableProject Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns if the current specification is valid or not. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EnsureRunnableProject() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim value As Boolean
     
    value = instance.EnsureRunnableProject()  
  
C#|   
---|---  
      
    
    public bool EnsureRunnableProject()  
  
#### Return Value

True if the specification is valid.

# Remarks

Invalid specifications contain a transition with no target state or a running state that transitions to another running state.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


