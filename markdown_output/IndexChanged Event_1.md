Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IndexChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTask Class](topic6407.md) : IndexChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised when the index of the task has changed in the parent collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event IndexChanged As EventHandler(Of ValueChangedEventArgs(Of Integer))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTask](topic6407.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of Integer))
     
    AddHandler instance.IndexChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs<int>> IndexChanged  
  
# Event Data

The event handler receives an argument of type [ValueChangedEventArgs<T>](topic5834.md) containing data related to this event. The following **ValueChangedEventArgs <T>** properties provide information specific to this event.

Property| Description  
---|---  
[NewValue](topic5841.md)| Gets the new value.   
[OldValue](topic5842.md)| Gets the old value.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTask Class](topic6407.md)   
[ComponentTask Members](topic6408.md)


