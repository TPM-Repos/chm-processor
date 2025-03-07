Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsValidChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandMonitor Interface](topic158.md) : IsValidChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [IsValid](topic170.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event IsValidChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandMonitor](topic158.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.IsValidChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> IsValidChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandMonitor Interface](topic158.md)   
[ICommandMonitor Members](topic159.md)


