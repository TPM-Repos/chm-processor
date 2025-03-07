Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsAvailableChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommand Interface](topic77.md) : IsAvailableChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [IsAvailable](topic87.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event IsAvailableChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommand](topic77.md)
    Dim handler As EventHandler
     
    AddHandler instance.IsAvailableChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler IsAvailableChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommand Interface](topic77.md)   
[ICommand Members](topic78.md)


