Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Deleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [State Class](topic11559.md) : Deleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [Delete](topic11565.md) method is called to delete the state. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event Deleted As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [State](topic11559.md)
    Dim handler As EventHandler
     
    AddHandler instance.Deleted, handler  
  
C#|   
---|---  
      
    
    public event EventHandler Deleted  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[State Class](topic11559.md)   
[State Members](topic11560.md)


