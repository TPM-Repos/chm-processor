Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsValidChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommand Interface](topic77.md) : IsValidChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [IsValid](topic89.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event IsValidChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommand](topic77.md)
    Dim handler As EventHandler
     
    AddHandler instance.IsValidChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler IsValidChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommand Interface](topic77.md)   
[ICommand Members](topic78.md)


