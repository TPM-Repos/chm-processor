RuleRenamingFinished Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : RuleRenamingFinished Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the processing of an individual rule is finished. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event RuleRenamingFinished As EventHandler(Of RenameRuleEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler(Of RenameRuleEventArgs)
     
    AddHandler instance.RuleRenamingFinished, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RenameRuleEventArgs> RuleRenamingFinished  
  
# Event Data

The event handler receives an argument of type [RenameRuleEventArgs](topic10306.md) containing data related to this event. The following **RenameRuleEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ContainerName](topic10314.md)| Gets the name of the rule container.   
[RuleName](topic10315.md)| Gets the name of the rule in a format specific to the type of container.   
[RuleText](topic10316.md)| Gets the text of the rule.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)


