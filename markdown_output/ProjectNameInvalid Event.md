Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectNameInvalid Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationRequest Interface](topic1778.md) : ProjectNameInvalid Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when the specification is being processed and a project with the given name can't be located. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event ProjectNameInvalid As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationRequest](topic1778.md)
    Dim handler As EventHandler
     
    AddHandler instance.ProjectNameInvalid, handler  
  
C#|   
---|---  
      
    
    event EventHandler ProjectNameInvalid  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationRequest Interface](topic1778.md)   
[ISpecificationRequest Members](topic1779.md)


