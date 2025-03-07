Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsEnabledChanged Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandMonitor Interface](topic158.md) : IsEnabledChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [IsEnabled](topic169.md) property changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event IsEnabledChanged As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandMonitor](topic158.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.IsEnabledChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> IsEnabledChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandMonitor Interface](topic158.md)   
[ICommandMonitor Members](topic159.md)


