Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
LocationChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTask Class](topic6407.md) : LocationChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The even that gets raised when the location of the task has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event LocationChanged As EventHandler(Of ValueChangedEventArgs(Of ComponentTaskSequenceLocation))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTask](topic6407.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of ComponentTaskSequenceLocation))
     
    AddHandler instance.LocationChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs<ComponentTaskSequenceLocation>> LocationChanged  
  
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


