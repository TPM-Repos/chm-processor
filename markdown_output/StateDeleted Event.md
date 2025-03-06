       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StateDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [States Class](topic11612.md) : StateDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a state is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event StateDeleted As [StateEventHandler](topic11825.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [States](topic11612.md)
    Dim handler As [StateEventHandler](topic11825.md)
     
    AddHandler instance.StateDeleted, handler  
  
C#|   
---|---  
      
    
    public event [StateEventHandler](topic11825.md) StateDeleted  
  
# Event Data

The event handler receives an argument of type [StateEventArgs](topic11590.md) containing data related to this event. The following **StateEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[State](topic11600.md)| Gets the state which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[States Class](topic11612.md)   
[States Members](topic11613.md)


