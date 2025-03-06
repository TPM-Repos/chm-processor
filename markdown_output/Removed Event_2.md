Removed Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskConditions Class](topic6561.md) : Removed Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised whenever a condition has been removed from this collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event Removed As EventHandler(Of ComponentTaskConditionEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskConditions](topic6561.md)
    Dim handler As EventHandler(Of ComponentTaskConditionEventArgs)
     
    AddHandler instance.Removed, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ComponentTaskConditionEventArgs> Removed  
  
# Event Data

The event handler receives an argument of type [ComponentTaskConditionEventArgs](topic6529.md) containing data related to this event. The following **ComponentTaskConditionEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Condition](topic6535.md)| Gets the condition involved in the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskConditions Class](topic6561.md)   
[ComponentTaskConditions Members](topic6562.md)


