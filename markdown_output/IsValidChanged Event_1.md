Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsValidChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IHasValidation Interface](topic308.md) : IsValidChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Fires when the value of the [IsValid](topic313.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event IsValidChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasValidation](topic308.md)
    Dim handler As EventHandler
     
    AddHandler instance.IsValidChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler IsValidChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasValidation Interface](topic308.md)   
[IHasValidation Members](topic309.md)


