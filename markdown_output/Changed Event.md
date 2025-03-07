Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Changed Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [INotifyChanged Interface](topic2257.md) : Changed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raise when the owning object has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Changed As EventHandler(Of EventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [INotifyChanged](topic2257.md)
    Dim handler As EventHandler(Of EventArgs)
     
    AddHandler instance.Changed, handler  
  
C#|   
---|---  
      
    
    event EventHandler<EventArgs> Changed  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[INotifyChanged Interface](topic2257.md)   
[INotifyChanged Members](topic2258.md)


