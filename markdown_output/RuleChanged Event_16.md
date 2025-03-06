       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskRuleCollection Class](topic6723.md) : RuleChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The event that gets raised whenever a rule in the collection has changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event RuleChanged As EventHandler(Of ComponentTaskRuleEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskRuleCollection](topic6723.md)
    Dim handler As EventHandler(Of ComponentTaskRuleEventArgs)
     
    AddHandler instance.RuleChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ComponentTaskRuleEventArgs> RuleChanged  
  
# Event Data

The event handler receives an argument of type [ComponentTaskRuleEventArgs](topic2530.md) containing data related to this event. The following **ComponentTaskRuleEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Rule](topic2536.md)| Gets the rule associated with the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskRuleCollection Class](topic6723.md)   
[ComponentTaskRuleCollection Members](topic6724.md)


