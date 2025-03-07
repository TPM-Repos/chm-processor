Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsRunningChanging Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : IsRunningChanging Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a specification is about to enter or leave a running state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event IsRunningChanging As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler
     
    AddHandler instance.IsRunningChanging, handler  
  
C#|   
---|---  
      
    
    public event EventHandler IsRunningChanging  
  
# Remarks

There is a chance that the specification state might not change due to exceptions etc. Typically this can be used to know when a specification (and its project) is about to close (via cancel or transition etc).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


