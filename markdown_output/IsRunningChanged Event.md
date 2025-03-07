Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRunningChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : IsRunningChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when specification enters or leaves a running state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event IsRunningChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler
     
    AddHandler instance.IsRunningChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler IsRunningChanged  
  
# Remarks

If the specification enters the running state because a task requires it, the [IsRunningChanged](topic11262.md) event doesn't fire as it is intended to detect state changes as the result of a specification action such as a transition or copy operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


