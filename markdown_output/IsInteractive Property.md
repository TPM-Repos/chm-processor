Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsInteractive Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IInteraction Interface](topic321.md) : IsInteractive Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets a value indicating whether the application is capable of interaction with a user. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property IsInteractive As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IInteraction](topic321.md)
    Dim value As Boolean
     
    value = instance.IsInteractive  
  
C#|   
---|---  
      
    
    bool IsInteractive {get;}  
  
#### Property Value

True if the application is running in an interactive environment, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IInteraction Interface](topic321.md)   
[IInteraction Members](topic322.md)


