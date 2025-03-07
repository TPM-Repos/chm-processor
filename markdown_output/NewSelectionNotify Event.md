Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NewSelectionNotify Event   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks Namespace](topic13345.md) > [ISolidWorksState Interface](topic13419.md) : NewSelectionNotify Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Post-notifies the user program when the selection list has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event NewSelectionNotify As EventHandler(Of NewSelectionNotifyEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISolidWorksState](topic13419.md)
    Dim handler As EventHandler(Of NewSelectionNotifyEventArgs)
     
    AddHandler instance.NewSelectionNotify, handler  
  
C#|   
---|---  
      
    
    event EventHandler<NewSelectionNotifyEventArgs> NewSelectionNotify  
  
# Event Data

The event handler receives an argument of type [NewSelectionNotifyEventArgs](topic13867.md) containing data related to this event. The following **NewSelectionNotifyEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[IsDrawing](topic13874.md)| Gets whether a drawing is selection.   
[Success](topic13916.md)| Gets/sets the result of the event (default is True). (Inherited from [DriveWorks.SolidWorks.ResultEventArgs](topic13909.md))  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISolidWorksState Interface](topic13419.md)   
[ISolidWorksState Members](topic13420.md)


