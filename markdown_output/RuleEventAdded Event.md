       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RuleEventAdded Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectProfiler Class](topic4712.md) : RuleEventAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a rule based event occurs. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event RuleEventAdded As EventHandler(Of ProjectProfileRuleEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectProfiler](topic4712.md)
    Dim handler As EventHandler(Of ProjectProfileRuleEventArgs)
     
    AddHandler instance.RuleEventAdded, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ProjectProfileRuleEventArgs> RuleEventAdded  
  
# Event Data

The event handler receives an argument of type [ProjectProfileRuleEventArgs](topic4728.md) containing data related to this event. The following **ProjectProfileRuleEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[RuleEvent](topic4737.md)| Gets the project rule event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectProfiler Class](topic4712.md)   
[ProjectProfiler Members](topic4713.md)


