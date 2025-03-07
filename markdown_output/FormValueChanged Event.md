Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
FormValueChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : FormValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised whenever a form value has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event FormValueChanged As EventHandler(Of ValueChangedEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs)
     
    AddHandler instance.FormValueChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs> FormValueChanged  
  
# Event Data

The event handler receives an argument of type [ValueChangedEventArgs](topic9575.md) containing data related to this event. The following **ValueChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[EventArgument](topic9584.md)| Gets the argument describing the source of this change.   
[NewValue](topic9585.md)| Gets the value of the property as it after the change.   
[OldValue](topic9586.md)| Gets the value of the property as it was before the change.   
[Property](topic9587.md)| Gets the property that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


