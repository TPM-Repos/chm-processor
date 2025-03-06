RuleChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [INotifyRuleChanged Interface](topic5987.md) : RuleChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the rule for the object has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event RuleChanged As EventHandler(Of ValueChangedEventArgs(Of String))  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [INotifyRuleChanged](topic5987.md)
    Dim handler As EventHandler(Of ValueChangedEventArgs(Of String))
     
    AddHandler instance.RuleChanged, handler  
  
C#|   
---|---  
      
    
    event EventHandler<ValueChangedEventArgs<string>> RuleChanged  
  
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

[INotifyRuleChanged Interface](topic5987.md)   
[INotifyRuleChanged Members](topic5988.md)


