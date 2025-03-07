Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NameChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [ExecutableNodeBase Class](topic6938.md) : NameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when the name of the node has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event NameChanged As EventHandler(Of ValueChangedEventArgs(Of String))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ExecutableNodeBase](topic6938.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of String))
     
    AddHandler instance.NameChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs<string>> NameChanged  
  
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

[ExecutableNodeBase Class](topic6938.md)   
[ExecutableNodeBase Members](topic6939.md)


