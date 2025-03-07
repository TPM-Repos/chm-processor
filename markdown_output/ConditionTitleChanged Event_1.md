Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConditionTitleChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseConditions Class](topic6682.md) : ConditionTitleChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised whenever the title of a condition in the collection changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ConditionTitleChanged As EventHandler(Of ValueChangedEventArgs(Of String))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseConditions](topic6682.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of String))
     
    AddHandler instance.ConditionTitleChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ValueChangedEventArgs<string>> ConditionTitleChanged  
  
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

[ComponentTaskReleaseConditions Class](topic6682.md)   
[ComponentTaskReleaseConditions Members](topic6683.md)


