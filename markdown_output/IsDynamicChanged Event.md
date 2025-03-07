Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
IsDynamicChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskProperty Class](topic6633.md) : IsDynamicChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised when the [IsDynamic](topic6643.md) property has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event IsDynamicChanged As EventHandler(Of ValueChangedEventArgs(Of Boolean))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskProperty](topic6633.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of Boolean))
     
    AddHandler instance.IsDynamicChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs<bool>> IsDynamicChanged  
  
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

[ComponentTaskProperty Class](topic6633.md)   
[ComponentTaskProperty Members](topic6634.md)


